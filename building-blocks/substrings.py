def substrings(string, dictionary):
    words = string.split()
    frequencies = {}
    for i in words:
        for x in range(len(i)):
            count = 1
            while x + count <= len(i):
                substring = i[x:x + count].lower()
                if substring in dictionary:
                    if frequencies.get(substring) is None:
                        frequencies[substring] = 1
                    else:
                        frequencies[substring] += 1
                count += 1
    print frequencies
