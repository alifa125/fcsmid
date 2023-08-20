import csv
import datetime
from sqlite3 import Row
admins = {}
def read():
   
    with open(r"employees.txt","r") as f:
    # Read the data from the text file.
      reader = csv.reader(f)
      
      for row in reader:
        admin_id, username, timestamp, gender, salary = row
        admins[admin_id] = {
            "username": username,
            "timestamp": timestamp,
            "gender": gender,
            "salary": salary,
        }
    return admins
    

       
print('service:\n ')       
print('1. Display Statistics\n')
print('2. Add an Employee\n')
print(" 3. Display all Employees\n")
print(' \n 4. Change Employees Salary')
print('\n 5. Remove Employee')
print('\n6. Raise Employees Salary')
print('\n 7. Exit')






service = input('choice your server ')

if int(service)== 1: 
    male =0
    female=0
    def statis(admins):
        
       
       for admin in admins.values():
        if admin['gender'] == 'male':
            male += 1
        else:
            female += 1
    
    print("male ="+ str(male)+'\nfemale='+str(female))            
elif int(service)==2:
    read()
    admin_id=Row
    username = input("Enter username: ")
    gender = input("Enter gender (male/female): ")
    salary = int(input("Enter salary: "))
    timestamp = datetime.datetime.now().strftime("%Y%m%d")
    admins[admin_id.strip] = {
        
        'username': username,
        'timestamp': timestamp,
        'gender': gender,
        'salary': salary
    }
    print("Employee added successfully!")
elif int(service)==3:
    admins = {}
    with open(r"employees.txt","r") as f:
    # Read the data from the text file.
      reader = csv.reader(f)
      
      for row in reader:
        admin_id, username, timestamp, gender, salary = row
        admins[admin_id] = {
            "username": username,
            "timestamp": timestamp,
            "gender": gender,
            "salary": salary,
        }
        
    for admin in admins:
      print(admin, admins[admin])   
elif int(service)==4:
    admins ={}   
    admin_id = input("Enter employee's ID: ")
    new_salary = int(input("Enter new salary: "))
    if admin_id in admins:
       admins[admin_id].salary = new_salary
       print("Salary changed successfully.")
    else:
        print("Employee not found.")
elif int(service)==5:
    key=input("enter the id ")
    def delete_item(admins, key):
      if key in admins:
         del admins[key]
      else:
        print("The key does not exist in the dictionary.")    
elif int(service)==6:
    read()
    id=input('enter the id for employee')
    j=float(input('the the raise percentage '))
 
elif int(service)<0 or int(service)>8:
    print('incrrorect server')

else :
    exit()
    
  
    
            
            