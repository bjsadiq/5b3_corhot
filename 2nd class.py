
string1 = "This is a string"
string2 = "I love this string"

# print (string1+ " " +string2)
# print (string1, string2)

# print(string1[8])

# print(string1[-1])

# a1 = 45567

# print(a1[3])

# print(string2[1:15:2])
# print(string2[1:7])

# FORMATING

# 

# Bolaji

# firstname = input("Enter your firstname: ")
# lastname = input("Enter your Lastname: ")
# username = lastname[:3]+firstname[-2]

# print(f"""Welcome, {firstname}.
# Your account has been created and 
# your username is {username}.

# Kindly proceed to your portal to login.

# Cheers,

# Mabsad Int.""")

# print("My Dad said,\"make hay while the sun shine\"")


# name = input("Enter your name: \n ::>>")

# print(name.upper())
# print(name.capitalize())

# text1 = "this is an example of the question"
# search_word = input("Enter your search word: ")
# Result = text1.count(search_word)
# print(Result)
# print (search_word.upper())

text = """An alternative is designed development, 
in which high-level insight into the problem can
 make the programming much easier. In this case,
 the insight is that a Time object is really a 
 three-digit number in base 60"""

search_for = input(">").lower()
print(f"{text.lower().count(search_for)} result(S) found")
print(text.lower().replace(search_for,
search_for.upper()))