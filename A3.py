def sum_down(n):
    if n == 0:
        return 0
    return n + sum_down(n - 1)

input("Stack overflow - each call adds a frame to the stack, limit is 1000. Press Enter")
print(" sum_down(3) = 3 + 2 + 1 + 0 =", sum_down(3))
print(" sum_down(4) = 4 + 3 + 2 + 1 + 0 =", sum_down(4))

n = int(input("Enter a number ( try 5 or 6): "))
input("sum_down(n) = n + (n-1) + ... uses n frames. Press Enter ")
print(" sum_down("+ str(n) +") =", sum_down(n), " frames used:", n)
