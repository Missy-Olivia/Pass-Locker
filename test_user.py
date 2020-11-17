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

if __name__ == "__main__":
    unittest.main()
