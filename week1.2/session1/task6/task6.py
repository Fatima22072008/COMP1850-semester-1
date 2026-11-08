# Week 1.2, Session 1: Task 6
"""
in this task we are creating a music database (using a dictionary), 
where the keys are artists and the values are album names
We are gonna import pretty print to then output certain parts of the dictionary using it
"""
from pprint import pprint # allows to import pretty print 

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music = {
    "Ariana Grande": ["Sweetner","Petal"],
    "Olivia": "Sour"
}

# Pretty-print the data structure
pprint(music)
print(music)

# Display details of one album recorded by a specific artist
album = music.get("Olivia")
print(album)