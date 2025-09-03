import datetime

def ping(params):
    return "pong"

def getTime(params):
    return {"now": datetime.datetime.now().isoformat()}