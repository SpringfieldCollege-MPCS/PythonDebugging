

# Create a student class
class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __repr__(self):
        return f"Student[{self.first_name}, {self.last_name}, {self.age}"


def sort_list_by_last_name(students):
    "Sort Users by last name and return the sorted list"
    return sorted(students, key=lambda x: x.last_name)

def find_user_by_last_name(studnets, last_name):
    "Find user by the last name, return None if not found"
    for student in studnets:
        if student.last_name == last_name:
            return student
    return None

def print_out_all_students(students):
    for studen in students:
        print(student)

def find_combined_age_of_all_students(students):
    "Get the combined age of all the students"
    combined_age = 0
    for student in students:
        combined_age += student.age
    return combined_age

def main():
    s1 = Student("Jeremy", "Castagno", 30)
    s2 = Student("Tom", "California", 19)
    s3 = Student("Tamara", "Smith", 20)
    s4 = Student("Roy", "Zelda", 2)
    s5 = Student("John", "Smith", 22)

    students = [s1, s2, s3, s4, s5]

    sorted_students = sort_list_by_last_name(students)
    
    last_name = input("Enter the last name of someone you want to find: ")
    user = find_user_by_last_name(sorted_students, last_name)
    if user is not None:
        likely_birth_year = 2022 - user.age
        print(f"This user was most like born in the year {likely_birth_year}")
        new_age = input("Type in the age of to override for this user: ")
        user.age = new_age
    else:
        print("User not found")
    
    print_out_all_students(sorted_students)
    find_combined_age_of_all_students(sorted_students)







    
if __name__ == "__main__":
    main()
