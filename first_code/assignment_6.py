#1 find sum
def find_sum(a: int, b: int) -> int:
    return a + b

print(find_sum(5, 4))

#2 reverse word
def reverse_word(input_word: str) -> str:
    new_word = input_word[::-1]
    return new_word

print(reverse_word("BAKO"))

#3 string-length
def find_length(city: str) -> int:
    count = len(city)
    return count

print (find_length("ASTANA"))

#4 concatenate-string
def concatenate_strings(s1: str, s2: str) -> str:
    return s1 + s2

print(concatenate_strings('big', 'city'))

#5 is-vowel
VOWEL = ['a', 'i', 'o', 'u', 'e']
def is_vowel(s: str) -> bool:
    if not s and len(s) > 1:
        return False
    if s in VOWEL:
        return True
    return False
    
print(is_vowel('a'))

#6 swap-first-last
def swap_characters(s: str) -> str:
    new_string = s[-1:] + s[1:-1] + s[:1]
    return new_string

print(swap_characters('nfactorial'))

#7 to-uppercase
def do_uppercase(s: str) -> str:
    return s.upper()

print(do_uppercase('hello'))

#8 rectangle-area
def find_rec_area(x: int, y: int) -> int:
    area = x * y
    return area

print(find_rec_area(4, 5))

#9 is even
def is_even(a: int) -> bool:
    if a % 2 == 0:
        return True
    return False

print(is_even(4))

#10 extract-first-three
def extract_first3_characters(s: str) -> str:
    return s[3:]

print(extract_first3_characters("status"))

#11 string-interpolation
def interpolate_strings(s1: str, s2: str) -> str:
    return f'{s1}, {s2}'

print(interpolate_strings('name', 'surname'))

#12 string-slicing
def slice_string(s: str) -> str:
    return s[:2] + s[-1:]

print(slice_string('country'))

#13 type-conversion
def convert_string(s: str) -> int:
    return int(s)

print(convert_string('123'))

#14 string-repetition
def repeat_string(s: str) -> str:
    return s * 3

print(repeat_string('city'))

#15 calculate-quotient-remainder
def calculate_quotient_remainder(a: int, b: int) -> int:
    quotient = a / b
    reminder = a % b
    return quotient, reminder

print(calculate_quotient_remainder(100, 3))

#16 float-division
def divide_float_numbers(a: int, b: int) -> float:
    return a / b

print(divide_float_numbers(25, 4))

#17 string-metods
def count_occurances(s: str) -> str:
    return s.count('_')

print(count_occurances('my_name_is'))

#18 escape-sequences
def escape_seq(s: str) -> str:
    new_string = "school name is \"Nfactorial\""
    return new_string

print(escape_seq('school name is "Nfactorial"'))

#19 multi-line-string
def use_slash(s: str) -> str:
    return "-how are you?\n-I'm good, thank you!"

print(use_slash("-how are you?-I'm good, thank you!"))

#20 exponential
def find_the_power(a : int, b: int) -> int:
    return a ** b

print(find_the_power(5, 2))

#21 exponential 
def is_palindrome(s: str) -> bool:
    is_palindrome = s == s[::-1]
    return is_palindrome

print(is_palindrome('radar'))

#22 check-anagrams
def is_anagrams(s1: str, s2: str) -> str:
    if sorted(s1) == sorted(s2):
        return True
    return False

print(is_anagrams('spar', 'rasp'))