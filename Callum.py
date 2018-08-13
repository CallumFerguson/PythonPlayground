

#determine if a box with width and height at a specific x is valid
def checkBox(x, width, height, array):
    for i in array[x : x + width]:
        if i < height:
            return False
    return True

#finds the largest box at any x with a specific width in an array
def largestBoxWithWidth(width, array):
    largestFoundBox = 0
    for height in range(0, max(array) + 1):
        for i in range(0, len(array) - width + 1):
            if checkBox(i, width, height, array):
                if width * height > largestFoundBox:
                    largestFoundBox = width * height
    return largestFoundBox

#finds the largest box at any x and with any width or height in an array
def largestBox(array):
    largestFoundBox = 0
    for i in range(1, len(array)):
        if largestBoxWithWidth(i, array) > largestFoundBox:
            largestFoundBox = largestBoxWithWidth(i, array)
    return largestFoundBox


print(largestBox([2, 1, 5, 6, 2, 3]))