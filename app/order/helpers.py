
class DashboardHelpers:
    '''Dashboard Helpers'''
    def __init__(self):
        pass
    
class UserInventoryHelper:
    '''User Inventory'''
    def __init__(self, username=None, password=None, token=None):
        self.username = username
        self.password = password
        if token is None:
            self.token = self.authenticate()
            
    def authenticate(self):
        '''Authenticate with record that store in database'''
        return True