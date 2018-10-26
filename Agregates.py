import pandas as pd
import json as j

#df = pd.DataFrame({'key': ['A', 'B', 'B', 'A', 'B', 'A']
#                   ,'data': [1,1,2,3,4,5,]
#                 ,'key2': ['B', 'B', 'B', 'A', 'B', 'B']}
# , columns=['key','key2', 'data'])
#print (df)
#print(df.groupby(['key2','key']).sum())


total_point_by_profile = pd.DataFrame(
                    {'profile_id': ['1', '2', '3', '4', '5', '6']
                   ,'total_point': [50,10,13,15,23,30]

                     }
                    , columns=['profile_id','total_point'])
total_point_by_matches = pd.DataFrame(
                    {'profile_id': ['1', '2', '3', '4', '5', '6',  '1', '2', '3', '4', '5', '6',   '1', '2', '3', '4', '5', '6'],
                'other_profile_id':['5', '6','1', '2', '3', '4',    '2', '3', '4', '5', '6','1',   '3', '4', '5', '6','1','2' ]
                ,'total_point_match':        [25,5,6,7,20,24,                40,9,10,4,15,10,                 10,8,11,5,15,18]}
                    , columns=['profile_id','other_profile_id', 'total_point_match'])
merge=total_point_by_matches.merge(total_point_by_profile, on='profile_id')

raw_data = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Eder', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Bonder', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
df_a = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])

raw_data = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Bonder', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['4', 'Black', 'Balwner', 'Brice', 'Btisan']}
df_b = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
join=df_b.merge(df_b, left_on=['last_name'],right_on=['subject_id'], how='inner')
raw_data = {
        'nombreb': ['camila', 'eder', 'valery', 'luz', 'sebastian','eder','camila'],
        'nombreb': ['eder', 'sebastian', 'carmen', 'katerine', 'chela','camila','luz'],
        'palabrb': ['NOV', 'Black', 'Balwner', 'Brice', 'Btisan','IO','test']}

df_b = pd.DataFrame(raw_data, columns = ['nombreb', 'nombreb', 'palabrab'])
raw_data = {
        'nombrea': ['camila', 'eder', 'valery', 'luz', 'sebastian','eder','camila'],
        'nombrea': ['eder', 'sebastian', 'carmen', 'katerine', 'chela','camila','luz'],
        'palabra': ['NOV', 'Black', 'Balwner', 'Brice', 'Btisan','IO','test']}

df_a = pd.DataFrame(raw_data, columns = ['nombrea', 'nombrea', 'palabraa'])

join = pd.concat([df_b,df_a],axis=1,sort=True)
#join=df_b.merge(df_b, left_on=['nombre2','nombre'],right_on=['nombre','nombre2'], how='inner')
print(join)


