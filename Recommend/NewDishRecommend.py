'''
Created on 2016

@author: Jerry

A Most frequent orders
'''
from BaseRecommender import BaseRecommender
import Lunch.OrderUtils as OrderUtils


class NewDishRecommender(BaseRecommender):
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
            sorted_frequency_map = OrderUtils.get_consine_frequency(self._user_name, include_all=True, reverse=False)
        else:
            sorted_frequency_map = OrderUtils.get_resturant_frequency(self._user_name, False)
        return [item[0] for item  in sorted_frequency_map if item[1] == 0]

