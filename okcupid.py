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
points = []

for profile in profiles["profiles"]: #all profiles
    ##if(profile["id"]==0 or profile["id"]==1):
    for question in profile["answers"]:#all question by profile
        for other_profile in profiles["profiles"]:#all question others profiles
            if profile["id"] != other_profile["id"]:#exclude same profiles
                for index ,question_other_profile in enumerate(other_profile["answers"]):#all question of other profile
                    if question["questionId"] == question_other_profile["questionId"] and profile["id"] != other_profile["id"] :
                        #add to matriz the question matches
                        question_matches.append([profile["id"],other_profile["id"],question["questionId"],question["importance"],(question_other_profile["answer"]in question["acceptableAnswers"])])

    print("n\id:",profile ["id"])
#total point and real point
#for match in question_matches:
    #print("n\match:",match)
    #points.append([match[0],match[1],match[0]])
    ##points.append([match[0]])
#array = np.array([[1, 0, -1], [3, 4, 1]])
#salida = np.sum(array, axis=1)
#print(salida)
print("fin questions matches")
def sum(profile, other_profile,array):
    sum_posibles=0
    sum_real=0
    for data in array:
        if(data[0]==profile and data[1]==other_profile):
            sum_posibles+=VALUES_POINT[data[3]]
        if(data[0]==profile and data[1]==other_profile and data[4]):
            sum_real+=VALUES_POINT[data[3]]
    return([profile, other_profile,sum_posibles,sum_real])
#sum=sum(0,2,question_matches)
#print((sum[1]/sum[0]))
#print(len(question_matches))
results=[]
for profile in profiles["profiles"]: #all profiles
    for other_profile in profiles["profiles"]: #all profiles
        if(profile["id"]!=other_profile["id"]):
            results.append([sum(profile["id"],other_profile["id"],question_matches)])

print("result",results)

