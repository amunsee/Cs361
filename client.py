import socket
import time

def send_data(data):

    host = "127.0.0.1"
    port = 1234
    #reopen socket each time function is called
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port)) #connect to host and port

        if data != 'exit':
            new_data = f"{data[1]},{data[2]}"

        else:
            new_data = 'exit'    
    
        s.send(bytes(new_data, encoding='utf-8'))

        msg = s.recv(1024)
        msg = msg.decode()
        print(msg)
        return (msg)

        s.close()
        

def save_data(last_calculation):
    #setup connection to new server in function.
    pass
    #pass data to microservice with this function
    #Array data values in order: #of people, Airline, luggage choice, total calc cost
    
