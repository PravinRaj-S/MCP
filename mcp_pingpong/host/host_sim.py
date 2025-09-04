import os, sys 
sys.path.append(os.path.dirname(os.path.dirname(__file__))) 


from client.client_main import MCPClient 


if __name__ == "__main__": 
    client = MCPClient("server/server_main.py") 


print("Host calling ping:", client.send_request("ping")) 
print("Host calling getTime:", client.send_request("getTime"))