import unittest
from user import User
from user import Credentials

class TestUser (unittest.TestCase):
    '''
    test class that defines test case for user class behaviour
    '''
    def tearDown (sefl):
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


if __name__ == "__main__":
    unittest.main()
