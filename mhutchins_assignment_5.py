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

print('=== Challenge 2: Prime Number Checker ===')
prime_num = int(input("Enter a number: "))
print(f'Testing divisors from 2 to {prime_num - 1}...')
is_prime = ""
count = 2
if prime_num > 1:
    i = 2
    for i in range(2, prime_num-1):
        if prime_num % i == 0:
            is_prime = False
            count += 1
            break
        else:
            is_prime = True
if is_prime:
    print(prime_num, 'is prime!')
else:
    print(f'{prime_num} is not prime (divisible by {count})')