from simple_unittest  import test

def cakes(recipe, available):
    if len(recipe) > len(available):
        return 0

    max = -1

    for k in recipe:
        if(k not in available):
            return 0

        cur = int(available[k] / recipe[k])
        if max == -1:
            max = cur
        elif max > cur:
            max = cur


    return max


# 1. if len recipe > len available then 0 as its clear we lack ingredients
# most basic idea
# go through each recipe key check if it exissts 
# if not -> 0,
# if exists - divide available by recipe - set it as max doable
# go to next key -> if max < previous max new max it is
# this would then be O(n) as we only go through available list and checking another one is O(1)

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200}
test('len different', cakes(recipe, available), 0)

recipe = {'pears': 61, 'butter': 54, 'sugar': 81} 
available = {'flour': 3190, 'butter': 34, 'cream': 8955, 'crumbles': 3153, 'pears': 4032, 'sugar': 2134, 'apples': 5238, 'oil': 8597, 'nuts': 1870, 'cocoa': 5292}
test('failing test', cakes(recipe, available), 0)

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
test('example #1', cakes(recipe, available), 2)

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
test('example #2', cakes(recipe, available), 0)