def intersection(arrays):
    result = 0
    cache = {}

    for array in arrays:
        for num in array:
            if num in cache:
                return cache[num]
            cache[num] = 

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
