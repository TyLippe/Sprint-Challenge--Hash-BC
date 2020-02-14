#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    #insert tickets into our ht
    for ticket in tickets:
        #using source as the key and dest as value
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    #set current location
    current_location = 'NONE'

    #insert ht into route
    for i in range(length):
        route[i] = hash_table_retrieve(hashtable, current_location)
        current_location = route[i]

    route.pop()

    return route
