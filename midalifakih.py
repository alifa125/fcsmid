
print('login page for admin and users ')
max_attempts = 5
for i in range(max_attempts):
        username=input('enter your username   :')
        password=input('enter your password   :')
        
        if username=='admin' and password== 'admin123123' :
            print('welcome in admin page admin' )
            from adminpage import *
            
           
            
        elif username=='ali' and password=='':
            
            
        
            from users import *
            break
        else :
            print('username or password is incorrect ')
            i=i+1
          



    
       
        
        
        


       
    

    