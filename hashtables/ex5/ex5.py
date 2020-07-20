# Your code here


def finder(files, queries):
    result = []
    cache = {}
    for path in files:
        if path in cache:
            result.append(path)
            break
        pathSplit = path.split('/')        
        lastItem = pathSplit[len(pathSplit) - 1]
        if lastItem in queries:
            result.append(path)
            cache[path] = 1

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        '/bin/foo',
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
