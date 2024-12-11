#Assignment 5 

#Exercise 1: List Manipulation
#Create a list called fruits containing the following fruits: apple, banana, cherry, date.
#Add "elderberry" to the end of the list. Then remove "banana" from the list.
#Sort the list in alphabetical order. Then print the list.
fruits = ["apple", "banana", "cherry", "date"]
fruits.append("elderberry")
fruits.remove("banana")
fruits.sort()
print(f"Exercise 1: {fruits}")


print("")


#Exercise 2: Dictionary Basics
#Create a dictionary called student with the following key-value pairs:
#name: John Doe. age: 25. major: Computer Science.
#Change the value of 'major' to "Electrical Engineering".
#Add a new key-value pair: 'year' with a value of 'Senior'.
#Print out the keys and the values in the dictionary.
student = {
    'Name': 'John Doe', 'Age': 25, 'Major': 'Computer Science',
}
student["Major"] = "Electrical Engineering"
student['Year'] = 'Senior'
print(f"Exercise 2: {student}")


print("")


#Exercise 3: List of Dictionaries
#Create a list of dictionaries, where each dictionary represents a book and has the following keys:
#title, author, and year.
#Add at least 3 books to your list. Print the title of the second book in the list.
#Print the year the third book was published.
#Iterate over the list and print out each book's title and author.
books = [
    {'Title': 'Mass Effect', 'Author': 'Shepard', 'Year': 2007},
    {'Title': 'Mass Effect 2', 'Author': 'Tim', 'Year': 2010},
    {'Title': 'Mass Effect 3', 'Author': 'Anderson', 'Year': 2012},
]
print(f"Exercise 3: {books[1]['Title']}")
print(books[2]['Year'])
for book in books:
    print(book['Title'], book['Author'])
  

print("")


#Exercise 4: Dictionary containing a List
#Create a dictionary called courses where the keys are the names of courses and the values are lists of student names enrolled in each course.
#Then complete the following using methods/functions:
#Add 5 students to "math". Remove the third student from "history".
#Print out the students in "chemistry".
#Add a new course "physics" with a list of 4 students.
courses = {
    'Math': ['Ryan', 'Caleb', 'Jackson'],
    'History': ['Kim', 'Pat', 'EJ'],
    'Chemistry': ['Greg', 'Nicole', 'Carrie'],
}
courses['Math'].extend(['Shadik', 'Andrew', 'Austein', 'Ray', 'Lorenzo'])
courses['History'].remove('EJ')
courses['Physics'] = ["Skyler", "Tara", "Taylor", "Jenna"]
print(f"Exercise 4: {courses}")