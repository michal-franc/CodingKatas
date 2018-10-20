def are_two_movies(flight_length, movie_lengths):

    if len(movie_lengths) < 2:
        return False

    # a + b = c
    # a = c - b


    # break on two

    # if a doesnt fulfill then put c - a => key dict
    # then check if key b is in dict
    # if not then put c - b => dict
    # break if there is a key

    cache = {}

    for x in movie_lengths:
        if x not in cache:
            cache[flight_length - x] = True
        else:
            return True

    return False

# edge cases
# one movie length - covered
# 20 and two movies with 10 - covered

movie_lengths = [10, 20, 30, 40, 50, 60, 78, 90, 12, 16, 25, 26, 88]

print(are_two_movies(30, movie_lengths))

# What if we wanted the movie lengths to sum to something close to the flight length (say, within 20 minutes)?
# O(n^2) -> calculate what is the maximum number we need to match the movielength + threshdols
# check if there already exists number <= maximun
# if it is -> return True
# if not add current maximum to cache


def are_two_movies_with_threshold(flight_length, movie_lengths, threshold):
    cache = []
    flight_treshold = flight_length + threshold

    for current_movie in movie_lengths:
        maximum_length_to_match = flight_treshold - current_movie
        # is there a less_equal_to_this_one?
        for existing_movie in cache:
            if existing_movie <= maximum_length_to_match:
                return True

        cache.append(maximum_length_to_match)
    return False

# we could optimize it for O(nlgn) by sorting movie_length O(n log(n)) and then for each item
# use binary search O(log(n)
# this would lead to O(nlog(n)) complexityl

def are_two_movies_with_threshold_binary(flight_length, movie_lengths, threshold):
    sorted_movies_lengths = sorted(movie_lengths)
    cache = []
    flight_treshold = flight_length + threshold

    for current_movie_index in range(len(sorted_movies_lengths)):
        maximum_length_to_match = flight_treshold -sorted_movies_lengths[current_movie_index] 

        # exclude current element from the list
        sorted_movies_excluding_current = sorted_movies_lengths[:current_movie_index] + sorted_movies_lengths[current_movie_index + 1:]
        match = [existing_movie for existing_movie in sorted_movies_excluding_current if existing_movie <= maximum_length_to_match]
        return len(match) > 0

    return False

movie_lengths = [10, 20, 30, 1]

print(are_two_movies_with_threshold_binary(10, movie_lengths, 10))
