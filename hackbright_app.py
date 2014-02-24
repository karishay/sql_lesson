import sqlite3

CONN = None
DB = None

###functions here###

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

def make_new_student(first_name, last_name, github):
    query = """INSERT INTO Students VALUES (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print "Sucecessfully added student: %s %s" % (first_name, last_name)

#find the projects by title
def query_project_title(title):
    #first, find out what you want to query
    query = """SELECT title, description FROM Projects WHERE title = ?"""
    DB.execute(query (title,))
    CONN.commit()
    row = DB.fetchone()
    print "Here's a description of the book %s: \n \"%s\" " % (row[0], row[1])

#add a project
def add_project(title, max_grade):
    #what are you looking for and what do you want to return?
    query = """INSERT INTO Projects (title, max_grade) VALUES (?, ?); """
    DB.execute(query(title, max_grade))
    CONN.commit()
    print "New project %s has been added to the database." % title

#Query for a student's grade given a project
def students_project_grade(first_name, title):
    query = """SELECT first_name, title, grade FROM ReportCardView WHERE first_name= ?; """
    DB.execute(query(first_name, title))
    CONN.commit()
    row = DB.fetchone()
    print "Here is %s \'s grade on the %s assignment: %s" % ([row[0], row[1], row[2]])

#give a grade to a student
def new_grade(student_gitub, project_title, grade):
    #what are your input arguments?
    #what do you want to return?
    query = """INSERT INTO Grades (student_gitub, project_title, grade) VALUES (?, ?, ?); """
    DB.execute(query(arguments))
    CONN.commit()
    print "You have added %s \'s new grade for the %s project as %s" % (row[0], row[1], row[2])

#show all the grades for a student
def all_students_grades(first_name):
    #what are your input arguments?
    #what do you want to return?
    query = """SELECT * FROM ReportCardView WHERE first_name= ?;"""
    DB.execute(query(first_name,))
    CONN.commit()

    print "Student %s \'s grades: %s" % (first_name #stuff??)
    pass




def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "project":
            add_project(*args)
        elif command == "project_title":
            query_project_title(*args)
        #elif command == ""
        #    pass

    CONN.close()





if __name__ == "__main__":
    main()
