# Part A - 1: Create and index a list
fruits = ["Apple", "Banana", "Orange", "Mango", "Pineapple"]

print("Fruits:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Second fruit:", fruits[1])

# Part A - 2: List slicing
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print("First three numbers:", numbers[:3])
print("Last three numbers:", numbers[-3:])
print("Numbers from index 2 to index 5:", numbers[2:6])  # 6 is excluded
print("Every second number:", numbers[::2])
print("List in reverse order:", numbers[::-1])

#  Part A - 3: Common list methods
animals = ["cat", "dog", "rabbit"]

print("Original list:", animals)

# Add "lion" to the end
animalsappend = animals.append("lion")
print("Append", animals)

# Insert "tiger" at index 1
animalsinsert = animals.insert(1, "tiger")
print("Insert", animals)

# Remove "dog"
animalsremove = animals.remove("dog")
print("remove", animals)

# Remove and return the last item
animalsextend = animals.extend(["beer", "dear"])
print("Remove & Return", animals)

# Sort alphabetically
animalssort = animals.sort()
print("Sort", animals)

# Reverse the list
animalsreverce = animals.reverse()
print("Reverce", animals)

# Print the final List 
print(animals)

# Part B - 1: Create and index a tuple
colors = ("Red", "Green", "Blue", "Yellow", "Black")

print("Entire tuple:", colors)
print("First color:", colors[0])
print("Last color:", colors[-1])
print("Third color:", colors[2])

# Part B - 2: Tuple slicing
numbers = (10, 20, 30, 40, 50, 60, 70)

print("First three numbers:", numbers[:3])
print("Last three numbers:", numbers[-3:])
print("Numbers from index 2 to index 5:", numbers[2:6])  # 6 is excluded
print("Tuple in reverse order:", numbers[::-1])

# Part B - 3: Tuples are immutable
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

# This line will cause an error
days[0] = "Sunday"

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# The value could not be changed because "days" is a tuple, and tuples are immutable.
# That means once a tuple is created, you cannot change, add, or remove its items.

# Create a new tuple with the change
days = ("Sunday",) + days[1:]
print(days)

# Part C - 1: Create a dictionary
student = {
    "name": "John",
    "age": 20,
    "course": "Computer Science",
    "score": 85
}

print("Entire dictionary:", student)
print("Name:", student["name"])
print("Course:", student["course"])
print("Score:", student["score"])


# Part C - 2: Access and update a dictionary
person = {"name": "Mary", "age": 22, "city": "Lagos"}

print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

# Change the age to 23
person["age"] = 23

print("Updated dictionary:", person)

# Part C - 3: Add and remove dictionary items
book = {"title": "Python Basics", "author": "John Smith", "year": 2025}

print("Original:", book)

# Add a "price" key
book["price"] = 5000

# Add a "category" key
book["category"] = "Programming"

# Change the year
book["year"] = 2026

# Remove the category key
del book["category"]

print("Final dictionary:", book)

# Part C - 4: Dictionary methods
student = {"name": "David", "age": 21, "course": "Python", "score": 90}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Check whether "name" exists in the dictionary
if "name" in student:
    print("'name' exists in the dictionary.")
else:
    print("'name' does not exist.")

# Get the student's score using get()
print("Score:", student.get("score"))


