def success(message, data=None):
    return {"status": True, "message": message, "data": data}

def error(message):
    return {"status": False, "message": message}
