'''
task = produce list of fibonacci numbers of length n

DIFFICULTY = EASY
TOPICS = lists, variables, loops

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''

def produceFibsList(n):
    '''
    >>> produceFibsList(0)
    []
    >>> produceFibsList(1)
    [1]
    >>> produceFibsList(2)
    [1, 1]
    >>> produceFibsList(3)
    [1, 1, 2]
    >>> produceFibsList(5)
    [1, 1, 2, 3, 5]
    '''
    numbersList = [1 , 1]
    num = 1
    k = 0

    if (n == 0):
        numbersList = []    
    if (n == 1):
        numbersList = [1]
 
    else:
        while (k < n):
            if (k >= 2):
                numbersList.append (numbersList[k - 1] + numbersList [k - 2])

            k = k + 1             
              
           
    return numbersList
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
