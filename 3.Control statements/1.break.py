# The break statement is used to exit or terminate a loop prematurely. When encountered within a loop, the break
# statement immediately terminates the loop's execution and resumes execution at the next statement after the loop.

numbers = [1, 3, 5, 8, 9, 11]
i=0
while i<len(numbers):
# for num in numbers:
    if numbers[i] % 2 == 0:
        print("First even number found:", numbers[i])
        break
    i+=1
