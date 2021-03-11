"""a horizontal line of ten stars"""
import random

print("a horizontal line of ten stars")
for i in range(10):
    print("*", end="")
print("")
print("____________________________________________________________")

# 10x10 square of stars
print("10x10 square of stars")
for i in range(10):
    for j in range(10):
        print("*", end="")
    print()
print("____________________________________________________________")
# an array of one hundred zeros
print("an array of one hundred zeros")
grid = []
for i in range(10):
    grid.append([])
    for j in range(10):
        grid[i].append(0)
    print(grid[i])
print("____________________________________________________________")
# a function that will display your favorite number
print("a function that will display your favorite number")


def my_favorite_num():
    """random num"""
    print("My favorite num is", random.randrange(100))


my_favorite_num()
print("____________________________________________________________")
# a function that takes three numbers and returns the arithmetic mean of those numbers.
print("a function that takes three numbers and returns the arithmetic mean of those numbers.")


def arithmetic(x_num, y_num, z_num):
    """arithmetic"""
    algorithm = (x_num + y_num + z_num) / 3
    print(f"The arithmetic mean of the numbers entered: {algorithm}")


arithmetic(1, 2, 3)
print("____________________________________________________________")

# Write the code for Ball class. Set it attributes for position and speed
# Create an update() method that moves the position on the ball relative to its speed
# Create an instance of the Ball class and set its attributes
# Create a for loop that will call the update() method on the ball 10 times,
# $and also output the position of the ball.
print("Write the code for Ball class. Set it attributes for position and speed")
print("Create an update() method that moves the position on the ball relative to its speed")
print("Create an instance of the Ball class and set its attributes")
print("Create a for loop that will call the update() method on the ball 10 times,")
print(" and also output the position of the ball.")


class Ball:
    """Class Ball"""
    pos = 1
    speed = 1

    def update(self):
        """update"""
        self.pos = self.pos + self.speed


Ball = Ball()
Ball.pos = 1
Ball.speed = 1
print(f"First Ball position :{Ball.pos}")
for i in range(10):
    Ball.update()
print(f"Ball position after update :{Ball.pos}")
print("____________________________________________________________")
# write the code for swapping the numbers 25 and 40
print("write the code for swapping the numbers 25 and 40")
list_first = [55, 41, 52, 68, 45, 27, 40, 25, 37, 26]
print(f"Unsorted list:{list_first}")
list_first[7], list_first[6] = list_first[6], list_first[7]
print(f"Sorted list:{list_first}")
print("____________________________________________________________")
# write the code for swapping the numbers 2 and 27
print("write the code for swapping the numbers 2 and 27")
list_second = [27, 32, 18, 2, 11, 57, 14, 38, 19, 91]
print(f"Unsorted list:{list_second}")
list_second[0], list_second[3] = list_second[3], list_second[0]
print(f"Sorted list:{list_second}")
print("____________________________________________________________")
# Show how the following list of numbers is sorted using the selection sort:
print("Show how the following list of numbers is sorted using the selection sort:")
