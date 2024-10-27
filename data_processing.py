# 1.Prompt the user to enter a sentence and then print the sentence in uppercase letters.
a = input ("What is the first thing that comes to your mind? ")
b = a.upper()
print(f"{b}")

print("")

# 2.Prompt the user to enter a paragraph and then count the number of words in the paragraph.
c = input (f"Why was {a} the first thing that came to mind? ").split()
print(f"This paragraph has {len(c)} words")

print("")

# 3.Prompt the user for a string, and check if all the characters in the string are digits. Output true or false
d = input ("Interesting. What else is on your mind? ").isdigit()
print(d)

print("")

# 4.Prompt the user for a string, and replace all occurrences of the letter "a" with the letter "o"
e = input ("Can you give me more detail? ").replace("a", "o")
print(e)

print("")

# 5.Prompt the user to enter their full name and then print their initials. Assume that the user will enter their full name with a space between each name.
def abbrevName(name):
    return ".".join(x[0] for x in name.split()).upper()
f = input ("What is the full name of your current crush? ")
print(f"The initials of your crush's name is {abbrevName(f)}")

print("")

# 6.Prompt the user for a string, then print its length.
g = input("Any final thoughts? ")
print(f"The lenght of this string is {len(g)} characters")