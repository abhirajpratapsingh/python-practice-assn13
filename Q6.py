# Q 6. Write a python program to append elements from another list to the current list.(
#      firstlist = ["Java", "Python", "SQL"]
#      secondlist = ["C", "Cpp", "NoSQL"] )

firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
print ( 'list-1 = {}\nlist-2 = {}\nappend the elements form list-1 to list-2' . format ( firstlist , secondlist ) )
for element in firstlist : secondlist . append ( element )
print ( 'list-2 =' , secondlist )