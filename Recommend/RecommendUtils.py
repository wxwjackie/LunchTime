'''
Created on 2016
@author: Jerry

Base Utils to process recommend system
'''
import math

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


class Similarity(object):
    '''
    A class to calculate the similarity of the two items, item might be the
    '''
    def __init__(self):
        '''
        Init the Similarity calculation method
        '''

    def __validate(self, feature_vector1, feature_vector2):
        """

        :param feature_vector1:
        :param feature_vector2:
        :return:
        """

        if not isinstance(feature_vector1, list) or \
                not isinstance(feature_vector1, list):
            print "feature should be a list"
            return False

        if len(feature_vector1) != len(feature_vector2):
            print "feature dimension not match"
            return False

        return True


    def cosine_similarity(self, feature_vector1, feature_vector2):
        '''
        TO calcaulate the consie similarity between the two feature vectors
        :param feature_vector1: feature vector1 with number
        :param feature_vector2: feature vector2
        :return:  a float value represent the ConsineSimilarity
        '''

        if not self.__validate(feature_vector1, feature_vector2):
            return 0

        dot_multiply_value = 0
        len_of_one = 0
        len_of_two = 0
        for i in range(0, len(feature_vector1)):
            dot_multiply_value += (feature_vector1[i] * feature_vector2[i])
            len_of_one += feature_vector1[i]**2
            len_of_two += feature_vector2[i]**2

        return (dot_multiply_value * 1.0)/(math.sqrt(len_of_one*1.0) * math.sqrt(len_of_two*1.0))


    def manhattan_similarity(self, feature_vector1, feature_vector2):
        '''
        Calculate the Mahantan distance between two vector
        :param feature_vector1:
        :param feature_vector2:
        :return:
        '''
        if not self.__validate(feature_vector1, feature_vector2):
            return 0

        distance = 0
        for i in range(0, len(feature_vector1)):
            distance += math.fabs(feature_vector1[i] - feature_vector2[i])

        return distance


    def eucildean_similarity(self, feature_vector1, feature_vector2):
        '''
        use Eucilidean distance to represent the mahantn distance
        :param feature_vector1:
        :param feature_vector2:
        :return:
        '''
        if not self.__validate(feature_vector2, feature_vector1):
            return 0

        distance = 0
        for i in range(0, len(feature_vector1)):
            distance += (feature_vector1[i] - feature_vector2[i])**2

        return distance


