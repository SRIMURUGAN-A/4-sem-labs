#Working with paandas
import pandas as pd 
data = {'name':['ram','babu','sri','roger'],
        'age':['34','35','34','43'],
        'dept':['ai','ai','ai','ai'],
        'city' :['tuty','tuty','tuty','tuty']}
datas =pd.DataFrame(data)
print(datas)
print()
print (datas[['name', 'age']])


datas['sala'] = ['30k','50k','40k','30k']

print(datas)