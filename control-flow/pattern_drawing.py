positive_number = int(input("Enter the size of the pattern: "))
i = 1
while i <= positive_number:
    j = 1
    while j <= positive_number:
        print("*", end="")
        j += 1
    print()
    i += 1
