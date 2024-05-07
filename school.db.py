import sqlite3
from sqlite3 import Error

# Opretter forbindelse til en SQLite-database
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# Udfører en SQL-forespørgsel, der ikke returnerer resultater
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# Udfører en SQL-forespørgsel, der returnerer resultater.
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

# Opret SQL-forespørgsel for at oprette 'Students' tabel
create_students_table = """
    CREATE TABLE IF NOT EXISTS Students (
      student_id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      major TEXT
    );
"""

# Opret SQL-forespørgsel for at oprette 'Courses' tabel
create_courses_table = """
    CREATE TABLE IF NOT EXISTS Courses (
      course_id INTEGER PRIMARY KEY AUTOINCREMENT,
      course_name TEXT NOT NULL,
      instructor TEXT
    );
"""
# inserts Students in database
create_students = """
INSERT INTO
  Students (name, major)
VALUES
  ('James', 'Kunstig intelligens'),
  ('Leila', 'Psykologi'),
  ('Brigitte', 'Biologi'),
  ('Mike', 'Lære'),
  ('Elizabeth', 'Astronaut');
"""

# inserts Courses in database
create_courses = """
INSERT INTO
  Courses (Course_name, instructor)
VALUES
  ('Ai og Data', 'Jesper'),
  ('DUAS', 'Andreas'),
  ('Math', 'Morten'),
  ('Intro to AI', 'Lasse'),
  ('PBL', 'Sofie');
"""

# Opret SQL-forespørgsel for at oprette 'Enrollments' tabel
create_enrollments_table = """
    CREATE TABLE IF NOT EXISTS Enrollments (
      enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
      student_id INTEGER NOT NULL,
      course_id INTEGER NOT NULL,
      FOREIGN KEY (student_id) REFERENCES Students (student_id),
      FOREIGN KEY (course_id) REFERENCES Courses (course_id)
    );
"""
# indsæt Enrollments i database
create_enrollments = """
INSERT INTO
  Enrollments (student_id, course_id)
VALUES
  (1, 1),
  (2, 3),
  (3, 1),
  (4, 4),
  (5, 5);
"""

# SQL-forespørgsel for at vælge alle kurser for en specific studerende
select_courses_for_student_query = """
SELECT Courses.course_name
FROM Courses
INNER JOIN Enrollments ON Courses.course_id = Enrollments.course_id
INNER JOIN Students ON Enrollments.student_id = Students.student_id
WHERE Students.name = 'James';
"""


# SQL-forespørgsel for at vælge alle studerende der er tilmeldt et specifikt kursus
select_students_for_course_query = """
SELECT Students.name
FROM Students
INNER JOIN Enrollments ON Students.student_id = Enrollments.student_id
INNER JOIN Courses ON Enrollments.course_id = Courses.course_id
WHERE Courses.course_name = 'Math';
"""

if __name__ == "__main__":
    # Opret forbindelse til databasen
    connection = create_connection("school.db")
    
    
    # Opret 'Students' tabel
    execute_query(connection, create_students_table)
    
    # Opret 'Courses' tabel
    execute_query(connection, create_courses_table)

    # Opret 'enrollment' tabel
    execute_query(connection, create_enrollments_table)


    # Indsæt students i databasen
    execute_query(connection, create_students) 

    # Indsæt courses i databasen
    execute_query(connection, create_courses) 

    # Indsæt tilmeldinger i databasen
    execute_query(connection, create_enrollments)


    # Udfør forespørgslen for at vælge kurser for en specifik studerende
    courses_for_student = execute_read_query(connection, select_courses_for_student_query)
    # Udskriv resultaterne
    for course in courses_for_student:
        print(course)
    
    # Udfør forespørgslen for at vælge students tilmeldt et specifik kursus
    student_for_course = execute_read_query(connection, select_students_for_course_query)
    # Udskriv resultaterne
    for student in student_for_course:
        print(student)