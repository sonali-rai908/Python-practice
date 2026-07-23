# It checks the value of a variable and executes the matching block of code.

def http_status(status):

    match status:
        case 200:
            return "OK"

        case 400:
            return "Not found"

        case 500:
            return "Internal server error"

        case _:
            return "Unknown status"

print(http_status(280))
