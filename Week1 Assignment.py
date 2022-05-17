# # Write a program that takes 3 numbers from the user 
# # and computes the average

# d = input("Enter the first number:" )
# e = input("Enter the second number:" )
# f = input("Enter the third number:" )
# 
# d = float(d)
# e = float(e)
# f = float(f)
# g = d + e + f
# h = (g/3)
# print(f"""The average of the numbers is:{h}""")

# Write a program that takes a sentence from the user and 
# changes the first word to upper case.

# name = input("Write your sentence here: \n ::>>")

# print(name.upper())

# Write a program with the sentence "I am learning python". 
# When your program is run, the string "I" should be changed
# to "you"

text = """I am learning python"""

print(text.replace("I am","You are"))
 
# Write a program that takes the string 
# "I hope you had fun today in class". 
# Print the number of times that the
# string "a" appears in the sentence. ""

text = """i hope you had fun today in class"""
search_for = input(">")
print(f"{text.lower().count(search_for)} result(s) found")