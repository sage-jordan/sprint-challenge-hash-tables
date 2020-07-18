#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    cache = {}
    route = [None] * length

    for i in range(length):
        source = tickets[i].source
        destination = tickets[i].destination
        # if this pair isn't stored
        if source is not None:
            if source not in cache:
                # store it
                cache[source] = destination
        else:
            route.append(source)
            route.append(destination)
            while destination in cache:
                route.append(cache[destination])
                destination = cache[destination]
            if destination is not None:
                if source not in cache:
                    # store it
                    cache[source] = destination
            else:
                route.append(source)

    return route
