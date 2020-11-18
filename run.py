#!/usr/bin/env python3.6
from user import User
from user import Credentials

def create_new_user(username,password):
    '''
    function to create new user
    '''
    new_user = User(userName,passWord)
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
