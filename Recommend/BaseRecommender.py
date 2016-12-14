'''
Created on 2016

@author: Jerry

@attention: A base class for recommender
'''
import abc
from Food.settings import RECOMMENDER_TYPE


class BaseRecommender(object):
    '''
    Base class for recommender system
    '''
    __metaclass__ = abc.ABCMeta
    def __init__(self, user_name, Handler):
        '''
        @param user_name: the user's name on which the recommender applyes
        @param Hander: The Algorithm to apply 
        '''
        self._user_name = user_name
        self._recommend = Handler
    
    @abc.abstractmethod
    def recommend(self, flag=None):
        """
        @attention: give recommendation to 
        @return: A list of the recommendation List with 
        """
        return NotImplemented

class RecommenderFactory(object):
    """
    Factory class to init
    """
    @classmethod
    def GetRecommender(cls, user_name):
        """

        :return:
        """
        if RECOMMENDER_TYPE == "MostFreq":
            from MostFreqRecommender import MostFreqRecommender
            return MostFreqRecommender(user_name)
        elif RECOMMENDER_TYPE == "Special" or RECOMMENDER_TYPE == "CFRecommend":
            from CFRecommender import CFRecommender
            return CFRecommender(user_name, 5)
        else:
            return None
