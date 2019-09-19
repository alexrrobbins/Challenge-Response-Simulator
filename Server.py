from User import User
import re
import csv
import random

class Server():

    # First open password file and initilize an array (simulating a database)
    def __init__(self):
        file = open("passwords.csv", 'r')
        self.user_array = []

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
            if not match:
                print("User ID invalid.")
            else:
                user_found = True
                h = H()
                r = random.random()
                f = F()
                return [r,h,f]

class H():
    def hash_func(self,password_plaintext):
        return hash(password_plaintext)

class F():
    def one_way_func(self,r,hash):
        # TODO: Put a better function
        return r + hash
