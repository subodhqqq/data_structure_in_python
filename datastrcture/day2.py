#touple
# -> touples are used to store multiple items in a single variable

# -> A tuple is a collection which is ordered and unchangeable
# -> touple can not access nested properities

# example of touple
touple=(1,2,3,"subodh")
print(touple)


# ->Tuple items are ordered, unchangeable, and allow duplicate values
# 1.ordered
# ->When we say that tuples are ordered, it means that the items have a defined order, and that order will not change
# 2.Unchangeable
# -> Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created like append del method are not work
# 3.Allow Duplicates
# -> Since tuples are indexed, they can have items with the same value
touple(0)=6 # this line is erorr shows-> SyntaxError: cannot assign to function call


# Tuple Length
# ->o determine how many items a tuple has, use the len() function
print(len(touple))


#The tuple() Constructor
# -> It is also possible to use the tuple() constructor to make a tuple.
touple = tuple(("apple", "banana", "cherry"))
print(touple)
