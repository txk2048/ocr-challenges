def generate_permutations(array):
    # see https://en.wikipedia.org/wiki/Heap%27s_algorithm

    stack = [0 for _ in range(len(array))]
    permutations = [array.copy()]

    i = 0
    while i < len(array):
        if stack[i] < i:
            if i % 2 == 0:
                array[0], array[i] = array[i], array[0]
            else:
                array[stack[i]], array[i] = array[i], array[stack[i]]

            permutations.append(array.copy())
            stack[i] += 1
            i = 0
        else:
            stack[i] = 0
            i += 1

    return permutations
