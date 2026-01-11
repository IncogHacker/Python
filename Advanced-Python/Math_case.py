


def status(value):

    match value:

        case 200:
            return "SuccessFull"
            

        case 404:
            return "Not Found"
            

        case 500:
            return "Server Error"
            

        case _:
            return "Unknown Status"
            

    
print(status(200))
print(status(404))
print(status(500))
print(status(2323))