# Define a function named recursive_list_sum that calculates the sum of elements in a nested list
def recursive_list_sum(data_list):
    # Initialize a variable 'total' to store the cumulative sum
    total = 0

    # Iterate through each element in the input list
    for element in data_list:
        # Check if the current element is a list (nested list)
        if type(element) == type([]):
            # If the element is a list, recursively call the recursive_list_sum function on the element
            total = total + recursive_list_sum(element)
        else:
            total = total + element
    return total
print(recursive_list_sum([1, 2, [3, 4], [5, 6]]))