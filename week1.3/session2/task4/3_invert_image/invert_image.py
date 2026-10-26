# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except

with open("../images/feep.pgm", "r") as infile:
    readfile = infile.read()
    value = readfile.split()
    width = value[1]
    height = value[2]
    max_greyValue = int(max(value[3]))
    for x in value:
        original_pixel_value = x
    invert_pixel_value = max_greyValue - int(original_pixel_value)
    print(invert_pixel_value)

# Create inverted image
# the formula: invert_pixel_value = max_gray - original_pixel_value


# write the inverted pgm image to a new file.
# Remember to include:
# - the string `P2`
# - the width and height dimensions
# - maximum gray value
# - you could convert numbers in a list to strings and join them with spaces
#   for example line = [255, 255, 0, 255, 255]
#   string_line = " ".join(str(item) for item in line)
#   # output: string_line = "255 255 0 255 255"