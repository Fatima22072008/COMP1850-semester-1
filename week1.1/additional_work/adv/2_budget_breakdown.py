"""Advanced Task 2: Budget Breakdown
- Ask for three separate expense amounts (for example: travel, food, accommodation).
- Convert each input so you can add them together to get a total trip cost.
- Calculate the average spend per category and show each value with an f-string.
- Extension: format the totals so they always show two decimal places.
"""

travel_cost_input = int(input("Travel cost in pounds: "))
food_cost_input = int(input("Food cost in pounds: "))
accommodation_cost_input = int(input("Accommodation cost in pounds: "))

# TODO: calculate the total and the average spend per category
total_trip_cost = travel_cost_input + food_cost_input + accommodation_cost_input

# TODO: convert each value to a number type that supports decimals
# TODO: print the three costs, the total, and the average
print(f"this is your travel cost {travel_cost_input:.2f} this is your food cost {food_cost_input:.2f} this is your accomodation cost: {accommodation_cost_input:.2f} this is your total trip cost: {total_trip_cost:.2f}")


# Extension: format the totals to two decimal places
