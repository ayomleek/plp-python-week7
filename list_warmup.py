"""Part A - List Warmup: index access, append, remove and len."""

# 1. Create a list of four fruits
fruits = ["apple", "banana", "mango", "orange"]

# 2. Print the first and last item using indexes
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. Append a fifth fruit and print the whole list
fruits.append("grape")
print("After append:", fruits)

# 4. Remove one fruit and print the list again
fruits.remove("banana")
print("After remove:", fruits)

# 5. Print how many fruits remain
print("Fruits remaining:", len(fruits))