#program for adding 'ing' at end of the given verbs

verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"] #given verbs
ing= []    # creating a varaible and declaring as empty list 
for i in range(len(verbs)):  # using the range function and len to count the length of the list
    ing.append(verbs[i]+'ing') #using append function to add 'ing' at the end of every word in the list
print(ing)