import sqlite3

# Connect to your database
conn = sqlite3.connect('resume_database.db')
cursor = conn.cursor()

# Ask for the full name to search
name_to_search = input("Enter the full name to search: ")

# Step 1: Find the user
cursor.execute("SELECT * FROM Users WHERE full_name = ?", (name_to_search,))
user = cursor.fetchone()

if user:
    user_id = user[0]  # Get the user's ID from Users table

    print("\n--- User Details ---")
    print(f"Full Name: {user[1]}")
    print(f"Phone Number: {user[2]}")
    print(f"Email: {user[3]}")

    # Step 2: Find Education details
    cursor.execute("SELECT institution, graduation_year, degree FROM Education WHERE user_id = ?", (user_id,))
    education = cursor.fetchone()
    if education:
        print("\n--- Education Details ---")
        print(f"Institution: {education[0]}")
        print(f"Graduation Year: {education[1]}")
        print(f"Degree: {education[2]}")

    # Step 3: Find Experience details
    cursor.execute("SELECT company_name, job_title, years_of_experience FROM Experience WHERE user_id = ?", (user_id,))
    experience = cursor.fetchone()
    if experience:
        print("\n--- Experience Details ---")
        print(f"Company Name: {experience[0]}")
        print(f"Job Title: {experience[1]}")
        print(f"Years of Experience: {experience[2]}")

    # Step 4: Find Skills
    cursor.execute("SELECT skills FROM Skills WHERE user_id = ?", (user_id,))
    skills = cursor.fetchone()
    if skills:
        print("\n--- Skills ---")
        print(f"Skills: {skills[0]}")

else:
    print("No user found with that name.")

# Close the connection
conn.close()
