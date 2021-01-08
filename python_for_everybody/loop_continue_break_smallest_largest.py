'''
5.2 Write a program that repeatedly prompts a user for integer numbers until the user
enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with a try/except and put
out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the
output below.
'''

def find_largest_smallest(arr):
    largest = -1
    smallest = None
    # print(arr)
    for i in arr:
        if smallest is None:
            smallest = i
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
    return largest, smallest



arr = []
while True:
    num = input("Enter a number: ")

    try:
        if num == "done":
            break
        else:
            num = int(num)
            arr.append(num)
    except:
        print('Invalid input')

largest, smallest = find_largest_smallest(arr)

print("Maximum is", largest)
print("Minimum is", smallest)