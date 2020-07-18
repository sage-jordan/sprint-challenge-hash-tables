
def get_indices_of_item_weights(weights, length, limit):

    cache = {}
    # iterate over list
    for i in range(length):
        # print(i)
        number = weights[i]
        # calculate weight needed
        weightNeeded = limit - number
        # if this value isn't in our cache
        if weightNeeded not in cache:
        # add this num:i to cache
            cache[number] = i
            # print(cache)
            continue
        # if value needed is in cache, return these indexes
        weightNeeded = cache[weightNeeded]
        if i < weightNeeded:
            return (weightNeeded, i)
        else:
            return (i, weightNeeded)
    return None