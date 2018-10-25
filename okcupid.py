import pandas as pd
import json

import sys
import math
#read file
profiles = json.loads(open('input.json').read())
VALUES_POINT=[0,1,10,50,250]
print("cantidad de profiles")
#print(len(leer["profiles"][0]))
#total points  by question macthed for each user
total_importance=0
#profile,other_profile,question_id,importance,acceptableAnswers
question_matches = []

for profile in profiles["profiles"]: #all profiles
    if(profile["id"] in [0,1,2]):
        for question in profile["answers"]:#all question by profile
            for other_profile in profiles["profiles"]:#all question others profiles
                if profile["id"] != other_profile["id"]:#exclude same profiles
                    for index ,question_other_profile in enumerate(other_profile["answers"]):#all question of other profile
                        if question["questionId"] == question_other_profile["questionId"] and profile["id"] != other_profile["id"] :
                            #add to matriz the question matches
                            question_matches.append([profile["id"]
                                                    ,other_profile["id"]
                                                    ,question["questionId"]
                                                    ,VALUES_POINT[question["importance"]],
                                                    VALUES_POINT[question["importance"]] if(question_other_profile["answer"]in question["acceptableAnswers"]) else 0])

print("fin questions matches")
sum=pd.DataFrame(question_matches)
#sum.rename(index=str, columns={"0": "profile_id", "1":"other_profile_id"})

#sum.to_csv("cruzes.csv", sep='\t', encoding='utf-8')
sum=sum.groupby([0,1]).sum()
sum_point= (sum[4]/sum[3])
#sum=pd.concat([sum,sum_point])
#sum.to_csv("sumas.csv", sep='\t', encoding='utf-8')

print (sum_point)
