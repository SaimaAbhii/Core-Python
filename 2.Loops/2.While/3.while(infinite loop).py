# Infinite Loops with Conditional Exit
# Sometimes, you might want to create a loop that runs indefinitely until a certain condition is met.
# You can achieve this by setting the loop condition to True and using break to exit when necessary.

while True:
    name=input("enter name ")
    if name.lower()=="abhii":
        print(f"Welcome {name}")
        break



