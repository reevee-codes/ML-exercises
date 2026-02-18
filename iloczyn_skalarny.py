def dot_product(first: list, second: list) -> float:
    result = 0
    for x in range(len(first)):
        result += first[x] * second[x]
    return result

print(dot_product([1, 2, 3], [4, 5, 6]))

# [1,2,3] · [4,5,6] = 1*4 + 2*5 + 3*6 = 32
