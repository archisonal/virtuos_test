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
while student_name and len(student_name)>30:
    student_name = input("the length should be less than 30. Enter again: ")

college_name = input("Enter your college name: ")
while college_name and len(college_name)>50:
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
        return 'rejected'
    else:
        return 'selected'
        
def calc_place(total_marks):
    if(total_marks>=45):
        return 1
    elif(total_marks>=40):
        return 2
    elif(total_marks>=35):
        return 3
    else:
        return 0
    
def calc_percent(marks, t_marks):
    percent = marks*100/t_marks
    return percent

round1_per = calc_percent(round1, 10)
round2_per = calc_percent(round2, 10)
round3_per = calc_percent(round3, 10)
techround_per = calc_percent(tech_round, 20)

#updated logic
if round1_per >= 70 and round2_per >= 70 and round3_per >= 70 and techround_per >= 70:
    result = 'selected'
else:
    result = 'rejected'

        
# we will calculate result and rank and store them in the following variables respectively
rank = calc_place(total_marks)

#inserting into db
query = """INSERT INTO assessment (student_name, college_name, round1, round2, round3, tech_round, total_marks, result, place) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
cursor.execute(query, (student_name, college_name, round1, round2, round3, tech_round, total_marks, result, rank))
conn.commit()

#printing values
# query1 = """SELECT student_name, total_marks, result, place FROM assessment ORDER BY total_marks DESC"""
# cursor.execute(query1)
# rows = cursor.fetchall()
# print('Student name | total marks | result | rank')
# for row in rows:
#     print(row)

#printing values
# cursor.execute("SELECT * FROM assessment")
# rows = cursor.fetchall()
# print('Student name | College Name | Round1 marks | round2 marks | round3 marks | technical round marks | total marks | result | rank')
# for row in rows:
#     print(row)
    
# cursor.execute("DELETE FROM assessment")
# conn.commit()
# query = """SELECT student_name, college_name, total_marks, place FROM assessment ORDER BY place ASC"""
# cursor.execute(query)
# rows = cursor.fetchall()
# query1 = """SELECT student_name, college_name, total_marks, place FROM assessment WHERE result = %s"""
# query2 = """SELECT student_name, college_name, total_marks, place FROM assessment WHERE result = %s"""
# cursor.execute("SELECT student_name, college_name, total_marks, place FROM assessment WHERE result = 'selected'")
# # cursor.execute("SELECT student_name, college_name, total_marks, place FROM assessment WHERE result = %s", 'rejected')
# rows = cursor.fetchall()

# print("student_name, college_name, total_marks, place ")
# for row in rows:
#     print(row[0], row[1], row[2], row[3])

# cursor.execute("SELECT student_name, college_name, total_marks, place FROM assessment WHERE result = 'rejected'")

# rows = cursor.fetchall()

# print("student_name, college_name, total_marks, place ")
# for i in rows:
#     print(i[0], i[1], i[2], i[3])
    



cursor.execute("UPDATE assessment SET result = result")
# cursor.execute("SELECT student_name, college_name, total_marks, place FROM assessment WHERE result = 'rejected'")

# cursor.execute("SELECT * FROM assessment")
rows = cursor.fetchall()
# print("student_name, college_name, total_marks, place ")
for i in rows:
    print("\n",rows)
    
cursor.execute("SELECT * FROM assessment WHERE total_marks>35")
rows = cursor.fetchall()
for i in rows:
    print("\n",rows)