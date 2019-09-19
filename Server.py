from User import User
import re
import csv
import random
import hashlib
from zlib import crc32

class Server():

    # First open password file and initilize an array (simulating a database)
    def __init__(self):
        file = open("passwords.csv", 'r')
        self.user_array = []
        self.r = 0
        self.u = ''
        with open("passwords.csv", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                u = User(row['username'], row['password'])
                self.user_array.append(u)
        file.close()

    # This method gets the ID from the user and checks against "database"
    def request_id(self):
        user_found = False
        while not user_found:
            input_id = input("Please enter user ID: ")
            match = False
            for user in self.user_array:
                if user.getUserID() == input_id:
                    match = True
                    self.u = user
            if not match:
                print("User ID invalid.")
            else:
                user_found = True
                h = H()
                r = random.random()
                f = F()
                self.save_nonce(r)
                return [r,h,f]

    def save_nonce(self,r):
        self.r = r

    def verify_password(self,reply):
        temp_hash = self.u.getHash()
        temp_result = F().f(self.r,temp_hash)
        if temp_result == reply:
            return True
        else:
            return False


class H():
    def bytes_to_float(self,b):
        return float(crc32(b) & 0xffffffff) / 2**32

    def str_to_float(self,s, encoding="utf-8"):
        return self.bytes_to_float(s.encode(encoding))

    def h(self,password_plaintext):
        encoded_password = str.encode(password_plaintext)
        hashed_password = hashlib.sha224(encoded_password).hexdigest()
        float_password = self.str_to_float( hashed_password )
        return float_password

class F():
    def f(self,r,hash):
        # TODO: Put a better function
        return r + hash
