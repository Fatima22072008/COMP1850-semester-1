# Week 1.2, Session 1: Task 5
"""
this is a dictionary which has values and keys (key-value pairs)
The keys are the words on the left which are the cities
The values are the rivers whcih are on the right
"""
rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}


# Add two new entries to the rivers database
print(rivers)
rivers["Dehli"] ="Ganga"
rivers["Dewsbury"] = "Calder"


# Display all the keys
print(rivers.keys())

# Display all the values
print(rivers.values())

# Display all the key:value pairs, as tuples
tupleRivers = tuple(set(rivers.items()))
print(tupleRivers)

# Delete an entry from the rivers database
rivers.pop("London")
print(rivers)