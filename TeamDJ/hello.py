'''
Created on 21.01.2013

@author: rekzah
'''

def iAmAFunction(argument):
    returnValue = 6
    print argument
    return returnValue 

if __name__ == '__main__':
    print 'hello world'
    
    # I am a one-line comment
    
    """
    I am a multi-line comment
    """
    
    # A simple for loop
    print range(10)
    for x in range(10):
        print x
    
    # A boolean variable
    janinaIsPretty = True
    
    
    # A basic if-then-else construct
    if janinaIsPretty:
        print 'Janina is very pretty indeed!'
    else:
        print 'Janina is not very pretty.'
        
    # Call a function
    returnVal = iAmAFunction(janinaIsPretty)
    print returnVal