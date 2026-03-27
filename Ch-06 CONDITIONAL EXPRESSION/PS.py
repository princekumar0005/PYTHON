# 1. Write a program to find the greatest of four numbers entered by the user.



a = int (input(" Enter the number ; "))



if(a>4):

    print(" a is greater then four")



elif(a==4):

    print(" a is equal to four")





else:

    print("a is not equal to four")    



# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.





mark1 = int(input("Enter your first subject marks"))

mark2 = int(input("Enter your second subject marks"))

mark3 = int(input("Enter your third subject marks"))



total_percentage = (100*(mark1+mark2+mark3))/300



if(total_percentage>=40 and mark1>=33 and mark2>=33 and mark3>=33):

    print("You are passed:", total_percentage)



else:

    print("YOu are fail try again next year :",total_percentage)    



# 3. A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program

# to detect these spams.    





p1 = "Make a lot of money"

p2 = "buy now"

p3 = "subscribe this"

p4 = "click this"



massage = input("Enter your comment")



if((p1 in massage) or (p2 in massage) or(p3 in massage)or (p4 in massage)):

    print("This comment is spam")



else:

    print("This commant not spam")



# 4. Write a program to find whether a given username contains less than 10 characters or not.    



name = input("Enter your username")



if(len(name)<10):

    print("username contains lass than 10 cherecters")



else:

    print("Username is contains greter than 10 charecters")



# 5. Write a program which finds out whether a given name is present in a list or not.



name = [

    "harry",

    "prince",

    "king",

    "ram",

    "somya",

    "rohan"

]    



enter = input("Enter the name ;")



if(enter in name):

    print("name is finded")



else:

    print("name is not found")    





# 6. Write a program to calculate the grade of a student from his marks from the

# following scheme:

# 90 – 100 => Ex

# 80 – 90 => A

# 70 – 80 => B

# 60 – 70 =>C

# 50 – 60 => D

# <50 => F

    



mark = int(input("Enter your marks "))



if(mark>=90 and mark<=100):

    grade = "EX"

elif(mark>=80 and mark<=90):

    grade ="A"

elif(mark>=70 and mark<=80):

    grade ="B"

elif(mark>=60 and mark<=70):

    grade ="C"

elif(mark>=50 and mark<=60):

    grade ="D"

elif( mark<50):

    grade ="F"



print("Your grade is ; ",grade)   



# 7. . Write a program to find out whether a given post is talking about “Harry” or not



post = input("Enter the post: ")







if("harry" in post.lower()):

    print("This post is talking about harry")



else:

    print("This post is not talking about harry")
