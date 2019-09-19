from Server import Server

s = Server()

response = s.request_id()

password = input("Please enter password: ")
password_hash = response[1].h(password)

reply_to_server = response[2].f(response[0],password_hash)

s.verify_password(reply_to_server)
