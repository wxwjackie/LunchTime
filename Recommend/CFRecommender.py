'''
Created on 2016

@author: Jerry

@attention: A collabative filter method to implementation recommender
'''
from BaseRecommender import BaseRecommender
import Lunch.OrderUtils as OrderUtils
import CollaborativeFiltering as CFUtil

class CFRecommender(BaseRecommender):
    """
    Collarative filter recommendation
    """
    def __init__(self, user_name, recommend_num):
        self._user_name = user_name
        self._recommend_num = recommend_num
        
    
    def Recommend(self, flag=None):
        """
        Use CF method to implement the recommend
        """
        raw_list = OrderUtils.get_orders_by_user(self._user_name)
        return []

