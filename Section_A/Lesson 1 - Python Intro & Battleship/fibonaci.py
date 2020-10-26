import itertools

# Prints out the fibonaci sequence a specified number of times
def fibonaci(n):
    num_one = 0
    num_two = 1
    current_num = 0
    for _ in itertools.repeat(None, n):
        print(current_num)
        current_num = num_one + num_two
        num_one = num_two
        num_two = current_num

fibonaci(10)