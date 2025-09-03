from .transport import StdIOTransport

class MCPClient:
    def __init__(self, server_path):
        self.transport = StdIOTransport(server_path)
        self.request_id = 0

    def send_request(self, method, params={}):
        self.request_id += 1
        req = {
            "jsonrpc": "2.0",
            "id": self.request_id,
            "method": method,
            "params": params
        }
        return self.transport.send_request(req)
