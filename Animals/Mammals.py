class Mammals:
    """
        A class used to represent an Animal
        ...

        Attributes
        ----------
        says_str : str
            a formatted string to print out what the animal says
        name : str
            the name of the animal
        sound : str
            the sound that the animal makes
        num_legs : int
            the number of legs the animal has (default 4)

        Methods
        -------
        printMembers(self)
            Prints the list of animals
        """

    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']
 
 
    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)