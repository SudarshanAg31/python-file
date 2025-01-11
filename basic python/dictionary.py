# dictionary: a collection of {key:value} paire
#            ordered and changeable. No duplicates

marks={"sudarshan":43,
       "tanvi":54,
       "shriyansh":65,
       "love":12}
#it print all the keys of marks
for i in marks.keys():
    print(i) 
#------------or--------------
for i in marks:
    print(i)
#it print all the value of marks
for i in marks.values():
    print(i) 
#it print all the item present in the dictionary of marks
for i,j in marks.items():
    print(i,j) 
    
# it use to update our dictionary
# marks.update({"dhruv":32})

#it use to delete item for dictionary
#marks.pop("love")

#it delete last item form dictionary
#marks.popitem()

#it print the value if we pass the key
#print(marks.get("sudarshan"))
