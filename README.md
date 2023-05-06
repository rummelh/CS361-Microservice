# CS361-Microservice

Here is an example call to my microservice: 
print("Connecting to time microservice…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

duration must come in unit of minutes
duration = 1
deposit = 100
chores = ["sweep", "vacuum", "dust"]

#add three values to single dictionary
json_dump = {"duration": duration, "deposit": deposit, "chores": chores}

#add dictionary to json file
add_to_json = json.dumps(json_dump)

#send the request
print(f"Sending request …")
socket.send_json(add_to_json)

The information for duration, deposit, and chores will all be sent by my partners project. I have dummy values here for testing and to show the functionality. 

The values need to be sent via JSON in order to be parsed correctly on my microservice side. 

#  Get the reply.
message = socket.recv_json()
print(f"Received reply [ {message} ]")

This shows how it will receive the data back from my microservice. To use the data that was sent back to the project, use this statement: decode_json = json.loads(message). Then it can be accessed as one would a normal python dictionary. 
![Screenshot 2023-05-06 134857](https://user-images.githubusercontent.com/107904009/236641614-6be1d02f-1b78-4df0-b17e-15f17ac026da.png)

