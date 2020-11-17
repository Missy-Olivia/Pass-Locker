class User :
    '''
    class to generate new intances of a user
    '''
    user_list = []

    def __init__ (self,username,password):
        '''
        method that helps define the properties of our objects.
        '''
        self.username = username
        self.password = password
    
    def save_user(self):
        '''
        method that saves new user instance in user list
        '''
        User.user_list.append(self)
    
    @classmethod
    def display_user(cls):
        '''
        method to display infromation passed in user list
        '''
        return cls.user_list

    def delete_user(cls):
        '''
        method to delete the user information
        '''
        User.user_list.remove(self)

class Credentials :
    '''
    class to create credential instances
    '''
    creds_list = []
    
    def __init__(self, account, user_name, pass_word):
        '''
        method for credential properties
        '''
        self.account = account
        self.user_name = user_name
        self.pass_word = pass_word

    def save_creds(self):
        '''
        method to save credentials in credential list
        '''
        Credentials.creds_list.append(self)

    def delete_creds(self):
        '''
        method to remove credential info from our list
        '''
        Credentials.creds_list.remove(self)
        