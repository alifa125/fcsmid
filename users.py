import datetime
username=input("enter your name")
gender=input("choisier your gender male or femal ")
def display(username,gender):
    if gender=="male":
        return("welcome mr "+username)
    else:
        return ('welcome mrs '+username )
          
print("1. Check my Salary")
print("2. Exit")
def check_salary(username):
   
    salary = 50000
    print(f"Your salary, {username}, is ${salary}")
while True:
    display(gender, username)
    choice = input("Enter your choice: ")

    if choice == '1':
        check_salary(username)
    elif choice == '2':
        with open("login_timestamps.txt", "a") as file:
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{username} logged in at {timestamp}\n")
        break
    else:
            print("Invalid choice. Please choose again.")

def main():
    gender = input("Enter your gender (male/female): ").lower()
    username = input("Enter your name: ")
    display(gender, username)