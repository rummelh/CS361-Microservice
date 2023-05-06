import time
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv_json()
    print(f"Received request: {message}")

    #extract values
    decode_json = json.loads(message)
    duration = decode_json["duration"]
    deposit = decode_json["deposit"]
    chores = decode_json["chores"]

    #converts wait time to seconds
    wait_time = duration * 60

    #waits amount of time specified in user input
    time.sleep(wait_time)

    json_dump = {"duration": duration, "deposit": deposit, "chores": chores}
    add_to_json = json.dumps(json_dump)

    #Send reply back to client
    socket.send_json(add_to_json)