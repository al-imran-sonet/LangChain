from pydantic import BaseModel,EmailStr

# Basic 
# class student(BaseModel):
#     name : str


# new_student= {'name':'imran'} # since we set the name as string , we cant input number as the name. It will show error.

# student=student(**new_student)
# print(student)



# Default value
# class student(BaseModel):
#     name : str='imrannn' # This is a default value . If you dont give any value  name it will set imrannn as by default  


# new_student= {} 

# student=student(**new_student)
# print(student)
# print(student.name)



# Optional field 
# from typing import Optional 
# class student(BaseModel):
#     name : str='al'
#     age: Optional[int]= None  # you can give optional field. If the value is present it will show that other wise it will show None or what ever you set 


# new_student= {'name':'imran','age':23} # 

# student=student(**new_student)
# print(student)



# # Type Coerce 
# from typing import Optional 
# class student(BaseModel):
#     name : str
#     age: Optional[int]= None 

# new_student= {'name':'imran','age':'23'} # For Optional field it will convert the type .

# student=student(**new_student)
# print(student)
# print(type(student.age))  # it will convert the age into integer



# # Email validation 

# from typing import Optional
# class student(BaseModel):
#     name : str
#     age: Optional[int]= None 
#     email: EmailStr    # email validation  .

# new_student= {'name':'imran','age':'23','email':'abcde@gmail.com'} 

# student=student(**new_student)
# print(student)
# print(type(student.age)) 



# Field function 

from pydantic import BaseModel, EmailStr , Field 
from typing import Optional 

class student(BaseModel):
    name : str
    age: Optional[int]= None 
    email: EmailStr    # email validation  .
    cgpa: float =Field(gt=0, le=4, default=3,description='A decimal value reperesenting the cgpa of the student ') 
    Phone_number:str= Field(default=None,description='Phone number must be in string format')
 # Field is used for condition set for particular variable field 
 # (default values, constarints,description etc) 
 # discription is used for documenting perpose only 
new_student= {'name':'imran','age':'23','email':'abcde@gmail.com','cgpa':3.7,'Phone_number':'01832792411'}

student_obj=student(**new_student)
print(student_obj)
print(type(student_obj)) 

student_dict= dict(student_obj)   # converting a pydantic object into dictionary 
print(student_dict)   

student_json= student_obj.model_dump_json() 
print(student_json)