def clean_and_lowercase(word):
    lowered = word.lower()

    # we can assume that special character will appear at the end of word
    right_index = len(word) - 1

    while not word[right_index].isalpha():
        right_index -= 1

    return lowered[0:right_index + 1]

def increment_or_create_key(key, dictionary):
    if key not in dictionary:
        dictionary[key] = 1
    else:
        dictionary[key] += 1

def build_cloud_data(input_string):

    if len(input_string) <= 0:
        return None

    world_cloud = {}

    current_word_start = 0

    for current in range(len(input_string)):

        # handles case of last character
        if current == len(input_string) - 1:
            word = input_string[current_word_start: current]
            cleanedup_word = clean_and_lowercase(word)
            increment_or_create_key(cleanedup_word, world_cloud)
            continue

        if input_string[current] == ' ':
            word = input_string[current_word_start: current]
            # to start after ' ' char
            current_word_start = current + 1
            cleanedup_word = clean_and_lowercase(word)
            increment_or_create_key(cleanedup_word, world_cloud)

    return world_cloud

print(build_cloud_data('After beating the eggs, Dana read the next step:'))
print(build_cloud_data('Add milk and eggs, then add flour and sugar.'))
