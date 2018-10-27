import pandas as pd
import json
import numpy as np
import math

import sys
import math
#read file
profiles = json.loads(open('input.json').read())
#set points
VALUES_POINT=[0,1,10,50,250]

total_importance=0
question_matches = []
total_profiles=len(profiles["profiles"])
current_profile_analisis=0

for profile in profiles["profiles"]: #all profiles
    current_profile_analisis=current_profile_analisis+1
    print("please wait %",current_profile_analisis/total_profiles*100)
    for question in profile["answers"]:#all question by profile
        for other_profile in profiles["profiles"]:#all profiles
            if profile["id"] != other_profile["id"]:#exclude same profiles
                for question_other_profile in (other_profile["answers"]):#all question of other profile
                    if question["questionId"] == question_other_profile["questionId"] and profile["id"] != other_profile["id"] :
                        #add to matriz the question matches
                        question_matches.append([profile["id"]
                                                ,other_profile["id"]
                                                ,question["questionId"]
                                                ,VALUES_POINT[question["importance"]],
                                                VALUES_POINT[question["importance"]] if(question_other_profile["answer"]in question["acceptableAnswers"]) else 0])
#convert question_matches to numpy array

question_matches=np.array(question_matches)
raw_data = {
        'profile_id': question_matches[:,0],
        'other_profile_id': question_matches[:,1],
        'question_id': question_matches[:,2],
        'possible_points' :question_matches[:,3],
        'real_points' :question_matches[:,4]}
#convert question_matches to dataframe  pandas
dt=pd.DataFrame(question_matches)

#rename columns
dt=dt.rename(index=str, columns={0: "profile_id", 1:"other_profile_id",2:'question_id',3:'possible_points',4:'real_points'})
#grup by id_profile and other_profile_id
sum=dt.groupby(['profile_id','other_profile_id']).sum()
#this function recovery a original names
sum=sum.reset_index()
#deleting a not necessary column
sum=sum.drop(["question_id"],axis=1)
#adding colunm that represent "The Match"
sum["percent"]= (sum["real_points"]/sum["possible_points"])
sum=sum.reset_index()
#cross to  get  "The Match" of other profiles
merge=pd.merge(sum,sum,left_on=["other_profile_id","profile_id"],right_on=["profile_id","other_profile_id"],how='inner')
merge=merge.reset_index();
#adding column that represent  "...match percentage for you and B, we just multiply your satisfactions...
merge["score"]= pow(merge["percent_x"]*merge["percent_y"],0.5)
#deliting a not necessary columns
merge=merge.drop(["index_y",'profile_id_y',"other_profile_id_y",'possible_points_y',"real_points_y","index_x",'index'],axis=1)
merge=merge.drop(["possible_points_x",'real_points_x',"percent_x",'percent_y'],axis=1)
merge=merge.reset_index()
merge=merge.sort_values("score",ascending=False)
merge=merge.reset_index()
merge=merge.drop(["level_0","index"],axis=1)
report=pd.DataFrame({
        'profile_id_x': [],
        'other_profile_id_x': [],
        'score': []})
for profile in profiles["profiles"]: #all profiles
    dt=merge[merge["profile_id_x"]==profile["id"]].sort_values('score',ascending=False).head(10)#get top10 by profiles
    report=pd.concat([report,dt])#concat
report.to_csv("top10_by_profiles.csv", sep='\t', encoding='utf-8')
print("end matching you can see the response in top10_by_profiles.csv file ")


