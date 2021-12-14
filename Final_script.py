###import and merge the excel file using pandas
import glob
import pandas as pd
from pandas import ExcelFile
path = '/Users/lanjunpeng/Downloads/LING555_project'
###open excel files
f1 = pd.read_excel(path+"/HockeyZonePlus-Salary-Database-1994-2017-Indiana-University.xlsx")
f2 = pd.read_excel(path+"/players_performance_regular.xlsx")
###transpose the excel to better match the data
df1 = (pd.melt(f1,id_vars=['First','Last'],value_name='year_'))
###split the year column name and drop extra columns
df1[['tmp','Season']]=df1.variable.str.split('_',expand=True)
df1 = df1.drop(['variable','tmp'],axis=1).sort_values(['Last','First'])
###rename the column
df1 = df1.rename(columns={"year_":"salary"})
###save and export to excel for records
df1.to_excel(path+"/df1.xlsx",index=False)

###using pandas to merge
f3 = pd.merge(df1,f2,how='left')
###sort the excel file alphabetically by lastname firstname and season
f4 = f3.sort_values(["Last","First","Season"])
###save the merged excel file
f4.to_excel(path+"/new.xlsx",index=False)

###use transcriber to fix name issues
f5 = f4
#form a dictionary
map = {}
map['Alexandre']='Alexander'
map['Nikolay']='Nikolai'
map['Niklas']='Niclas'
map['Viktor']='Victor'
map['Zachary']='Zach'
map['Cameron']='Cam'
map['Ruslam']='Ruslan'
map['Louie']='Louis'
map['Patrik']='Patrick'
map['Christopher']='Chris'
map['Richard']='Rich'
map['Andrei']='Andrey'
###add row to the existing row
word=f5['First']
for k in map:
	word=word.replace(k,map[k])
f5['Revised']=word
print(f5)


###replace some common name issues using panda dataframe value replace(as an alternative to transcriber)
#f5 = f4
#f5['First']=f4['First'].replace(['Alexandre','Nikolay','Niklas','Viktor','Zachary','Cameron','Ruslam','Louie','Patrik','Christopher','Richard','Andrei'],['Alexander','Nikolai','Nicklas','Victor','Zach','Cam','Ruslan','Louis','Patrick','Chris','Rich','Andrey'])

###drop rows which has NaN in salary column
mod_f5=f5.dropna(how='any',subset=['salary'])
print(mod_f5)
