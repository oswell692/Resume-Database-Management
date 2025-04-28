import sqlite3
conn = sqlite3.connect('resume_database.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

print("----- Resume Summary Report -----\n")

for user in users:
    user_id, full_name, phone, email = user
    print(f"Name: {full_name}")
    print(f"Phone: {phone}")
    print(f"Email: {email}")
    

    cursor.execute('SELECT degree, institution, graduation_year FROM Education WHERE user_id = ?', (user_id,))
    education = cursor.fetchone()
    if education:
        degree, institution, graduation_year = education
        print(f"Education: {degree} from {institution} (Graduated: {graduation_year})")
    else:
        print("Education: Not Provided")

    cursor.execute('SELECT company_name, job_title, years_of_experience FROM Experience WHERE user_id = ?', (user_id,))
    experience = cursor.fetchone()
    if experience:
        company_name, job_title, years_of_experience = experience
        print(f"Experience: {company_name} at {job_title} for {years_of_experience} years")
    else:
        print("Experience: Not Provided")

    print("\n-------------------------\n")

conn.close()
