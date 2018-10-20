def sort_scores(scores, highest_score):

    # if there is exists higher value then there will be a key in dictionary with 100 - (value + 1)
    # if the score is from 0 - 100 and we dont anticipate any ... value then we can just go through 
    # all the values and put them to dict with value as key and counter as value

    # then we can do a for from 0 - 100 that in O(1) takes a dict key takes value and adds counter
    # this would be O(1) operatio as it is limited by 100 at the top

    scores_dict = {}
    sorted_scores = []

    for score in scores:
        if score not in scores_dict:
            scores_dict[score] = 1
        else:
            scores_dict[score] += 1


    for key in range(100, -1, -1):
        if key in scores_dict:
            how_many_scores = scores_dict[key]

            for x in range(how_many_scores):
                sorted_scores.append(key)

    return sorted_scores

unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

# Returns [91, 89, 65, 53, 41, 37]
print(sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE))
