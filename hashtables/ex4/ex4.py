
def has_negatives(a):
    result = []
    cache = {}
    # print("result: ",result)
    for num in a:
        if num < 0:
            cache[num] = 0
        else:
            cache[num] = 1
    for value in cache:
        # print(value)
        if -value in cache and value > 0:
            result.append(value)
    # print(result)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
