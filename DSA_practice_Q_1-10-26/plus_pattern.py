N = 7  
for i in range(1, N + 1):
    for j in range(1, N + 1):
        # Print asterisk at the middle row or middle column
        if i == (N // 2 + 1) or j == (N // 2 + 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
