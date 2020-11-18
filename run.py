#!/usr/bin/env python3.6
from user import User
from user import Credentials

def create_new_user(userName,passWord):
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


