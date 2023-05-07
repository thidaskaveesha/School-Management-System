from sqlalchemy import  Column, String, Integer
from extention import Base,session
import logging

#this will reduce extra content that providing by sqlalchemy so only error will raise 
logger = logging.getLogger()
logger.disabled = True
logging.getLogger('sqlalchemy.engine').addHandler(logging.NullHandler())

class Teacher(Base) :
    __tablename__ = "teacher"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(50))
    hometown = Column("hometown", String(50))

    def __init__ (self,id,name,hometown):
        self.id = id 
        self.name = name
        self.hometown = hometown


    def add(self):
        try:
            id = int(input("Enter Teacher number : "))
        except(ValueError):
            print("you have entered non numeric !") 
        name = input("Enter teacher's name : ")
        hometown = input("Enter teacher's hometown : ")
        teacher = Teacher(id , name, hometown)
        session.add(teacher)
        print("student added !")
        input("please enter a key to continue.....")

    def read(self):
        teachers = session.query(Teacher).all()
        print("-----AVAILABLE TEACHERS---------")
        for teacher in teachers:
            print("------------------------")
            print("Teacher ID:", teacher.id)
            print("Name:", teacher.name)
            print("Hometown:", teacher.hometown)
            print("------------------------")
        input("please enter a key to continue....")
    
    def readInfo(self):
        try : 
            id = int(input("Enter Teacher ID :"))
        except(ValueError):
            print("Entered a ID in a invalid format")
        teacher = session.query(Teacher).filter(Teacher.id == id).first()
        if teacher:
            print("-----YOU LOOKING FOR---------")
            print("------------------------")
            print("Teacher ID:", teacher.id)
            print("Name:", teacher.name)
            print("Hometown:", teacher.hometown)
            print("------------------------")
            input("please enter a key to continue.....")
            
        else:
            print("------------------------")
            print("Teacher not found with ID:", id)
            print("------------------------")
            input("please enter a key to continue.....")

    def update(self):
        try : 
            id = int(input("Enter Teacher ID :"))
        except(ValueError):
            print("Entered a ID in a invalid format")
        teacher = session.query(Teacher).filter(Teacher.id == id).first()
        if teacher:
            print("------------------------")
            print("Current teacher information:")
            print("Teacher ID:", teacher.id)
            print("Name:", teacher.name)
            print("Hometown:", teacher.hometown)
            print("------------------------")
            new_name = input("Enter new name for the teacher: ")
            new_hometown = input("Enter new hometown for the teacher: ")
            teacher.name = new_name
            teacher.hometown = new_hometown
            session.commit()
            print("------------------------")
            print("Teacher information updated successfully.")
            print("------------------------")
            input("please enter a key to continue....")
        else:
            print("------------------------")
            print("Teacher not found with ID:", id)
            print("------------------------")
            input("please enter a key to continue....")
    
    def delete(self):
        try : 
            id = int(input("Enter Teacher ID :"))
        except(ValueError):
            print("Entered a ID in a invalid format")
        teacher = session.query(Teacher).filter(Teacher.id == id).first()
        if teacher:
            print("------------------------")
            print("Deleting the following teacher:")
            print("Teacher ID:", teacher.id)
            print("Name:", teacher.name)
            print("Hometown:", teacher.hometown)
            print("------------------------")
            choice = input("Are you sure you want to delete this teacher? y/n : ")
            if choice.lower() == "y":
                session.delete(teacher)
                session.commit()
                print("------------------------")
                print("Teacher deleted successfully.")
                print("------------------------")
                input("please enter a key to continue....")

            else:
                print("------------------------")
                print("Deletion canceled.")
                print("------------------------")
                input("please enter a key to continue....")
        else:
            print("------------------------")
            print("Teacher not found with ID:", id)
            print("------------------------")
            input("please enter a key to continue....")