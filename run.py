#!/usr/bin/env python3.8
from user import User # Importing the User class
from user import Credentials # Importing the contact class

def create_user(u_name,password):
    '''
    Function to create a new user
    '''
    new_user = User(u_name,password)
    return new_user

def registration(user):
    '''
    Funtion to register a user
    '''
    user.registration()

def create_credentials(information_details):
    '''
    Function to create a new credentials
    '''
    new_credential = Credentials(information_details)
    return new_credential

def save_credentials(credentials):
    '''
    function to save credentials
    '''
    credentials.save_credentials()

def main():

    print("Hello! and welcome to password locker")
    print('\n')

    while True:
        print("use these short codes : \n ca - create account, \n si - sign in, \n exit - q")
        
        short_code = input().lower()

        if short_code == 'ca':
            print("-"*40)
            print("Create an account")
            print("\n")
            print("create username....")
            u_name = input()
            print("\n")
            print("create password....")
            password = input()

            registration(create_user(u_name,password)) #create and register a new user
            print ("\n")
            print(f"New User {u_name} created")
            print ("\n")

        elif short_code == 'si':
            print("-"*40)
            print("Log in using your username and password")
            print("\n")
            print("enter username....")
            default_username = input()
            print("\n")
            print("enter password....")
            default_password = input()

            count = 0
            count += 1
            

        while default_username == "Jackson" and default_password == "chapatimoto14":


            if default_username == "Jackson" and default_password == "chapatimoto14":
                print("Welcome")
           
        
            elif default_username != "Jackson" and default_password != "chapatimoto14":
                print("Your username or password is wrong")
                default_username = input("\n\nUsername:....")
                default_password = input("password:...")
                count += 1
                continue

            elif default_username != "Jackson" and default_password != "chapatimoto14":
                print("Your username or password is wrong")
                default_username = input("\n\nUsername:....")
                default_password = input("password:...")
                count += 1
                continue

            elif default_username != "Jackson" and default_password != "chapatimoto14":
                print("Your username or password is wrong")
                default_username = input("\n\nUsername:....")
                default_password = input("password:...")
                count += 1
                continue

            elif count == 3:
                print("\n You have exhausted your login attempts. Goodbye")
                break
        
            elif short_code == "q":
                print("Bye .......")
                break
            else:
                print("I really didn't get that. Please use the short codes")
    
    while True:
        print("use these short codes : \n ca - create account, \n si - sign in, \n exit - q")
        short_code = input().lower()

        if short_code == 'ca':
            print("\nEnter your bio details")
            print("\nThe site information....")
            information_details = input()
            save_credentials(create_credentials(information_details))
            print("\nCredentials created successfully!")

        elif short_code == 'si':
            print("\n Welcome to your Bio!")
            information_details = input()

        elif short_code == "q":
             print("Bye .......")
             break
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
            

