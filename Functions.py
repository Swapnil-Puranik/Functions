#Task1
def greet_user(name):
    print("Hey ",name," hope you are having a great day!")

def add_numbers(a,b):
    return a+b

greet_user("Swapnil")
print("The sum of ", 5, " and ", 10, "is ",add_numbers(5,10))

print("-"*40 )
#Task 2 - Using Default Parameters
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

# Example usage:
describe_pet("Buddy")  # Default animal_type = dog
describe_pet("Whiskers", "cat")


print("-"*40 )

#Task 3 - Functions with Variable Arguments
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for item in ingredients:
        print(f"- {item}")

# Example usage:
make_sandwich("Lettuce", "Tomato", "Cheese")


print("-"*40)

#Task 4 - Understanding Recursion

# Factorial Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Fibonacci Function
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

num = 5
fib_n = 6
print(f"Factorial of {num} is {factorial(num)}.")
print(f"The {fib_n}th Fibonacci number is {fibonacci(fib_n)}.")

