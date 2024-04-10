''' Write a function that take number argument and calculate cube of it.
If there is no value passed when the function is called, then
it should calculate cube of 2.'''

def cube(num = 2):
    cube = num ** 3
    return f"Cube of {num} is {cube}. "

num = int(input("Enter the number, you want the cube of : "))
print(cube(num))
print(cube())
