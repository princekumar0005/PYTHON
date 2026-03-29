# 1. Write a program using functions to find greatest of three numbers.



def great():

    a = int(input("enter the number"))

    b = int(input("enter the number"))

    c = int(input("enter the number"))



    if(c<a>b):

        print(f"a is greaterst num {a}")

    elif(b<c>a):

        print(f"c is greaterst num {b}")

    elif(c<b>a):

        print(f"b is greaterst num {c}")



great()



# 2. Write a python program using function to convert Celsius to Fahrenheit.



def f_to_c(f):

    return 5*(f-32)/9



f = int(input("Enter temperature in F: "))

c = f_to_c(f)

print(f"{round(c, 2)}°C")  



# 3. How do you prevent a python print() function to print a new line at the end.

 

print("a")

print("a")

print("a",end="")

print("a",end="")



# 4. Write a recursive function to calculate the sum of first n natural numbers.



'''

sum(1) = 1

sum(2) = 1 + 2

sum(3) = 1 + 2 + 3

sum(4) = 1 + 2 + 3 + 4

sum(5) = 1 + 2 + 3 + 4 + 5



sum(n) = 1 + 2 + 3 + 4.... n -1 + n

sum(n) = sum(n-1) + n

'''



def sum(n):

    if(n==1):

        return 1

    return sum(n-1) + n



print(sum(4))



# 5. Write a python function to print first n lines of the following pattern:

# ***

# ** - for n = 3

# *



def pattern(n):

    if(n==0):

        return

    print("*" * n)

    pattern(n-1)





pattern(3)





# 6. Write a python function which converts inches to cms



def inch_to_cms(inch):

    return inch * 2.54



n = int(input("Enter value in inches: "))



print(f"The corresponding value in cms is {inch_to_cms(n)}")

    

# 7. Write a python function to remove a given word from a list ad strip it at the same time.



def rem(l, word):

    n = [] 

    for item in l:

        if not(item == word):

            n.append(item.strip(word))

    return n





l = ["Harry", "Rohan", "Shubham", "an"]



print(rem(l, "an"))





# 8. Write a python function to print multiplication table of a given number.



def multiply(n):

    for i in range(1, 11):

        print(f"{n} X {i} = {n*i}")



multiply(1000) 





# WAF to print the lenght of a list (list is the parameter)



def lenght(list):

    print(len(list))



l = ["Harry", "Rohan", "Shubham", "an"]   

lenght(l)



# WAF to print the element of a list in a single line.(list is the para meter )



def l(list):

    for i in list:

        print(i,end=" ")





li = ["Harry", "Rohan", "Shubham", "an"]   

l(li)



# WAF to find the factorial of n. (n is the parameter)



def factorial(n):

    if(n==1 or n==0):

        return 1

    return n * factorial(n-1)





n = int(input("Enter a number: "))

print(f"The factorial of this number is: {factorial(n)}")



# WAF to convert USD to INR.



def cul_inr(usd_no):

    to = usd_no*85.56

    print(usd_no,"usd","=",to,"INR")



cul_inr(int(input("enter the value")))
