# coding=utf-8
#!/usr/bin/python
'''
推荐系统的经典算法就是协同过滤了，协同过滤算法有两种，一种是基于物品的，一种是基于用户的.
简单来说基于物品的协同过滤算法是说系统会推荐与你所喜欢物品相似的物品，
而基于用户的协同过滤算法是说系统推荐和你相似的用户所喜欢的物品。
计算物品的相似的时候我们比较不同的人来对他打分来比较，
同样计算用户相关性的时候我们就是通过对比他们对相同物品打分的相关度来计算的
Created on 2016年12月3日

@author: lowang
'''
from math import sqrt
from testData import critics

def sim_distance(prefs, person1, person2, dist_fun=None):
    '''
    Compute the distance between two persons.
    '''
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    if len(si) == 0: return 0
    
    if dist_fun and callable(dist_fun):
        return dist_fun(prefs, person1, person2)
    else:
        sum_of_squres = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                             for item in prefs[person1] if item in prefs[person2]])
        return 1 / (1 + sqrt(sum_of_squres))

def power_distance(prefs, person1, person2):
    '''
    Euclidean distance
    '''
    if not isinstance(prefs, dict):
        raise "prefs should be a dict"
    sum_of_squres = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                     for item in prefs[person1] if item in prefs[person2]])
    return 1 / (1 + sqrt(sum_of_squres))

def pearson_distance(prefs, person1, person2):
    '''
    pearson distance: depend on cosa. The value is between (-1,1).
    '''
    # Get the list of mutually rated items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # if they are no ratings in common, return 0
    if len(si) == 0:
        return 0

    # Sum calculations
    n = len(si)

    # Sums of all the preferences
    sum1 = sum([prefs[person1][item] for item in si])
    sum2 = sum([prefs[person2][item] for item in si])

    # Sums of the squares
    sum1Sq = sum([pow(prefs[person1][item], 2) for item in si])
    sum2Sq = sum([pow(prefs[person2][item], 2) for item in si])

    # Sum of the products
    pSum = sum([prefs[person1][item] * prefs[person2][item] for item in si])

    # Calculate r (Pearson score)
    num = n * pSum - (sum1 * sum2)
    den = sqrt((n * sum1Sq - pow(sum1, 2)) * (n * sum2Sq - pow(sum2, 2)))
    if den == 0:
        return 0

    return num / den

def top_matches(perfs, person, n=5, dist_fun=pearson_distance):
    '''
    Return the top n persons who are most similary to the person in their common marks
    @param n: if n equals 0, return all ranks
    '''
    if not callable(dist_fun):
        dist_fun = pearson_distance
    scores = [(dist_fun(perfs, person, other), other) for other in perfs
              if other != person]
    scores.sort()
    scores.reverse()

    if n and len(scores) > n:
        return scores[0:n]
    else:
        return scores

def get_recommendation(perfs, person, dist_fun=pearson_distance):
    '''
    return the recommend goods for the person
    @param perfs:
    @param person:
    @param dist_fun:
    '''
    totals, sim_sums = {}, {}
    tops = top_matches(perfs, person, n=0, dist_fun=dist_fun)
#     print tops
    for (sim, other) in tops:
        if sim <= 0: continue
        for item in perfs[other]:
            if item not in perfs[person] or perfs[person][item] == 0:
                #similarity degree * evalutions value
                totals.setdefault(item, 0)
                totals[item] += perfs[other][item] * sim
                # sum of similarity
                sim_sums.setdefault(item, 0)
                sim_sums[item] += sim
    # normalization
    rankings = [(total / sim_sums[item], item) for item, total in totals.items()]
    rankings.sort()
    rankings.reverse()  # return None
    return rankings

def transform_perfs(perfs):
    '''
    Convert the data dict used for item-based collaborative filtering
    '''
    result = {}
    for person in perfs:
        for item in perfs[person]:
            result.setdefault(item, {})
            result[item][person] = perfs[person][item]
    return result

def calculate_similar_items(prefs, n=10, dist_fun=power_distance):
    '''Create a dictionary of items showing which other items they
    are most similar to.
    '''
    result = {}
    if not callable(dist_fun):
        dist_fun = power_distance
    # Invert the preference matrix to be item-centric
    itemPrefs = transform_perfs(prefs)
    c = 0
    for item in itemPrefs:
        # Status updates for large datasets
        c += 1
        if c % 100 == 0: print "%d / %d" % (c, len(itemPrefs))
        # Find the most similar items to this one
        scores = top_matches(itemPrefs, item, n=n, dist_fun=dist_fun)
        result[item] = scores
    return result

def get_recommended_items(prefs, item_match, user):
    '''
    Get the recommended Items using item-based collaborative filtering
    '''
    user_ratings = prefs[user]
    scores = {}
    total_sim = {}
    # Loop over items rated by this user
    for (item, rating) in user_ratings.items():
        # Loop over items similar to this one
        for (similarity, item2) in item_match[item]:
            # Ignore if this user has already rated this item
            if item2 in user_ratings: continue
            # Weighted sum of rating times similarity
            scores.setdefault(item2, 0)
            scores[item2] += similarity * rating
            # Sum of all the similarities
            total_sim.setdefault(item2, 0)
            total_sim[item2] += similarity

    # Divide each total score by total weighting to get an average
    rankings = [(score / total_sim[item], item) for item, score in scores.items()]

    # Return the rankings from highest to lowest
    rankings.sort()
    rankings.reverse()
    return rankings
if __name__ == '__main__':
    print "sim_distance:", sim_distance(critics, 'Lisa Rose', 'Gene Seymour', None)
    print "power_distance", power_distance(critics, 'Lisa Rose', 'Gene Seymour')
    print "sim_distance pearson", sim_distance(critics, 'Lisa Rose', 'Gene Seymour', pearson_distance)
    print "pearson_distance", pearson_distance(critics, 'Lisa Rose', 'Gene Seymour')
    print "Toby top_matches", top_matches(critics, 'Toby', n=3, dist_fun=pearson_distance)
    print "Toby get_recommendation", get_recommendation(critics, 'Toby', pearson_distance)
    movies = transform_perfs(critics)
    print "Items top_matches", top_matches(movies, "Superman Returns", pearson_distance)
    print "get_recommendation", get_recommendation(movies, "Just My Luck", pearson_distance)
    print "calculateSimilarItems"
    item_sims = calculate_similar_items(critics)
    for item in item_sims:
        print item , item_sims[item]
    print get_recommended_items(critics, item_sims, "Toby")
