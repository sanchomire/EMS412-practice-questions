def sum_to_n():
    start = 5
    end = 20
    step = 1
    sum = 0
    for r in range(start, end+1, step):
        sum = sum + 15*r**3 + 2*r**2 + 3
    return sum
print(sum_to_n())

