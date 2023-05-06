import zmq
import json

context = zmq.Context()

#  Socket to talk to server
print("Connecting to time microservice…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#duration must come in unit of minutes
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

#  Get the reply.
message = socket.recv_json()
print(f"Received reply [ {message} ]")