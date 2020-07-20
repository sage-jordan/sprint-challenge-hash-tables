#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # restructure tickets with dict comprehention
    tickets = {x.source:x for x in tickets}

    route = []
    
    # set current 
    current = tickets["NONE"]

    while current.destination != "NONE":
        route.append(current.destination)
        current = tickets[current.destination]

    route.append(current.destination)
    return route