from Server import Server

# Initilize a server "session" and establish link
s = Server()
response = s.request_id()

# Client gets the password from the user and hashes it
# using the hash function returned from the server.
# (note in this case, we assume the client program knows how to interpret response)
password = input("Please enter password: ")
password_hash = response[1].h(password)

# The client generates a value using the provided function
# and sends this value back to the server.
reply_to_server = response[2].f(response[0],password_hash)
auth = s.verify_password(reply_to_server)

# If the response is True, the user is logged on, false otherwise.
if auth:
    print("You are now logged in")
else:
    print("Invalid password")
