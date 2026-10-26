# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except
with open("invalid_pixels.pgm", "r") as infile:
    readFile = infile.read()
    SplitFile = readFile.split()
    width = SplitFile[1]
    height = SplitFile[2]
    Max_Grey_Value = max(SplitFile[3])

    for value in SplitFile:
        if value >= 0 and value <= Max_Grey_Value:


# Read the file content

# Store the width, the height, and the maximum gray value

# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive

# Check if the widths and heights are the same as specified

# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value