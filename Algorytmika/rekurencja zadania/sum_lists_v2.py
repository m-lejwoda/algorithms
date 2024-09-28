def sum_lists_v2(tab):
    total = 0
    for i in tab:
        if type(i) == list:
            total += sum_lists_v2(i)
        if type(i) == int:
            total += i
    return total


tab = [1,2,[3,4],[5,6]]
print(sum_lists_v2(tab))