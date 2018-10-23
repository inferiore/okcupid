import json
import numpy as np

#read file
profiles = json.loads(open('input.json').read())

print("cantidad de profiles")
#print(len(leer["profiles"][0]))
#total points  by question macthed for each user
total_importance=0
#profile,other_profile,question_id,importance,acceptableAnswers
matches = []
points = []

for profile in profiles["profiles"]: #all profiles
    if profile["id"] == 0:
        for question in profile["answers"]:#all question by profile
            for other_profile in profiles["profiles"]:#all question others profiles
                for index ,question_other_profile in enumerate(other_profile["answers"]):#all question of other profile
                    if question["questionId"] == question_other_profile["questionId"] and profile["id"] != other_profile["id"] :
                        #if both responce the same question calculated all points posibles
                        matches.append([profile["id"],other_profile["id"],question["questionId"],question["importance"],question["acceptableAnswers"]])
                #print(total_importance)
                #profile[other_profile["id"]]=total_importance
                #print (other_profile["id"])


        #print("n\id:",profile ["id"],profile)
#total point and real point
#for match in matches:
#    print("n\match:",match)
#    points.append([match[0],])

#array = np.array([[1, 0, -1], [3, 4, 1]])
#salida = np.sum(array, axis=1)
#print(salida)



