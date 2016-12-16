'''
Created on 2016

@author: Jerry

@attention: A collabative filter method to implementation recommender
'''
from BaseRecommender import BaseRecommender
import Lunch.OrderUtils as OrderUtils
import CFRUtils as CFUtil

class CFRecommender(BaseRecommender):
    """
    Collarative filter recommendation
    """
    def __init__(self, user_name, recommend_num=5, flag=True):
        self._user_name = user_name
        self._recommend_num = recommend_num
        self._data = OrderUtils.get_CFR_data(include_all=flag)
        self.trans_data = CFUtil.calculate_similar_items(self._data, self._recommend_num, CFUtil.pearson_distance)
    def recommend(self, flag=1):
        """
        Use CF method to implement the recommend
        
        flag:
        1-UCFR:user-based collaborative filtering recommend
        0-ICFR:item-based collaborative filtering recommend
        """
        try:
            if flag:
                recommends = CFUtil.get_recommendation(self._data, self._user_name)
            else:
                recommends = CFUtil.get_recommended_items(self._data, self.trans_data, self._user_name)

        except Exception, e:
            print e
            recommends = []
        print "recommends=", recommends
        if not recommends:
            sorted_frequency_map = OrderUtils.get_consine_frequency(self._user_name)
            return [item[0] for item in sorted_frequency_map]
        # keep the return value corresponding with MostFreqRecommender, just return cousine name
        return [item[1] for item in recommends]

