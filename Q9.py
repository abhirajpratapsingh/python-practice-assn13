# Q 9. Write a Python script to create a list of city names taken from the user.

list = [ ]
for element in range ( 1 , int ( input ( 'enter the numbers of elements you want to in list :' ) ) + 1 ) :
    print ( 'enter the' , element , 'city name :' )
    take_element = ( input ( ) )
    list . append ( take_element )
print ( 'list =' , list )