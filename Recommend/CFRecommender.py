'''
Created on 2016Äê11ÔÂ27ÈÕ

@author: Jerry

@attention: A collabative filter method to implementation recommender
'''
from BaseRecommender import BaseRecommender

class CFRecommender(BaseRecommender):
    """
    Collarative filter recommendation
    """
    def __init__(self, user_name, recommend_num):
        self._user_name = user_name
        self._recommend_num = recommend_num
        
    
    def Recommend(self):
        """
        Use CF method to implement the recommend
        """
        return []