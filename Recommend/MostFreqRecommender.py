'''
Created on 2016Äê11ÔÂ27ÈÕ

@author: Jerry

A Most frequent orders 
'''
from BaseRecommeder import BaseRecommender
import Lunch.OrderUtils as OrderUtils

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
        
    
    def Recommend(self):
        '''
        Give recommender
        '''
        
        #first get the frequency of the user's order
        raw_list = OrderUtils.get_last_n_order(5, self._user_name)
        if not raw_list:
            return []
        
        frequency_map = {}
        for order in raw_list:
            if frequency_map.has_key(order.cousine.cousine_name):
                frequency_map[order.cousine.cousine_name] += 1
            else:
                frequency_map[order.cousine.cousine_name] = 1
        
        
        return []
        
        
