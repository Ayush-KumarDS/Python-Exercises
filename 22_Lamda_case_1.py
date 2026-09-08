add = lambda x,y: x+y
print(add (4,9,))

# map function :- applies function to each iterable items
numbers = [1,2,3,4,5,6,7]
Squares = map(lambda x: x**2,numbers)
print(list(Squares))

#filter ( ) 
numbers= [1,4,5,6,8,6,7]
even_list = filter(lambda x: x%2==0,numbers)
print(list(numbers))

# reduce () :- reduces an iterablw to a single value

from functools import reduce
numbers = [1,5,6,7,33,4,3,4,6,]
product = reduce(lambda x,y: x*y, numbers)
print(product)