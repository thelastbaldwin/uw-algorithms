class Set():
        
    # Creates an empty set instance
    def __init__( self ):
        self.elements = list()

    # Returns the number of items in the set
    def __len__( self ):
        return len( self.elements)

    # Adds a new unique element to the set.
    def Add( self, element ):
        if element not in self.elements:
            self.elements.append(element)

    # Determines if this set is a subset of setB.
    def isSubsetOf( self, setB ):
        for element in self.elements:
            if element not in setB:
                return False
        return True

    def __str__(self):
        return '[%s]' % ', '.join(map(str, self.elements))

    def __iter__(self):
        return (x for x in self.elements)

# create first set
set = Set()
set.Add(2)
set.Add(4)
set.Add(3)
set.Add(2)


# create second set
set2 = Set()
set2.Add(2)
set2.Add(3)

# check if the second set is a subset of the first
print(set2.isSubsetOf(set))
print(set.isSubsetOf(set2))
