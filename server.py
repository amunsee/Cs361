import socket
host = "127.0.0.1"
port = 1234

def get_cost(airline, baggage):
    if airline == 'United':
        united_costs = {
            'Oversized bag': '18.99',
            'Overweight bag': '23.99',
            'Extra bag': '30.00'
        }
        cost = united_costs[baggage]

    elif airline == 'Delta':
        delta_costs = {
            'Oversized bag': '19.00',
            'Overweight bag': '20.00',
            'Extra bag': '40.00'
        }
        cost = delta_costs[baggage]

    elif airline == 'Southwest':
        southwest_costs = {
            'Oversized bag': '15.79',
            'Overweight bag': '18.79',
            'Extra bag': '39.99'
        }
        cost = southwest_costs[baggage]
    
    else:
        american_costs = {
            'Oversized bag': '42.59',
            'Overweight bag': '37.29',
            'Extra bag': '50.00'
        }
        cost = american_costs[baggage]
    
    return cost


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port)) #server name is computer host, on port 1234
    while True:
        s.listen() #listening for requests and can take a queue of 5 items, changeable
        conn, addr = s.accept()
        with conn:
            print(f"connect by {addr}")
            data = conn.recv(1024)          
            
            if data == 'exit':
                print('exit')
                s.close()
                exit()

            if data: 
                print(f"message recieved from client: {data}")
                data = data.decode()
                data_values = data.split(',')
                cost = get_cost(data_values[0], data_values[1])

                conn.send(bytes(cost, encoding='utf-8'))
                print(data)
                
        
s.close()


    
    
