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

# Break Condition

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