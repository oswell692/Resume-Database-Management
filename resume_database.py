import sqlite3

def setup_database():
    conn = sqlite3.connect('resume_database.db')
    cursor = conn.cursor()
    cursor.execute('''  
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        phone_number TEXT,
        email TEXT
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Education(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        institution TEXT,
        graduation_year TEXT,
        degree TEXT,
        FOREIGN KEY(user_id) REFERENCES Users(id)
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Experience(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        company_name TEXT,
        job_title TEXT,
        years_of_experience TEXT,
        FOREIGN KEY(user_id) REFERENCES Users(id)
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Skills(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        skills TEXT,
        FOREIGN KEY(user_id) REFERENCES Users(id)
    )
    ''')
    conn.commit()
    return conn, cursor

# Setup
conn, cursor = setup_database()

# Data entry
print("--- ENTER RESUME DETAILS----")
full_name = input("Enter your Full Name: ")
phone_number = input("Enter your Phone Number: ")
email = input("Enter Your Email: ")

cursor.execute('INSERT INTO Users(full_name, phone_number, email) VALUES (?, ?, ?)', (full_name, phone_number, email))
user_id = cursor.lastrowid

institution = input("Enter the Institution: ")
graduation_year = input("Enter your Graduation Year: ")
degree = input("Enter your Degree: ")

cursor.execute('INSERT INTO Education(user_id, institution, graduation_year, degree) VALUES (?, ?, ?, ?)', (user_id, institution, graduation_year, degree))

company_name = input("Enter the Company Name: ")
job_title = input("Enter your Job Title: ")
year_of_experience = input("Enter Years of Experience: ")

cursor.execute('INSERT INTO Experience(user_id, company_name, job_title, years_of_experience) VALUES (?, ?, ?, ?)', (user_id, company_name, job_title, year_of_experience))

skills = input("Enter Your Skills: ")
cursor.execute('INSERT INTO Skills(user_id, skills) VALUES (?, ?)', (user_id, skills))

conn.commit()
conn.close()

print("\nResume details saved successfully!")
