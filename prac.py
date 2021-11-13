"""Lists"""
# list=["one","Two"]
"""Dictionary"""
# fib={1:1,2:1,3:2,4:3}

# print(fib.get(4, 0))
# print(fib.get(7, 5))

# print(fib.get(4, 0) + fib.get(7, 5))

"""Tuples"""
# words=("tuples","are","immutable","similar","to lists")

# print(words[0])
# words[1]="try to change causes type error"

# tuple_without_parantheses="tuples","tuples","tuples","tuples"
# empty_tpl=()
#faster than list but cannot be changed
"""List Slicing"""
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])   #[4, 9, 16, 25]
print(squares[3:8])   #[9, 16, 25, 36, 49]
print(squares[0:1])   #[0]
print(squares[:7])    #[0, 1, 4, 9, 16, 25, 36]
print(squares[7:])    #[49, 64, 81]
print(squares[2:8:3]) #[4, 25]
print(squares[1::4])  #[1, 25, 81]
print(squares[1:-1])