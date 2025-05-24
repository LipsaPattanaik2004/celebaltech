def lower_triangular(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()

def upper_triangular(n):
    for i in range(n):
        for j in range(n - i):
            print("*", end=" ")
        print()

def pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))


size = 5

print("Lower Triangular:")
lower_triangular(size)
print("\nUpper Triangular:")
upper_triangular(size)
print("\nPyramid:")
pyramid(size)
