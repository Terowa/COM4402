def multiplication_table(n):
    table = []
    if n < 0:
        raise ValueError
    elif type(n) != type(0):
        raise TypeError
    else:
        for i in table:
            result = n * i
            table.append(result)
    return table



multiplication_table(1)