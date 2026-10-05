# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)
rivers["Dehli"] ="Ganga"
rivers["Dewsbury"] = "Calder"

# Add two new entries to the rivers database

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