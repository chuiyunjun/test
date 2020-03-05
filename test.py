# for interview

# PS: there is no type of number -- 'double',  in python. I take 'float' instead.


''' Convert the format of dollars value into quote format.
By market convention, the normal fraction used for Treasury security prices is 1/32.
 A hyphen separates the full dollar portion of
the price from the 32nds of a dollar, which are to the right of the hyphen.
'''
class ThirtySecondsFormatter:
    
    def __init__(self, amount=0):
        '''constructor.  
        The <amount> is an optional parameter indicating the value of dollars.
        The default value of amount is 0.
        <amount> can be modified by set_amount()
        '''
        self.amount = amount
        
    def __str__(self):
        '''(ThirtySecondsFormatter) --> str
        Print final quote.
        '''
        integer, num_32nds = self.convert()
        result = integer.zfill(2) + "-" + num_32nds.zfill(2)
        return result
    
    def set_amount(self, amount):
        ''' (ThirtySecondsFormatter, int/float) --> Nonetype
        Set the value of input dollars.
        '''
        self.amount = amount
    
    
    def get_amount(self):
        ''' (ThirtySecondsFormatter) --> int/float
        Get the value of input dollars.
        '''  
        return self.amount
    
    
    def convert(self):
        ''' (ThirtySecondsFormatter) --> (str, str)
        Find the integer part of quote and the number of 32nds in fraction part.
        Convert them to string and return a tuple containing them
        '''
        integer = int(self.amount)
        fraction = self.amount - integer
        num_32nds = int(fraction * 32)
        integer = str(integer)
        num_32nds = str(num_32nds)
        return (integer, num_32nds)
    

if __name__ == "__main__":
    print("Initailize an instant with given dollar value")
    # given value of dollars. Initalize an instant. print the value
    # run the given sample in handout
    convertor = ThirtySecondsFormatter(105.25)
    print(convertor)
    convertor = ThirtySecondsFormatter(9 + 1/32)
    print(convertor)
    # the case where in fraction part, quote has more than 9 32nds
    convertor = ThirtySecondsFormatter(9.5)
    print(convertor)
     # the case where in fraction part, quote has 0 32nds
    convertor = ThirtySecondsFormatter(9)
    print(convertor)
    
    print('-----------------------------------------------------------')
    print("Initailize an instant without given dollar value. Then set the value later")
    # without value of dollars. Initalize an instant. Default value should be 0.
    convertor = ThirtySecondsFormatter()
    print(convertor)
    # set the dollars amount 
    convertor.set_amount(105.25)
    print(convertor)