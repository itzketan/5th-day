# A list of n integer values

price = [300, 600, 900, 1000, 1500, 1800, 2100]

print(price)

# Add an item in to the list (using function)

price.append(2400)

print(price) 

price.extend(price)

print(price)

print(price[3])

price.insert(3, 1200)

print(price)


# Delete (using function)


del price[0]
print(price)

price.pop()
print(price)

price.remove(900)
print(price)


# Store the Smallest number from the list to a variable
# Store the Largest number from the list to a variable

Low = min(price)
print("LOW", Low)

High = max(price)
print("HIGH", High)

# Create a tuple and print the reverse of the created tuple

my_info = ('A', 8177899637, 21, "ETC Engineer")
print(my_info)

my_info = tuple(reversed(my_info))
print(my_info)

# Create a tuple and convert tuple into list

Tuple = (22, 'K', 81, 91, 61, 71, 'e', 't')
List = list(Tuple)
print(List)
