#importing neccessary classes to use
from teacher import Teacher
from student import Student
from extention import Base, engine
import logging

#this will reduce extra content that providing by sqlalchemy so only error will raise 
logger = logging.getLogger()
logger.disabled = True
logging.getLogger('sqlalchemy.engine').addHandler(logging.NullHandler())

#this function is the main menu where we give options to users to navigate through our system 
def mainmenu():
    while True:
        #display a main menu
        print("----Welcome to the School Management System----")
        print("\n----Main Menu----\n")
        print("1. Create table (please use this if this wasn't done before)")
        print("2. Manage Students")
        print("3. Manage Teachers")
        print("4. EXIT\n")
        try:
            #get a menu number from a user
            mainchoice = int(input("Please Enter your choice : "))
        except(ValueError):
            print("You have entered invalid input format !")

        if mainchoice == 1 :
            #create tables
            Base.metadata.create_all(bind=engine)
            input("please enter a key to continue...")
        elif mainchoice == 2 or mainchoice == 3 :
            #Transfer into a submenu
            submenu(mainchoice)
        elif mainchoice == 4 : 
            #exit programme
            print("Thank For using this solution !")
            quit()
        else :
            #if the user entered a numeric value which is not a menu number
            print("You have entered INVALID input !")
            print("Press any key to continue....")

#this function is the sub menu where we give options to users to navigate through our system 
def submenu(mainchoice):
    if mainchoice == 2 :
        role_name = 'Student'
        method_class = Student(None, None, None)
    elif mainchoice == 3 :
        role_name = 'Teacher'
        method_class = Teacher(None, None, None)
    
    while True:
        print("\n----Sub Menu----\n")
        print("1-Add",role_name)
        print("2-Read", role_name)
        print("3-Read" ,role_name, "by ID")
        print("4-Update", role_name)
        print("5-Remove", role_name)
        print("7-Back to Main menu")
        print("8-Quit") 

        try : 
            subchoice = int(input("Please Enter Your Choice : "))
        except(ValueError):
            print("Entered an Invalid input format")

        if subchoice == 1 :
            method_class.add()
        elif subchoice == 2 :
            method_class.read()
        elif subchoice == 3 :
            method_class.readInfo()
        elif subchoice == 4 :
            method_class.update()
        elif subchoice == 5 :
            method_class.delete()
        elif subchoice == 7 :
            mainmenu()
            break
        elif subchoice == 8 :
            print("Thank for using this solution !")
            quit()
mainmenu()