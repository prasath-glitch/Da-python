                                # Task 1 : Movie Ticket Eligibility 


# name=input("enter name : ")
# age=(int(input("enter age :")))
# print(f"hello  {name}")
# if( age < 13):
#     print("  ticket Type: child ticket  ")
# elif(age >= 13 and age < 50 ):
#   print ("ticket Type : adult ticket")  

# elif(age >= 60):
#   print("ticket Type :senior citizen ticket")

 
#                          # Task 2: Temperature Checker

# temp=int(input("enter the num :"))

# if( temp < 20):
#        print(" Weather: very cold bro ")
# elif ( 20<= temp <=30 ):
#        print(" Weather: pleasant "
             
#              )
# elif(temp > 30 ):
#        print(" Weather: hot ")


                            #   Task 3: Employee Bonus Calculator 

 
name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))
experience = int(input("Enter Years of Experience: "))

if salary >= 50000 and experience >= 5:
    bonus = salary * 0.20
elif salary >= 30000 and experience >= 3:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

final_salary = salary + bonus

print("Employee Name:", name)
print("Bonus Amount:", bonus)
print("Final Salary:", final_salary)

percentage=int(input(" enter the pes :"))
exam_mark= int(input("enter the mark :"))

if(percentage >= 70 and  exam_mark >= 80):
    print("admission conform")
elif(percentage >= 60 and exam_mark >= 60):
    print("waiting list bro")
else:
    print( "other wise rejected bro")





    

                     

            

 































































