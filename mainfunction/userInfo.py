#program Entry Point
def greet_user():
    # gets user's name and greets them
    name = input("Enter your name: ")
    print("Hello, " + name + "!")
    return name
def get_age():
    #gets user's age

    age_str = input("Enter your age: ")
    age = int(age_str)
    return age

def display_info(name, age):
    # displays user's information
    print("\n=== User Profile ===")
    print("Name: " + name)
    print("Age: " + str(age))
    print("Grade level: Sienior")

def main():

    print("Welcome to Profile creator")
    print("-" * 30)

    user_name = greet_user()
    user_age = get_age()

if __name__ == "__main__":
    main()