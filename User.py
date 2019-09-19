from zlib import crc32
class User():

    def __init__(self,userID,passwordHash):
        self.userID = userID
        self.passwordHash = passwordHash

    def bytes_to_float(self,b):
        return float(crc32(b) & 0xffffffff) / 2**32

    def str_to_float(self,s, encoding="utf-8"):
        return self.bytes_to_float(s.encode(encoding))

    def getHash(self):
        return self.str_to_float(self.passwordHash)

    def getUserID(self):
        return self.userID
