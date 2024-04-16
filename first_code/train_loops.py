# for i in range(0, 10, 2):
#     print(i)

# for i in range(1, 4, 1):
#     for j in range(1, 4, 1):
#         print(i, j)


# new_word = 'geeksforgeeks'

# for letter in 'geeksforgeeks':
#     if letter == 'e' or letter == 's':
#         continue
#     print('Current letter :', letter)

# new_word = 'geeksforgeeks'
# for letter in new_word:
#     if letter == 'e' or letter == 's':
#         break
#     print('Current Letter :', letter)

# sum = 0
# for i in range(1, 10):
#     sum += i
#     print(i, end=" ")
# print("\nSum of first 10 numbers :", sum)

# ex1
def is_prime(n: int) -> bool:
    for i in range(2, n + 1):
        if n % i == 0:
            return False
        return True

print(is_prime(7))

def nth_fibonacci(n: int) -> int:
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

print(nth_fibonacci(9))

def factorial(n: int) -> int:
    if n < 0:
        print("Invalid input")
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

def count_vowels(s: str) -> int:
    VOWELS = {'a', 'e', 'o', 'u', 'i'}
    count = 0
    for letter in s:
        if letter in VOWELS:
            count += 1
    return count

print(count_vowels("hello"))

#ex 5
def sum_digits(n: int) -> int:
    count = 0
    while n != 0:
        n = n // 10
        count += 1
    return count

print(sum_digits(12345))    

#ex7
def sum_of_squares(n: int) -> int:
    sum = 0
    for i in range(1, n + 1):
        square = i * i
        sum += square
    return sum

print(sum_of_squares(5))

#ex10
def count_words(s: str) -> int:
    words = s.split()
    num_words = len(words)

    return num_words

print(count_words("Hello My World"))

def is_palindrome(s: str) -> bool:
    new_word = s[::-1]
    if s == new_word:
        return True
    return False

print(is_palindrome("aradara")) 

def sum_of_multiples(n: int, x: int, y: int) -> int:
    sum = 0
    for i in range(1, n + 1):
        if i % x == 0 or i % y == 0:
            sum += i
    
    return sum

print(sum_of_multiples(10, 3, 5))

def count_character(s: str, c: str) -> int:
    count = 0
    for char in s:
        if char == c:
            count += 1

    return count 

print(count_character("hello worlld", 'l'))


    











