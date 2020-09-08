import unittest # Importing the unittest module
from user import User # Importing the User class
from user import Credentials # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that definestest cases for the User class behaviours.

    Args:
        unittest.Testcase:Testcase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Jackson","chapatimoto14") #create user object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        ''' 
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"Jackson")
        self.assertEqual(self.new_user.password,"chapatimoto14")
    
    def test_registration(self):
        '''
        test_registration test case to test if the user object is registered into the user list
        '''
        self.new_user.registration() #registering the new user
        self.assertEqual(len(User.user_list),1)

    def test_register_multiple_users(self):
        '''
        test_register_multiple_users to check if we can save multiple contact objects to our contact_list
        '''
        self.new_user.registration()
        test_user = User("santa","bruteForce") #new user
        test_user.registration()
        self.assertEqual(len(User.user_list),2)

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the Credentials class behaviours.

    Args:
        unittest.Testcase:Testcase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("Jackson,chapatimoto14") #create credentials object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        ''' 
        Credentials.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''  
        self.assertEqual(self.new_credential.information_details,"Jackson,chapatimoto14")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into the credentials_list
        '''
        self.new_credential.save_credentials() #registering the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        '''
        test_register_multiple_users to check if we can save multiple contact objects to our contact_list
        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials("santa,bruteForce") #new credentials
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)



if __name__ == '__main__':
    unittest.main()
   
