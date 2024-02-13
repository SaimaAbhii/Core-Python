# The continue statement is used to skip the rest of the code inside a loop for the current iteration
# and continue with the next iteration. Unlike break, continue does not terminate the loop; instead,
# it skips the current iteration and continues with the next iteration.

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print("Odd number:", i)
