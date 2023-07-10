def collatz_sequence(number):
    sequence = [number]  # Initialize the sequence with the starting number

    while number != 1:
        if number % 2 == 0:  # If n is even
            number = number // 2
        else:  # If n is odd
            number = 3 * number + 1

        sequence.append(number)  # Add number to the sequence

    return sequence

try:
    number = int(input("Enter a number: "))
    if number <= 0:
        raise ValueError("Input must be a positive integer greater than zero.")

    sequence = collatz_sequence(number)
    print(*sequence)  # Print the sequence elements separated by a space

except ValueError as e:
    print("Invalid input:", e)