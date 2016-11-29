'''
Created on 2016
@author: Jerry

Base Utils to process recommend system
'''

def OrderMapByValue(dict):
    """
    Order the map by value, not the key
    It's commonly used in Recommendation system
    return a list of the key in decrease sqeuence by value
    """
    if not dict:
        return {}

    index_to_key = {}
    index_to_value = {}
    key_list = dict.keys()
    for index in range(0, len(key_list)):
        index_to_key[index] = key_list[index]
        index_to_value[index] = dict[index_to_key[index]]
    #call order function
    key_list = index_to_value.keys()

    QuickSort(key_list, index_to_value, 0, len(index_to_value) - 1)

    ordered_key_list = []
    for key in key_list:
        ordered_key_list.append(index_to_key[key])

    return ordered_key_list



def QuickSort(L, dict, low, high):
    '''
    quick sort algorithm as base
    @Note: L is a dict with index and values, when order, we actually sort the index
    '''
    i = low
    j = high
    if i >= j:
        return L
    key = dict[L[i]]
    key_index = L[i]
    
    while i < j:
        while i < j and dict[L[j]] <= key:
            j = j - 1
        L[i] = L[j]

        while i < j and dict[L[i]] >= key:
            i = i + 1
        L[j] = L[i]

    L[i] = key_index

    QuickSort(L, dict, low, i-1)
    QuickSort(L, dict, j+1, high)
    return L


if __name__ == '__main__':
    test_map = {'a':10, 'b': 11, 'd':4, 'eee':0}
    ret = OrderMapByValue(test_map)
    print ret



