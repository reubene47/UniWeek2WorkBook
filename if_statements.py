# book = input("Enter type of book: ").lower()

# if book == "adventure":
#     print("I like adventure books!")
# else:
#     print("Finished reading book.")

# activity = input("Please enter the activity to be performed: ").lower()

# if activity == "calculate":
#     print("Performing calculations...")
# else:
#     print("Performing activity...")

# print("Activity completed!")

# while True:
#     direction = input("Towards which direction should I go (up, down, left or right)?: ").lower()

#     if direction == "up":
#         print("I am moving in an upward direction!")
#     elif direction == "down":
#         print("I am moving in a downward direction!")
#     elif direction == "left":
#         print("I am moving to the left!")
#     elif direction == "right":
#         print("I am moving to the right!")

num = int(input("Please enter a whole number: "))

# work out if code is odd or even
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")