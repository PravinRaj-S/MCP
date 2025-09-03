import sys
import json
from handlers import ping, getTime

# Available methods
METHODS = {
    "ping": ping,
    "getTime": getTime
}

def send(msg):
    sys.stdout.write(json.dumps(msg) + "\n")
    sys.stdout.flush()

def main():
    for line in sys.stdin:
        try:
            req = json.loads(line)
            method_name = req.get("method")
            if method_name in METHODS:
                result = METHODS[method_name](req.get("params", {}))
                send({"jsonrpc": "2.0", "id": req["id"], "result": result})
            else:
                send({
                    "jsonrpc": "2.0",
                    "id": req.get("id"),
                    "error": {"code": -32601, "message": "Method not found"}
                })
        except Exception as e:
            send({
                "jsonrpc": "2.0",
                "id": req.get("id") if "req" in locals() else None,
                "error": {"code": -32000, "message": str(e)}
            })

if __name__ == "__main__":
    main()
