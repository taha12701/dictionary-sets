my_dict={'name' : 'Taha',
'roll#' : 44,
'subjects': ['Python', 'C', 'C++','Dictionary','Sets'],
'ispassed' : True,
'city' : 'Lahore'}
# print(type(my_dict))
# print(my_dict['roll#'])
# print(my_dict['city'])

#we can assign  new value

my_dict['name']="Babar"
# print(my_dict)


# null_dict={}
# null_dict['name']='Taha'
# print(null_dict)


#nested dictionary

nes_dict={
  'name':'Taha',
  'subjects':{
    'chemistry': 98,
    'physics' : 100,
    'mathematics': 95
  }
}

# print(ses_dict['subjects']['chemistry'])   #nested dict
# print(len(nes_dict.keys()))  #length
# print(list(nes_dict.keys()))

# print(list(nes_dict.values()))
# pairs=list(nes_dict.items())   
# print(pairs[1])

# print(nes_dict.get('name2'))
# print(nes_dict['name2'])

# new_dict={'name':'Babar', 'age':'29'}
# nes_dict.update(new_dict)
# print(nes_dict)

# set_1={1,2,3,5,7,4}
# set_1.pop()
# print(type(set_1))

# emp_set=set()
# emp_set.add("Taha")

# set1={1,2,3,4,5}
# set2={4,2,3,7,9,10}
# set_3=set1.union(set2)
# print(set_3)

# my_dict={
#   'subjects':['Chemistry','Physics']
# }

# set_1={"python", "c++" , "java","Javascript","python","ruby on rails", "java", "c++", "reactjs", "python"}
# print(len(set_1))

# user_subject1=input("Enter subject name : ")
# user_subject2=input("Enter subject name : ")
# user_subject3=input("Enter subject name : ")

# user_value1=input("Enter marks  : ")
# user_value2=input("Enter marks  : ")
# user_value3=input("Enter marks  : ")


# n=3
# i=0
# emp_dict={}
# while(i<=n):
#   user_subject=input("Enter subject name : ")
#   user_value=input("Enter marks  : ")
#   emp_dict[f'{user_subject}']=user_value
#   i +=1
# print(emp_dict)




# emp_dict[f'{user_subject2}']=user_value2
# emp_dict[f'{user_subject3}']=user_value3

# print(emp_dict)

# set_1={9,"9.0"}
# print(set_1)

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
# print(sampleDict.keys())
# print(sampleDict['class']['student']['marks']['history'])

