count = 1
total = 0

# BUG: The while statement was missing a colon (:), which caused a syntax error.
while count < 6:
    total = total + count

    # BUG: The original condition was count < 5, which stopped the loop before
    # adding 5. I changed it to count < 6 so that 5 is included.
    count = count + 1

# BUG: The original code tried to concatenate a string with an integer.
# I changed it to an f-string so that total can be displayed correctly.
print(f"Sum of 1 to 5 is: {total}")