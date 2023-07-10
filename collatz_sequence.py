def collatz_sequence(n):
    sequence = [n]  # Initialize the sequence with the starting number

    while n != 1:
        if n % 2 == 0:  # If n is even
            n = n // 2
        else:  # If n is odd
            n = 3 * n + 1

        sequence.append(n)  # Add n to the sequence

    return sequence

# Example usage:
try:
    number = int(input("Enter a number: "))
    if number <= 0:
        raise ValueError("Input must be a positive integer greater than zero.")

    sequence = collatz_sequence(number)
    print(*sequence)  # Print the sequence elements separated by a space

except ValueError as e:
    print("Invalid input:", e)