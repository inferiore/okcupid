import json

#read file
profiles = json.loads(open('input.json').read())

print("cantidad de profiles")
#print(len(leer["profiles"][0]))
#total points  by question macthed for each user
total_importance=0
for profile in profiles["profiles"]: #all profiles
    if(profile ["id"]==0):
        for question in profile["answers"]:#all question by profile
            for other_profile in profiles["profiles"]:#all question others profiles
                aDict = {}
                for index ,question_other_profile in enumerate(other_profile["answers"]):#all question of other profile
                    if(question["questionId"]==question_other_profile["questionId"] and profile["id"]==other_profile["id"] ):
                          #if both responce the same question calculated all points posibles
                        aDict[question["importance"]]=(question["importance"])
                print(aDict)
                #print(total_importance)
                #profile[other_profile["id"]]=total_importance
                #print (other_profile["id"])


        print("n\id:",profile ["id"],profile)

list = [1,2]
list2 = [1,2]

def sumar(list):
    list_sum = 0
    for x in list:
        list_sum += x
    return list_sum

