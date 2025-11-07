n = int(input("Input a positive integer: "))

print(f"\nHere is the Collatz Trajectory of {n}")

print(f"{n} ", end = "")

i = 0
j = 0
g = 0

while True:
    
    if n > g:
        g = n
        j = i
    
    if (n % 2 != 0):
        n = 3*n + 1
    else:
        n = n / 2
        
    print(f"\u21D2  {int(n)} ", end = "")
    
    i = i + 1
    
        
    if n == 1:
        break

print(f"\n\nThe total number of steps it took: {i}")
print(f"\nThe highest number reached was {int(g)}, taking {j} steps")
