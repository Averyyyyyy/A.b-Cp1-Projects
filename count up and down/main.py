#avery count up and down

# Initialize a variable to track the current number
current = 0

# Initialize a flag to determine whether we're counting up or down
counting_up = True

# Loop until the count reaches 0 again after counting up to 20
while True:
    print(current)

    # Change the direction of counting when reaching 20
    if counting_up and current == 20:
        counting_up = False
    elif not counting_up and current == 0:
        break  # Exit the loop when back to 0

    # Update the counter
    current += 1 if counting_up else -1
