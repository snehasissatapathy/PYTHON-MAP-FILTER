"""
## 1. Square the Even Numbers  *(Easy)*

=================================================
SQUARE EVEN NUMBERS WITH MAP & FILTER
=================================================

Problem Statement:
Write a Python program that takes a list of
integers and returns a NEW list containing
the SQUARES of only the EVEN numbers from the
original list.

You MUST solve this using:
   - filter() with a lambda
   - map()    with a lambda


-------------------------------------------------
Input Example 1:
[1, 2, 3, 4, 5, 6]

Output Example 1:
Squared Evens: [4, 16, 36]

-------------------------------------------------
Input Example 2:
[7, 9, 11]

Output Example 2:
Squared Evens: []

-------------------------------------------------
Explanation:
For [1, 2, 3, 4, 5, 6]:
   filter (even)  -> [2, 4, 6]
   map    (n*n)   -> [4, 16, 36]
=================================================

"""
def even_squares(numbers):
    return list(
        map(
            lambda x: x ** 2,
            filter(lambda x: x % 2 == 0, numbers)
        )
    )
nums = [1, 2, 3, 4, 5, 6, 7, 8]
result = even_squares(nums)

print(result)