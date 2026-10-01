"""Part C - List Report: numbering, counting and finding the longest name."""

items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# 1. Print each item numbered
print("Shopping list:")
number = 1
for item in items:
    print(f"{number}. {item}")
    number += 1

# 2. Count items with more than 4 letters
long_count = 0
for item in items:
    if len(item) > 4:
        long_count += 1
print(f"\nItems with more than 4 letters: {long_count}")

# 3. Find the longest item name using a loop comparison
longest = items[0]
for item in items:
    if len(item) > len(longest):
        longest = item
print(f"Longest item name: {longest}")