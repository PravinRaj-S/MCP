import subprocess
import json

class StdIOTransport:

    def __init__(self, server_path):
        self.proc = subprocess.Popen(
            ["python", server_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True
        )

    def send_request(self, request):
        self.proc.stdin.write(json.dumps(request) + "\n")
        self.proc.stdin.flush()
        response = self.proc.stdout.readline().strip()
        return json.loads(response)
