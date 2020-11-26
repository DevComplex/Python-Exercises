import collections

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]

def getRestaurantIndicies(restaurants):
    output = {}

    for i, restaurant in enumerate(restaurants):
        output[restaurant] = i

    return output

def findRestaurant(list1, list2):
    smallestSum = float('inf')
    groups = collections.defaultdict(list)
    list2Indicies = getRestaurantIndicies(list2)

    for i, restaurant in enumerate(list1):
        if restaurant in list2Indicies:
            indexSum = i + list2Indicies[restaurant]

            if indexSum <= smallestSum:
                smallestSum = indexSum
                groups[smallestSum].append(restaurant)

    return groups[smallestSum]

print(findRestaurant(list1, list2))