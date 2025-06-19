import mysql.connector
import csv

#establlishing connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Qwerty@321',
    database='DB1'
)

#creating an object
cursor = conn.cursor()

#taking inputs
student_name = input("Enter your name: ")
while len(student_name)>30:
    student_name = input("the length should be less than 30. Enter again: ")

college_name = input("Enter your college name: ")
while len(college_name)>50:
    college_name = input("the length should be less than 50. Enter again: ")
    
round1 = float(input("enter round 1 marks: "))
while round1<0 or round1>10:
    round1 = float(input("The value should be between 0 and 10. enter round 1 marks again: "))
    
round2 = float(input("enter round 2 marks: "))
while round2<0 or round2>10:
    round2 = float(input("The value should be between 0 and 10. enter round 2 marks again: "))

round3 = float(input("enter round 3 marks: "))
while round3<0 or round3>10:
    round3 = float(input("The value should be between 0 and 10. enter round 3 marks again: "))
    
tech_round = float(input("enter tech round marks: "))
while tech_round<0 or tech_round>20:
    tech_round = float(input("The value should be between 0 and 10. enter tech round marks again: "))
    
total_marks = round1+round2+round3+tech_round
print(total_marks)

def calc_res(total_marks):
    if(total_marks<35):
        print('rejected')
    else:
        print('selected')
        
def calc_place(total_marks):
    if(total_marks>=45):
        print('1st')
    elif(total_marks>=40):
        print('2nd')
    elif(total_marks>=35):
        print('3rd')
    else:
        print('sorry you are not selected')
        
# we will calculate result and rank and store them in the following variables respectively
result = calc_res(total_marks)
rank = calc_place(total_marks)

#inserting into db
query = """INSERT INTO assessment (student_name, college_name, round1, round2, round3, tech_round, total_marks, result, place) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
cursor.execute(query, (student_name, college_name, round1, round2, round3, tech_round, total_marks, result, rank))
conn.commit()

#printing values
cursor.execute("SELECT * FROM assessment")
rows = cursor.fetchall()
print('Student name | College Name | Round1 marks | round2 marks | round3 marks | technical round marks | total marks | result | rank')
for row in rows:
    print(row)
    
#then to Display the list of all the candidate sorted with their ranking and results we will execute the following query
# query1 = """SELECT student_name, result, place FROM assessment GROUP BY results"""
# cursor.execute(query)

# query2 = """SELECT student_name, result, place FROM assessment GROUP BY place"""
# cursor.execute(query)
