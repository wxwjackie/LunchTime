'''
Created on 2016Äê11ÔÂ27ÈÕ

@author: Jerry

@attention: A base class for recommender
'''

class BaseRecommender:
    '''
    Base class for recommender system
    '''
    def __init__(self, user_name, Handler):
        '''
        @param user_name: the user's name on which the recommender applyes
        @param Hander: The Algorithm to apply 
        '''
        self._user_name = user_name
        self._recommend = Handler
    
    
    def recommend(self):
        """
        @attention: give recommendation to 
        @return: A list of the recommendation List with 
        """
        return NotImplemented
