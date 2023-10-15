##
#! Python course from Skillup and Simplilearn
#* Project

import statistics as st
from time import sleep

#Log in first then do the other part of the program
print("Let's Log In")
LogInName = input("Username: ")
LogInPasw = input("Password: ")
    

if LogInName == 'Admin':
    if LogInPasw == 'Password123':
        studentGrades = {"Alex" : [92, 76, 88], "Sam" : [89, 92, 93]}

        print('\n     Welcome to Grade Central\n')

        print("   [1] - Enter Grades")
        print("   [2] - Remove Student")
        print("   [3] - Student Average Grades")
        print("   [4] - Exit\n")


        #! Don't know if i should store the names and grades in a file
        #! but to save the studentGrades into a file 
        #! we will have to use json.dump to conevert

        def StudentAdd():
            #add the name and grade to the dict
            studentName = input("Student Name: ")
            studentGrade = int(input("Grade: "))
            
            if studentName in studentGrades:
                studentGrades[studentName].append(studentGrade)
            else:
                studentGrades[studentName] = [studentGrade]
                
            print('Adding Grade...')
            print(studentGrades)
            
        def RemoveStudents():
            nameToRemove = input("What student to remove?: ")
            del studentGrades[nameToRemove]
            print("Removing Student...")
            print(studentGrades)
            
        def StudentAVGs():
            for student, grades in studentGrades.items():
                mean = st.mean(grades)
                print("The mean grade for", student, "is", mean)


        userChoice = int(input("What would you like to do today? (Enter a number): "))

        if userChoice == 1:
            StudentAdd()
        elif userChoice == 2:
            RemoveStudents()
        elif userChoice == 3:
            StudentAVGs()
        #! If the userChoice is above 3 then exit() so 4 will exit either way
        #* here we could also import sys so that we can sys.exit (sys -> system (OS))
        else:
            print('Exiting...')
            sleep(2) #pauses for x timea
            exit()
    else:
        print("Invalid Password, will detonate in 5 seconds!")
        sleep(5)
        exit()  
else:
    print("Invalid Username, will detonate in 5 seconds!")
    sleep(5)
    exit()