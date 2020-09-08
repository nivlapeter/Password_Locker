class User:
    '''
    class that generates new instances of users
    '''

    user_list = [] #empty user list
  
    def __init__(self,username,password):

        self.username = username
        self.password = password

    def registration(self):
        '''
        registration method adds users to the system
        '''
        User.user_list.append(self)

class Credentials:
    '''
    class that generates user credentials
    '''
    credentials_list = [] #empty credentials list

    def __init__(self,information_details):
        self.information_details = information_details

    def save_credentials(self):
        '''
        save credentialsmethod saves credentials object into the credentials_list
        '''
        Credentials.credentials_list.append(self)