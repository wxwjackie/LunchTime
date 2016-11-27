'''
Created on 2016Äê11ÔÂ27ÈÕ

@author: Jerry

Base Utils to process recommend system
'''

def OrderMapByValue(dict):
    """
    Order the map by value
    It's commonly used in Recommendation system
    """
    if not dict:
        return {}
      
    
    
    
    
    

def QuickSort(L, low, high):
    '''
    quick sort algorithm as base
    '''
    i = low 
    j = high
    if i >= j:
        return L
    key = L[i]
    
    while i < j:
        while i < j and L[j] >= key:
            j = j-1                                                             
        L[i] = L[j]
        while i < j and L[i] <= key:    
            i = i+1 
        L[j] = L[i]
    L[i] = key 
    QuickSort(L, low, i-1)
    QuickSort(L, j+1, high)
    return L
