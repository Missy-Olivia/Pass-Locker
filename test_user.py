import unittest
from user import User
from user import Credentials

class TestUser (unittest.TestCase):
    '''
    test class that defines test case for user class behaviour
    '''
    def tearDown (self):
        '''
        method to clean up after running each test
        '''
        User.user_list = []

    def setUp(self):
        '''
        test to run before the other tests
        '''
        self.new_user = User("Missy","xoxo")

    def test_init(self):
        '''
        init test case to test whether the objects have been well initialized
        '''
        self.assertEqual(self.new_user.username, "Missy")
        self.assertEqual(self.new_user.password, "xoxo")

    def test_save_user(self):
        '''
        test verify whether user objects are saved into the  user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_users(self):
        '''
        testing to see if we can store manu user info in our list
        '''
        self.new_user.save_user()
        test_user = User("Loud", "123")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test to see if we can remove user from list
        '''
        self.new_user.save_user()
        test_user = User("Loud", "123")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_display_user(self):
        '''
        running tests to see if we can display all users
        '''
        self.assertEqual(User.display_user(), User.user_list)

    def test_user_verif(self):
        '''
        method to check if we can get user by username
        '''
        self.new_user.save_user()
        test_user = User("Loud", "123")
        test_user.save_user()

        verified = User.user_verif("Loud", "123")

        self.assertTrue(verified)

class TestCreds(unittest.TestCase):
    '''
    test class to generate test cases for credentials class instances
    '''
    def tearDown (self):
        '''
        method to clean up after running each test
        '''
        Credentials.creds_list = []

    def setUp(self):
        '''
        test case to run before other tests
        '''
        self.new_creds = Credentials("Tumblr", "Messy", "321")
    
    def test_init(self):
        '''
        test case to see if the objects have been properly initialized
        '''
        self.assertEqual(self.new_creds.account, "Tumblr")
        self.assertEqual(self.new_creds.user_name, "Messy")
        self.assertEqual(self.new_creds.pass_word, "321")

    def test_save_creds(self):
        '''
        method to test if our credentials are being save into the creds list
        '''
        self.new_creds.save_creds()
        self.assertEqual(len(Credentials.creds_list),1)
    
    def test_save_many_creds(self):
        '''
        method to test if we can add multiple credentials to our list
        '''
        self.new_creds.save_creds()
        test_creds = Credentials("Gmail", "Mae", "345")
        test_creds.save_creds()

        self.assertEqual(len(Credentials.creds_list),2)

    def test_delete_creds(self):
        '''
        method to test if we can remove creds from our list
        '''
        self.new_creds.save_creds()
        test_creds = Credentials("Gmail", "Mae", "345")
        test_creds.save_creds()

        self.new_creds.delete_creds()
        self.assertEqual(len(Credentials.creds_list),1)

    def test_find_creds(self):
        '''
        method to test if we can find credentials using only the account
        '''
        self.new_creds.save_creds()
        test_creds = Credentials("Gmail","Mae", "345")
        test_creds.save_creds()

        my_creds = Credentials.find_creds("Gmail")
        self.assertEqual(my_creds.account, test_creds.account)

    def test_display_creds(self):
        '''
         method to display creds list
        '''
        self.assertEqual(Credentials.display_creds(), Credentials.creds_list)

if __name__ == "__main__":
    unittest.main()
