print('=== Challenge 1: Collatz Conjecture ===')
current_number = int(input("Enter starting number: "))
step_count = 0
sequence = []

print('Sequence:', current_number, end=" ")
while current_number != 1 and current_number > 0:
    if current_number % 2 == 0:
        current_number //= 2
        sequence.append(current_number)
    else:
        current_number = current_number * 3 + 1
        sequence.append(current_number)
    print(current_number, end=" ")
    step_count += 1
print("\nSteps:", step_count)
print()
