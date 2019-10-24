import requests
import json
from pprint import pprint 
import os.path
from os import path

def getCourses():
    if os.path.exists("courses.json"):
        myFile=open("courses.json",'r')
        readFile=myFile.read()
        dictionaryData=json.loads(readFile)
        coursesData=dictionaryData["availableCourses"]
        count=0
        coursesIdList=[]
        for index in coursesData:
            print count,index["name"],index["id"]
            coursesIdList.append(index["id"]) 
            count=count+1
        return coursesIdList

    else:
        url="http://saral.navgurukul.org/api/courses"
        response=requests.get(url)
        dictData=response.text
        myFile=open("courses.json",'w')
        writeFile=myFile.write(dictData)
        stringData=json.dumps(writeFile)
        myFile.close()
coursesIdList=getCourses()
# print coursesIdList

user_input=input("enter your Id:")
user_Id=coursesIdList[user_input]
print user_Id

def exersice_fun(api2): 
	filename="file/excersice"+str(user_Id)+".json"
	if os.path.exists(filename):
		course_json_file=open(filename,"r")
		data1=course_json_file.read()
		dict_data1=json.loads(data1)
		inside_data=dict_data1["data"]
		return inside_data
	else:
		exersice_data=requests.get(api2)
		excersiceData=exersice_data.json()
		json_file1=open(filename,"w")
		string_data=json.dumps(excersiceData)
		json_file1.write(string_data)
		json_file1.close()
		return filename
url2="http://saral.navgurukul.org/api/courses"+"/"+str(user_Id) + "/" +"exercises"
inside_data1 = exersice_fun(url2)

def getExercises(): 
    filename="file/excersice"+str(user_Id)+".json"  
    if os.path.exists(filename):
        myFile=open(filename,'r')
        readFile=myFile.read()
        dictionaryData=json.loads(readFile)
        exercisesData=dictionaryData["data"]
        count=0
        slug_list=[]
        exercisesIdData=[]
        for index in exercisesData:
            print count,index["name"],index["id"] ,index["slug"]
            exercisesIdData.append(index["id"]) 
            childExercisesdata=index["childExercises"]
            count1 = 0   
            for index1 in childExercisesdata:
                print "\t","\t",count1, index1["name"],index1["id"]  
                count1=count1+1
            count=count+1          
        return exercisesIdData    
    else:             
        url2= "http://saral.navgurukul.org/api/courses/"+str(user_Id)+"/exercises"
        response=requests.get(url2)
        dictData=response.text
        myFile=open(filename,'w')
        writeFile=myFile.write(dictData)
        stringData=json.dumps(writeFile)
        print ("**************************")
        return filename
        myFile.close()
exercisesIdData=getExercises()


slug_list=[]
def getSlug(user_input):
    for index in inside_data1:
        count=0
        parent_slug=exercisesIdData[user_input]
        if parent_slug==index["id"]:
            print count,index["name"]
            slug_list.append(index["slug"]) 
            childExercisesdata=index["childExercises"]
            count1=count+1  
            for index1 in childExercisesdata:
                print count1, index1["name"]
                slug_list.append(index1["slug"])  
                count1=count1+1  
        count=count+1        
    return slug_list   
slug_input=input("Enter your slug number:")
slug_list=getSlug(slug_input)


user_input1=input("enter your Exercise Id:")
Exercises_Id=slug_list[user_input1]

exersiceId=exercisesIdData[user_input1]


def getContent():
    slug_file="slug/slugExercise"+str(exersiceId)+".json"
    if os.path.exists(slug_file):
        course_json_file=open(slug_file,'r')
        data1=course_json_file.read()
        dict_data1=json.loads(data1)
        contentData=dict_data1["content"]
        print contentData
    else:
        url3="http://saral.navgurukul.org/api/courses/"+str(user_Id)+"/"+"exercise"+"/"+"getBySlug?slug="+str(Exercises_Id)
        response=requests.get(url3)
        dictData=response.text

        myFile=open(slug_file,'w')
        writeFile=myFile.write(dictData)
        stringData=json.dumps(writeFile)
        print ("*********************")
        myFile.close()
getContent()

