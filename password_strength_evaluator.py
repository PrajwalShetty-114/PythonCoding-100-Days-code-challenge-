special_characters='''~`!@#$%^&*()_-+=|][}.,{;:'"/?><'''

def password_length_status(Password_length):
   
      if Password_length>=12:
         print("Your Password is more than 12 characters long which is pretty strong")
      elif Password_length>=8:
         print("Strong but good to have 12 characters long")
      elif Password_length>=4:
         print("Your password is short, make it 12 characters long")
      else:
         print("Your Password is very weak, Please make it strong")
   

def check_strength(Password):
   has_digit=False
   # has_number=False
   has_alphabets=False
   has_special_char=False
   upper=False
   Password_length=len(Password)

   for character in Password:
      if character.isdigit():
         has_digit=True
      if character.isalpha():
         has_alphabets=True
         if character.isupper():
            upper=True
      if character in special_characters:
         has_special_char=True
   

   password_length_status(Password_length)
   
   if not has_digit:
   
         print("You don't have digit in your Password, please make sure to have it")
    
   if not has_alphabets:
      
         print("You don't have alphabets in your Password, please make sure to have it")
      
   if not has_special_char:
    
         print("You don't have special character in your Password, please make sure to have it")
      

   if not upper:
      print("It is good to have atleast one upper case letter,\
but your password does not contain any upper case letter  ")



print('''
      This will check the strength of your Password
      Your password must contain atleast one alphabets,digit and special characters
      It's good to have atleast one upper case letter

      please ensure you meet the above requirement while entering the password

''')   


password=input("Enter the password :")
if len(password) == 0:
   print("Please enter the password to check strength of the password")
else:
   check_strength(password)






