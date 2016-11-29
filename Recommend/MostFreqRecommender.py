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
        
    
    def recommend(self):
        '''
        Give recommender
        '''
        
        #first get the frequency of the user's order
        raw_list = OrderUtils.get_orders_by_user(self._user_name)
        print raw_list
        if not raw_list:
            return []
        
        frequency_map = {}
        for order in raw_list:
            if frequency_map.has_key(order.cousine.cousine_name):
                frequency_map[order.cousine.cousine_name] += 1
            else:
                frequency_map[order.cousine.cousine_name] = 1

        cousine_list = OrderUtils.get_cousine_list()
        print cousine_list
        for cousine in cousine_list:
            print cousine.cousine_name
            if frequency_map.has_key(cousine.cousine_name):
                continue
            frequency_map[cousine.cousine_name] = 0


        print frequency_map
        return OrderMapByValue(frequency_map)


        
        
