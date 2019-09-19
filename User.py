class User():

    def __init__(self,userID,passwordHash):
        self.userID = userID
        self.passwordHash = passwordHash

    def getHash(self):
        return self.passwordHash
