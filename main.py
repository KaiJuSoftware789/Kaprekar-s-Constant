def main():

    KAPREKAR_CONSTANT = 6174

    while True:
        # Get user input
        num = int(input("Enter a four digit number with at least two different digits: "))
        print("\n")

        # Input checks
        if num < 1000 or num > 9999:
            print("Please enter a four digit number.")
            continue

        if len(set(str(num))) < 2:
            print("Please enter a number with at least two different digits.")
            continue

        # Break loop if input is valid
        break

    # Perform Kaprekar's routine
    steps = 0
    while num != KAPREKAR_CONSTANT:

        digits = str(num).zfill(4)

        big = int("".join(sorted(digits, reverse=True)))
        small = int("".join(sorted(digits)))

        result = big - small

        print(f"{big:04d} - {small:04d} = {result:04d}")
        steps += 1

        num = result

    # How many steps it took to reach 6174
    print(f"\nReached 6174 in {steps} steps.")


if __name__ == "__main__":
    main()