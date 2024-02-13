# processing time of array increses as array size increases

def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers


numbers = [2,5,8,9]
print(get_squared_numbers(numbers))