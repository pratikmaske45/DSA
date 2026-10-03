N = 5
for i in range(1, N + 1):
    for j in range(1, N + 1):
        # Print asterisk only on the boundaries
        if i == 1 or i == N or j == 1 or j == N:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
