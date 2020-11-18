#!/usr/bin/env python3.6
from user import User
from user import Credentials

def create_new_user(username,password):
    '''
    function to create new user
    '''
    new_user = User(username,password)
    return new_user

def save_users(user):
    '''
    function to save users in user list
    '''
    user.save_user()

def delete_users(user):
    '''
    function to delete users from user list
    '''
    user.delete_user()

def display_users(user):
    '''
    fx to show all users in user list
    '''
    return user.display_user()

def users_verif(username, password):
    '''
    fx to find user by username
    '''
    verified = User.user_verif(username,password)
    return verified

def create_new_creds(account, user_name, pass_word):
    '''
    fx to create new credentials
    '''
    new_credentials = Credentials(account, user_name, pass_word)
    return new_credentials

def save_new_creds(credentials):
    '''
    fx to save credentials in our creds list
    '''
    credentials.save_creds()

def delete_new_creds(credentials):
    '''
    fx to delete credentials from our creds list
    '''
    credentials.delete_creds()

def findCreds(account):
    '''
    fx to find credentials by using account
    '''
    return credentials.find_creds(account)

def display_all_creds(credentials):
    '''
    fx to display credentials in our creds list
    '''
    return credentials.display_creds()

def lock():
    print("Hello, what is your name?")
    name = input()

    print(f"Hello {name}, welcome to your password locker! What would you like to do today? ")
    print('\n')
    while True :
        print("Please choose a shortcode to proceed : \n ca---- create new user account \n li------- log into existing acount")
        short_code = input().lower
    
        if short_code == 'ca' :
            print("Create account")
            print("-"*20)

            print("Username :")
            username= input()

            print("Enter Password :")
            password = input()
            
            save_users(create_new_user(username,password))
            print('\n')
            print(f"Hey {username } your account has been successfully created!This is you password : {password} ")
            print("-"*50)
        elif short_code == 'li' :
            print("Enter login info : \n")
            print(f"-"*30)  

            print("User name: \n")
            username = input()

            input("password: \n")
            password = input()

            for user in users_verif():
                if users_verif == login :
                    print(f"Hello {username}.Welcome To Password Locker")  
                    print('\n')
        else :
            print("INVALID ENTRY!PLEASE TRY AGAIN.")
            break
    while True:
        print("use these short codes: \n cc - create new credentials \n dc - display credentials \n fc- find credentials \n del - delete credentials \n ex - exit application")
        short_code = input().lower()
        if short_code == 'cc' :
            print("Create New Credential")
            print("."*20)

            print("Account name ....")
            account = input()

            print("Your Account username")
            user_name = input()

            print("Your account password")
            pass_word = input()
            
            save_new_creds(create_new_creds(account, user_name, pass_word))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {user_name} - Password:{pass_word} created succesfully")
            print('\n')
        elif short_code == 'dc':
            if display_all_creds():
                print("Here is your credentials list")
                print('_'* 30)
                for account in display_all_creds():
                    print(f" Account:{account.account} \n Username:{user_name}\n Password:{pass_word}")
                    print('_'* 30)
            else:
                print("No credentials yet saved")

        elif short_code == 'fc':
            print("What account are you looking for?")
            account_name = input()
            if findCreds(account_name):
                search_acc = findCreds(account_name)
                print(f"account Name : {search_acc.account}")
                print('\n')
                print(f"User Name: {search_acc.user_name} Password :{search_acc.pass_word}")
                print('\n')
            else:
                print("Credential does not exist!")

        elif short_code == 'del':
            print("What credentials do you want to delete?")
            account_name = input()
            if findCreds(account_name):
                search_acc = findCreds(account_name)
                search_acc.delete_new_creds()
                print("\n")
                print(f"Your stored credentials for : {search_acc.account} successfully deleted!!!")
                print("\n")
            else :
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'ex' :
            print("Bye....")
            break
        else:
            print("Invalid input!")
if  __name__ == "__main__":
    lock()


