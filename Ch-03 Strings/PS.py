# 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.





name = input("Enter your name")



print("Good Afternoon",name)

print(f"good afternoon {name}")



# 2. Write a program to fill in a letter template given below with name and date.



letter = '''

Dear <|Name|>,

You are selected!

<|Date|>

'''

# name=input(" entrer ypur name")

# date=input(" entrer the date")

# print(f"Dear {name}\nYou are selected!\n{date}")

print(letter.replace("<|Name|>", "Ram").replace("<|Date|>", "29 feb 2077"))



# 3. Write a program to detect double space in a string



name = "hi i am good  how are you"



print(name.find("  "))



# 4. Replace the double space from problem 3 with single spaces





print(name.replace("  "," "))



# 5. Write a program to format the following letter using escape sequence characters.



letter = "Dear Harry,\n this python course is nice.\n Thanks!"



print(letter)
