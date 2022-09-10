# Q 10. Write a Python script to create a list, where each element of the list is a digit of a
#       given number

take_num , list = input ( 'enter any number :' ) , [ ]
for element in take_num : list . append ( int ( element ) )
print ( 'List =' , list )