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

        