# Made for the solde purpose of GCI 2019
import random
def home():
    global a
    print("Welcome to the feedback form!")
    a=input("Please enter your name:")
    z=random.choice(lm)
    questions(z)
def questions(mil):
    if mil==l2:
        for i in l2:
            print(i)
            print(" 1. 9-10(Excellent) \n 2. 5-8(Good) \n 3. 2-4(Bad) \n 4. 0-2(Poor)  \n 5. Exit")
            l=int(input("Enter your choice(choose one option only:"))
            if l>5:
                print("Please choose from the given options only!")
                return home()
            if l==5:
                print("Thank you",a,"for filling in the feedback!")
                return None
            if l==1 or 2 or 3 or 4:
                continue
        print("Thank you",a,"for filling in the feedback!")
    if mil==l3:
        for i in l3:
            print(i)
            print(" 1. Yes \n 2. No \n 3. Maybe \n 4. Exit")
            l=int(input("Enter your choice(choose one option only:"))
            if l>4:
               print("Please choose from the given options only!")
               return home()
            if l==4:
                print("Thank you",a,"for filling in the feedback!")
                return None
            if l==1 or 2 or 3 :
                continue
    if mil==l1:
        for i in l1:
            print(i)
            print(" 1. Yes \n 2. No \n 3. Maybe \n 4. Exit")
            l=int(input("Enter your choice(choose one option only:"))
            if l>4:
               print("Please choose from the given options only!")
               return home()
            if l==4:
                print("Thank you",a,"for filling in the feedback!")
                return None
            if l==1 or 2 or 3 :
                continue
            
        print("Thank you",a,"for filling in the feedback!")
l1=["Was the managent friendly?","Did wee meet your expectations?","Was it easy to find what you were looking for?"]
l2=["Rate your experience:","Rate the quality of food:","Rate the management:"]
l3=["Would you recommend our company to your friends?","Would you think of repeating your business with us?"," Were we able to satisfy your need?"]
lm=[l1,l2,l3]
home()
