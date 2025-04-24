# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Set difference (set1 - set2)
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# Symmetric difference (items in either set, but not in both)
symmetric_diff = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_diff)

# Clear a set (removes all elements)
set1.clear()
print("Set1 after clearing:", set1)
