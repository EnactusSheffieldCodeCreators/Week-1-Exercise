# THIS IS TERRIBLE CODE, DO NOT COPY ANY ASPECT OF THIS!!!
# Read README.md before tackling this code.

input_number = 600851475143
prime_factors = []
current_prime = 2

while True:
    # Breaks out of loop when the value of input_number is prime.
    if input_number==current_prime:
        input_number = 0
        prime_factors.append(current_prime) # Append current_prime to the list of prime factors.
        break

    # Checks if the current value of current_prime is a factor of input_number.
    # Loops until it has removed all the factors with the value current_prime.
    while (input_number/current_prime).is_integer():
        prime_factors.append(current_prime) # Append current_prime to the list of prime factors.
        input_number = int(input_number/current_prime) # Divide input_number by the prime factor.

    # Advances current_prime to the next prime number.
    while True:
        current_prime += 1

        pri = True # Value to be flipped to false if the number isn't prime.

        # Actual prime checking code.
        for i in range(2, current_prime):
            # Checking if any of the numbers between 2 and 1-current_prime are factors, 
            # if that is the case then the number can't be prime.
            if (current_prime/i).is_integer():
                pri=False
                break
        
        # Break out of while loop on line 21 if the value of current_prime is prime.
        if pri == True:
            break

# Print out the largest value of the list of primes.
print(max(prime_factors))
        