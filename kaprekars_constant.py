# Variable and list assignment
int_input = input("Enter a four-digit integer: ")
input_list = list(int_input)
iterations = 0
output_list = [int_input]
sum = 0

# If the user enters less than 4 digits, add placeholders to the front
while len(input_list) < 4:
    input_list.insert(0, '0')

# Check if the input has at least two different digits
if len(set(input_list)) < 2:
    print(f'{int_input} > 0')
    print(f"{int_input} reaches 0 via Kaprekar's routine in 1 iterations ")
else:
    # While loop computing the sums for Kaprekar's constant.
    while sum != 6174:
        # Sorting the input to find ascending and descending numbers
        ascending_sort = sorted(input_list)
        descending_sort = sorted(input_list, reverse=True)

        # Converting lists to integers
        ascending = int(''.join(ascending_sort))
        descending = int(''.join(descending_sort))

        # Calculating the sum
        sum = descending - ascending
        output_list.append(sum)

        # Preparing for the next iteration
        input_list = list(str(sum))

        # Ensure the input list has four digits
        while len(input_list) < 4:
            input_list.insert(0, '0')

        iterations += 1

    # Final print statements for Kaprekar's constant.
    output_list = [str(item) for item in output_list] 
    print(" > ".join(output_list))
    print(f"{int_input} reaches 6174 via Kaprekar's routine in {iterations} iterations ")
