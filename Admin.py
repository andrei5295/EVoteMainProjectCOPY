class Admin:

    def __init__(self,username,password):
        self.user = username
        self.pw = password

    def changePassword(self,newPw):
        self.pw = newPw
