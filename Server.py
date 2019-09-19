from User import User
import re
import csv

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
