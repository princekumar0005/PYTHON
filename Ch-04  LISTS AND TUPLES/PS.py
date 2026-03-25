# 1. Write a program to store seven fruits in a list entered by the user.

fruits = []

f1 = input("Enter Fruit name: ")
fruits.append(f1)
f2 = input("Enter Fruit name: ")
fruits.append(f2)
f3 = input("Enter Fruit name: ")
fruits.append(f3)
f4 = input("Enter Fruit name: ")
fruits.append(f4)
f5 = input("Enter Fruit name: ")
fruits.append(f5)
f6 = input("Enter Fruit name: ")
fruits.append(f6)
f7 = input("Enter Fruit name: ")
fruits.append(f7)

print(fruits)


# 2. Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

f1 = int(input("Enter Marks here: "))
marks.append(f1)
f2 = int(input("Enter Marks here: "))
marks.append(f2)
f3 = int(input("Enter Marks here: "))
marks.append(f3)
f4 = int(input("Enter Marks here: "))
marks.append(f4)
f5 = int(input("Enter Marks here: "))
marks.append(f5)
f6 = int(input("Enter Marks here: "))
marks.append(f6)

marks.sort()

print(marks)

# 3. Check that a tuple type cannot be changed in python.

# a = (34, 234, "Harry") 

# a[2] = "Larry" # Tuple → immutable (cannot change)


# 4. Write a program to sum a list with 4 numbers.

a = [2,5,5,5,6]

print(sum(a))

# 5. Write a program to count the number of zeros in the following tuple:

a = (7, 0, 8, 0, 0, 9)
n = a.count(0)
print(n)

# WAP to ask the user to enter name of their three fav. movies and stored in list.

Movies = []

a= input("enter you 1st fav. movie")
b= input("enter you 4st fav. movie")
c= input("enter you 3st fav. movie")

Movies.append(a)
Movies.append(b)
Movies.append(c)

print(Movies)

# WAP to cheak if a list contains a plindrome of element.(hint copy() method
