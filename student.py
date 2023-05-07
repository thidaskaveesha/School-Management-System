from sqlalchemy import  Column, String, Integer
from extention import Base, session
import logging

#this will reduce extra content that providing by sqlalchemy so only error will raise 
logger = logging.getLogger()
logger.disabled = True
logging.getLogger('sqlalchemy.engine').addHandler(logging.NullHandler())
 
#inherit the database we are connected
class Student(Base) :
    #create the student table with fields 
    __tablename__ = "student"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(50))
    hometown = Column("hometown", String(50))

    #creating the constructor to create objects
    def __init__ (self,id,name,hometown):
        self.id = id 
        self.name = name
        self.hometown = hometown

    #using this method able to add objects to the student table in  database system
    def add(self):
        try:
            id = int(input("Enter Student number : "))
        except(ValueError):
            print("ID isn't a number !")       
        name = input("Enter student name : ")
        hometown = input("Enter student's hometown : ")
        student = Student(id, name, hometown)
        session.add(student)
        print("student added !")
        input("please enter a key to continue......")

    #using this method able to read that mean select all from the student table 
    def read(self):
        students = session.query(Student).all()
        print("-----AVAILABLE TEACHERS---------")
        for student in students:
            print("------------------------")
            print("Student ID:", student.id)
            print("Name:", student.name)
            print("Hometown:", student.hometown)
            print("------------------------")
        input("please enter a key to continue......")

    #using this method able to select students by thier id from student table 
    def readInfo(self):
        try : 
            id = int(input("Enter Student ID :"))
        except(ValueError):
            print("Entered a ID in a invalid format")
        student = session.query(Student).filter(Student.id == id).first()
        if student:
            print("-----YOU LOOKING FOR---------")
            print("------------------------")
            print("Student ID:", student.id)
            print("Name:", student.name)
            print("Hometown:", student.hometown)
            print("------------------------")
            input("please enter a key to continue.....")
        else:
            print("------------------------")
            print("Student not found with ID:", id)
            print("------------------------")
            input("please enter a key to continue.....")

    #using this method able to update field of students by thier id 
    def update(self):
        try : 
            id = int(input("Enter Student ID :"))
        except(ValueError):
            print("Entered a ID in a invalid format")
        student = session.query(Student).filter(Student.id == id).first()
        if student:
            print("------------------------")
            print("Current student information:")
            print("Student ID:", student.id)
            print("Name:", student.name)
            print("Hometown:", student.hometown)
            print("------------------------")
            new_name = input("Enter new name for the student: ")
            new_hometown = input("Enter new hometown for the student: ")
            student.name = new_name
            student.hometown = new_hometown
            session.commit()
            print("------------------------")
            print("Student information updated successfully.")
            print("------------------------")
            input("please enter a key to continue....")
        else:
            print("------------------------")
            print("Student not found with ID:", id)
            print("------------------------")
            input("please enter a key to continue....")
    
    #simply this method will help us to delete student record by thier id 
    def delete(self):
        try : 
            id = int(input("Enter Student ID :"))
        except(ValueError):
            print("Entered a ID in a invalid format")
        student = session.query(Student).filter(Student.id == id).first()
        if student:
            print("------------------------")
            print("Deleting the following student:")
            print("Student ID:", student.id)
            print("Name:", student.name)
            print("Hometown:", student.hometown)
            print("------------------------")
            choice = input("Are you sure you want to delete this student? y/n : ")
            if choice.lower() == "y":
                session.delete(student)
                session.commit()
                print("------------------------")
                print("Student deleted successfully.")
                print("------------------------")
                input("please enter a key to continue....")
            else:
                print("------------------------")
                print("Deletion canceled.")
                print("------------------------")
                input("please enter a key to continue....")
        else:
            print("------------------------")
            print("Student not found with ID:", id)
            print("------------------------")
            input("please enter a key to continue....")