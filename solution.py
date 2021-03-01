# THIS IS TERRIBLE CODE, DO NOT COPY ANY ASPECT OF THIS!!!
# Read README.md before tackling this code.

input_number = 600851475143
prime_factors = []
current_prime = 2

def check_if_prime(number):
    # Loop over numbers from 2 up to half the value of "number".
    for i in range(2, int(number/2)):
        if (number/i).is_integer():
            return False # If the number is divisible, it is not a prime.
    return True

# Advance a number to the next prime.
def advance_prime(prime):
    while True:
        prime += 1

        if check_if_prime(prime):
            return prime

while input_number != 1:
    # Checks if current_prime is a factor of input_number
    if (input_number/current_prime).is_integer():
        prime_factors.append(current_prime) 
        input_number = int(input_number/current_prime) 
    else: # Advances to the next prime if current_prime isn't a factor
        current_prime = advance_prime(current_prime)

# Print out the largest value of the list of primes.
print(max(prime_factors))
