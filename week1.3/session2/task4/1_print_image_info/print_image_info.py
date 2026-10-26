# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

with open("../images/gradient.pgm", "r") as infile:
    readFile = infile.read()
    value = readFile.split()
    width = int(value[1])
    height = int(value[2])
    greyValue = value[3]
    dimensions = (width * height)
    print(dimensions)
    print(max(greyValue))
# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)