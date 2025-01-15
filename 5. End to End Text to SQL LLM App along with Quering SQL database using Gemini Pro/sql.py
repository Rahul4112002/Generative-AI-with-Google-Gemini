import sqlite3

connection = sqlite3.connect('student.db')

cursor = connection.cursor()

table_info = '''
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
'''

cursor.execute(table_info)

cursor.execute('''INSERT INTO STUDENT VALUES ('Rahul', 'Data Science', 'A', 90)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Krishna', 'IT', 'B', 50)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('OM', 'Devops', 'C', 60)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikash', 'Data Science', 'C', 80)''') 


print("The inserted records")
data = cursor.execute('''Select * From STUDENT ''')

for row in data:
    print(row)
    
connection.commit()
connection.close()