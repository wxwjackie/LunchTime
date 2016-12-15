'''
Created on 2016

@author: Jerry

A Most frequent orders 
'''
from BaseRecommender import BaseRecommender
import Lunch.OrderUtils as OrderUtils
from RecommendUtils import OrderMapByValue


class MostFreqRecommender(BaseRecommender):
    """
    Recommender to give the users most frequent orders
    """
    def __init__(self, user_name, date_start=None, date_end=None):
        '''
        initial class
        '''
        self._user_name = user_name;
        self._date_start = date_start
        self._date_end = date_end
        
    
    def recommend(self, flag=None):
        '''
        Give recommender
        '''
        if not flag:
            sorted_frequency_map = OrderUtils.get_consine_frequency(self._user_name)
            print sorted_frequency_map
        else:
            sorted_frequency_map = OrderUtils.get_resturant_frequency(self._user_name)
        return [item[0] for item in sorted_frequency_map]

