# COSC 316-001 Assignment 1
# Written by Alex Robbins, 2019
# For educational purposes only.


# This is the User class for storing user data
# (which would otherwise be on a database in a real-world scenario)
# Similar to the server program, a segment of code for hashing was taken from:
# https://stackoverflow.com/questions/40351791/how-to-hash-strings-into-a-float-in-01

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
