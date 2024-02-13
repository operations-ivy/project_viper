def make_even(num):
    if num%2 == 1:
        return num+1
    else:
        return num
    
x = [233, 375, 931, 141, 779, 395, 675, 811, 403, 555]

y = list(map(make_even, x))
y2 = [make_even(num) for num in x]

print(y)

if y == y2:
    print('it worked')