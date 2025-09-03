import os, sys # OS and sys for path operations
sys.path.append(os.path.dirname(os.path.dirname(__file__))) # Add project root to sys.path for imports


from client.client_main import MCPClient # Import the MCPClient from the client package


if __name__ == "__main__": # Only run when executed directly
# Start client pointing to server
    client = MCPClient("server/server_main.py") # Tell client which server script to spawn


print("Host calling ping:", client.send_request("ping")) # Call method "ping" -> expect "pong"
print("Host calling getTime:", client.send_request("getTime"))