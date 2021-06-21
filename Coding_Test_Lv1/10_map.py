a, b = map(int, input().strip().split(' '))
def print_stars(a, b):
    while b >= 1:
        print("*"*a)
        b -= 1
print_stars(a,b)

a, b = map(int, input().strip().split(' '))
for i in range(b):
    print("*"*a, end="")
    print("")