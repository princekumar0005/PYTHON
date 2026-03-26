# 1. Write a program to create a dictionary of Hindi words with values as their English translation.Provide user with an option to look it up!



words ={

    "kutta" : "Dog",

    "billi" : "Cat",

    "hathi" : "Elephant"

 }



word = input("Enter the finding word ;" )



print(words[word])



# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).



s = set()



n1 = int(input("Enter the 1st number ; "))

n2 = int(input("Enter the 2st number ; "))

n3 = int(input("Enter the 3st number ; "))

n4 = int(input("Enter the 4st number ; "))

n5 = int(input("Enter the 5st number ; "))

n6 = int(input("Enter the 6st number ; "))

n7 = int(input("Enter the 7st number ; "))

n8 = int(input("Enter the 8st number ; "))



s.add(n1)

s.add(n2)

s.add(n3)

s.add(n4)

s.add(n5)

s.add(n6)

s.add(n7)

s.add(n8)



print(s,type(s))



# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?



s = set()



s.add("18")

s.add(18)

print(s)



# 4. What will be the length of following set s:

s = set()

s.add(20)

s.add(20.0)

s.add('20') # length of s after these operations?



print(s,len(s))



# 5. s = {} # What is the type of 's'?



s = {} # type is dict.

print(type(s))



# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.



d = {}



f1 = input("Enter the friend name ; ")

f2 = input("Enter the friend name ; ")

f3 = input("Enter the friend name ; ")

f4 = input("Enter the friend name ; ")



l1 = input("Enter the fav. language ; ")

l2 = input("Enter the fav. language ; ")

l3 = input("Enter the fav. language ; ")

l4 = input("Enter the fav. language ; ")



d.update({f1 :l1})

d.update({f2 :l2})

d.update({f3 :l3})

d.update({f4 :l4})



print(d)



# 7. If the names of 2 friends are same; what will happen to the program in problem  6?



d = {}



name = input("Enter friends name: ")

lang = input("Enter Language name: ")

d.update({name: lang})



name = input("Enter friends name: ")

lang = input("Enter Language name: ")

d.update({name: lang})



name = input("Enter friends name: ")

lang = input("Enter Language name: ")

d.update({name: lang})



name = input("Enter friends name: ")

lang = input("Enter Language name: ")

d.update({name: lang})





print(d)



# 8. If languages of two friends are same; what will happen to the program in problem 6?







d = {}



name = input("Enter friends name: ")

lang = input("Enter Language name: ")

d.update({name: lang})



name = input("Enter friends name: ")

lang = input("Enter Language name: ")

d.update({name: lang})



name = input("Enter friends name: ")

lang = input("Enter Language name: ")

d.update({name: lang})



name = input("Enter friends name: ")

lang = input("Enter Language name: ")

d.update({name: lang})





print(d)



# 9. Can you change the values inside a list which is contained in set S?



s = {8, 7, 12, "Harry", [1,2]}



# In Python, sets are unordered collections of unique elements, and they do not allow mutable objects like lists to be elements. This is because mutable objects, like lists, can change, and modifying them could cause issues with the set's internal structure.



# In your set s, the element [1, 2] is a list, and attempting to include a mutable object like that would cause a TypeError. Here's what happens when you try to define the set:



# python

# Copy

# s = {8, 7, 12, "Harry", [1, 2]}

# This will raise an error:



# bash

# Copy

# TypeError: unhashable type: 'list'

# Can you change values inside the list?

# Even if the set accepted the list (if it were a frozenset or a different structure), Python would not allow you to modify the list inside the set because sets do not support mutable elements. Lists themselves are mutable, and sets require their elements to be immutable (or "hashable").



# Conclusion:

# You cannot include a list inside a set in the first place. If you really need to change the values of a list, you could either:



# Use a list or tuple inside another container like a dictionary or frozenset, which accepts mutable elements.

# Store the list outside of the set and just reference it as needed.



