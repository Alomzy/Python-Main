# Classwork
# 1.	Class and Objects: Create a class called Student with the attributes name, age, and score. 
# Class attribute called School, value: Nano Academy Create at least two student objects.
# 2.	Encapsulation: Make the score attribute 
# private so it cannot be accessed directly from outside the class.
class Student:
    def __init__(self, name, age, score):
            self.name = name
            self.age = age
            self.__score = score
    School = "Nano Academy"
# Creating two student objects
# 3.	Property Getter and Setter: Create a getter to retrieve a student’s score and a setter to update 
# the score. The setter must ensure that the score is between 0 and 100.



    # 1. Property Getter
    @property
    def score(self):
        return self.__score

    # 2. Property Setter
    @score.setter
    def score(self, new_score):
        if 0 <= new_score <= 100:
            self.__score = new_score
        else:
            raise ValueError("Score must be between 0 and 100")


# 3. Class Method

    @classmethod
    def change_school(cls, new_school):
        cls.School = "new_school"

    # 4. Static Method
    @staticmethod
    def is_passed(score):
        return score >= 50

    # 5. Instance Method
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Score:", self.score)
        print("School:", self.School)

        if Student.is_passed(self.score):
            print("Result: Passed")
        else:
            print("Result: Failed")

        print("-" * 30)


# Creating student objects
student1 = Student("John", 18, 85)
student2 = Student("Jane", 20, 45)


# Displaying student information
student1.display_info()
student2.display_info()


# Updating a student's score using the setter
student2.score = 65

print("After updating Jane's score:")
student2.display_info()


# Changing the school for all students
Student.change_school("Nano Academy")

print("After changing the school:")
student1.display_info()
student2.display_info()


student1 = Student("John", 18, 85)
student2 = Student("Jane", 20, 92)
