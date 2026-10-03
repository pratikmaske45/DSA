N = 5
# Top half
for i in range(1, N + 1):
    print(" " * (N - i) + "*" + (" " * (2 * i - 3) if i > 1 else "") + ("*" if i > 1 else ""))

# Bottom half
for i in range(N - 1, 0, -1):
    print(" " * (N - i) + "*" + (" " * (2 * i - 3) if i > 1 else "") + ("*" if i > 1 else ""))
