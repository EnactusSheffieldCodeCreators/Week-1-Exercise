# Week-1-Exercise

## Solution

Please note that all of the solutions here are a personal choice, you may have something different that could be entirely valid. These are just examples of good practice while coding, as long as what you write makes it easier for others to understand that's good enough.

### Comments

First step is to decode what's actually going on in the code so commenting what each bit is doing is a helpful first step.

```python
n = 600851475143 # Input value.
pn = [] # Array to hold list of primes.
c = 2 # Current prime value.

while True:
    # Breaks out of loop when the value of n is prime.
    if n==c:
        n = 0
        pn.append(c) # Append c to the list of prime factors.
        break

    # Checks if the current value of c is a factor of n.
    # Loops until it has removed all the factors with the value c.
    while (n/c).is_integer():
        pn.append(c) # Append c to the list of prime factors.
        n = int(n/c) # Divide n by the prime factor.

    # Advances c to the next prime number.
    while True:
        c += 1

        pri = True # Value to be flipped to false if the number isn't prime.

        # Actual prime checking code.
        for i in range(2, c):
            # Checking if any of the numbers between 2 and 1-c are factors, 
            # if that is the case then the number can't be prime.
            if (c/i).is_integer():
                pri=False
                break
        
        # Break out of while loop on line 21 if the value of c is prime.
        if pri == True:
            break

# Print out the largest value of the list of primes.
print(max(pn))
```

This is massively over commented but hopefully it goes into enough detail that you can get an idea of what's going on here.

### Variable Names

Currently we have names such as n, c and pn all of which are super unhelpful, so let's change that.

```python
input_number = 600851475143
prime_factors = []
current_prime = 2
```

Renaming these variables like this we can get rid of the comments as they don't really need to be there. This should be the objective of variable names, make the name as self explanatory as possible. Also take note of the use of `joined_lower` for the variable names, this is standard practice for naming instance variables in python.

### Break Condition

For this bit let's focus on a specific section of the code:

```python
# Breaks out of loop when the value of input_number is prime.
if input_number==current_prime:
    input_number = 0
    prime_factors.append(current_prime) # Append current_prime to the list of prime factors.
    break
```

This section breaks out of the loop when the `input_number` is reduced to a prime because we know we are done at that point and can just take that prime to be the last prime factor. So here's how we improve this code:

```python
    # Breaks out of loop when the value of input_number is prime.
    if input_number == current_prime:
        prime_factors.append(current_prime)
        break
```

This bit is already pretty clean here's a list of what changed:
- Added spaces between variables and `==` on the if line to make it easier to read.
- Removed useless line that sets `input_number` to 0, it isn't needed as we never use `input_number` again
- Removed comment on the line where the prime is appended to the list `prime_factors` as the code is now self explanatory enough.

### Prime Removal Loop

```python
# Checks if the current value of current_prime is a factor of input_number.
# Loops until it has removed all the factors with the value current_prime.
while (input_number/current_prime).is_integer():
    prime_factors.append(current_prime) # Append current_prime to the list of prime factors.
    input_number = int(input_number/current_prime) # Divide input_number by the prime factor.
```

This section is mostly ok with the improved variable names, just needs some comments pruning.

```python
# Loops until it has removed all the prime factors of input_number 
# with the value current_prime.
while (input_number/current_prime).is_integer():
    prime_factors.append(current_prime) 
    input_number = int(input_number/current_prime) 
```

### Prime Advance Loop

```python
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
```

This is way too unwieldy so let's abstract it out to a function to clean up the loop within a loop within a loop that we've got going on here.

```python
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
```

Here I've actually broken it down into 2 functions just to make the functionality clearer. We only need to call the `advance_prime` function to get to the next prime within the main loop.

```python
current_prime = advance_prime(current_prime)
```

## Errors

If you've layed around with the code you may have noticed that the code will enter an endless loop if you happen to input a value like `4`. And you'll need to ctrl+c to exit the program at that point. This is because when there is a number with more than 1 of the same prime factor the program misses the break condition and loops forever.

The solution to this is to change the break condition.

```python
while True:
    # Loops until it has removed all the prime factors of input_number 
    # with the value current_prime.
    while (input_number/current_prime).is_integer():
        prime_factors.append(current_prime) 
        input_number = int(input_number/current_prime) 
        if input_number == 1:
            break

    current_prime = advance_prime(current_prime)

    if input_number == 1:
        break
```

This way we even manage to reduce the amount of repeated code. Although we still have a repeated if condition, we can again reduce this out with some careful restructuring of the surrounding code.

```python
while True:
    # Checks if current_prime is a factor of input_number
    if (input_number/current_prime).is_integer():
        prime_factors.append(current_prime) 
        input_number = int(input_number/current_prime) 
    else: # Advances to the next prime if current_prime isn't a factor
        current_prime = advance_prime(current_prime)

    if input_number == 1:
        break
```

And this way we actually manage to get rid of the nested loops from before. 

Finally we can actually remove the break condition and integrate it as part of the while loop.

```python
while input_number != 1:
    # Checks if current_prime is a factor of input_number
    if (input_number/current_prime).is_integer():
        prime_factors.append(current_prime) 
        input_number = int(input_number/current_prime) 
    else: # Advances to the next prime if current_prime isn't a factor
        current_prime = advance_prime(current_prime)
```

# Final Note

Don't worry if all the changes here didn't make sense we will be covering all this material in the following weeks in far greater detail.