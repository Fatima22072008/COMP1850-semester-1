
# function implementation
"""
this task calculate the area of a trinagle by taking into two inputs from the user and returning them
"""
def rectangle_area( ):  # define suitable input data
    length = int(input("enter the length"))
    width = int(input("enter the width")) 
        # implement the function
    return(length * width)           # return an appropriate value

# testing the function

print(f"Area is {rectangle_area()}")   # provide suitable data matching your inputs
