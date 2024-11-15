#Avery multiplication table

# Part 1: Get multiples of a chosen number
number = int(input("Enter a number to see its multiples (0-12): "))

print(f"\nMultiples of {number} from 0 to 12:")
for i in range(13):
    print(f"{number} x {i} = {number * i}")

# Part 2: Print full multiplication table (Bonus)
print("\nFull Multiplication Table (0-12):\n")

# Print the header row
print("     |", end=" ")
for col in range(13):
    print(f"{col:3}", end=" ")
print("\n" + "-" * 50)

# Print each row of the table
for row in range(13):
    print(f"{row:3} |", end=" ")
    for col in range(13):
        print(f"{row * col:3}", end=" ")
    print()
