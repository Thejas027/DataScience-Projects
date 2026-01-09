import numpy as np
import pandas as pd

num_students = 200
subjects = ["maths" , "reading",'writing']
random_seed = 42

np.random.seed(random_seed)

def generate_student(student_id):
    
    base_ability = np.random.normal(loc=70,scale=10)
    
    scores={}
    
    for subject in subjects:
        nosie = np.random.normal(loc=0,scale=10)
        score = base_ability + nosie
        
        score = max(0,min(100,score))
        
        scores[subject] = round(score,2)
        
    scores["student_id"] = student_id
    return scores

students = []

for i in range (num_students):
    student = generate_student(i+1)
    students.append(student)
    

df = pd.DataFrame(students)


df.to_csv("../data/students.csv" , index=False)

print("Student generated sucessfully")
print(df.head());
        