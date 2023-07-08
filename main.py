import pronouncing
from collections import Counter
import string


def remove_punctuations(input_string):
    translator = str.maketrans("", "", string.punctuation)
    no_punct = input_string.translate(translator)
    return no_punct

def frequency_score_count(line):

    word_occurance = Counter(line)
    list_frequency = []
    for key in word_occurance:
        if key not in ['a','e','i','o','u'] and word_occurance[key]>1:
            list_frequency.append(word_occurance[key])

    result = sum(list_frequency)
    return result


def syllable_score_count(line):
    words = line.split()
    list_syllable = []

    for word in words:
        pronunciation_list = pronouncing.phones_for_word(word)
        if len(pronunciation_list) == 0:
            continue
        list_syllable.append(pronunciation_list[0])

    freq = Counter(list_syllable)

    list_sum =[]
    for key in freq:
        if freq[key]>1:
            list_sum.append(freq[key])

    result = sum(list_sum)
    return result


def pronounciation_difficulty_count(line):
    words = line.split()
    l = []
    for word in words:
        pronunciation_list = pronouncing.phones_for_word(word)
        if len(pronunciation_list) == 0:
            continue
        count = pronouncing.syllable_count(pronunciation_list[0])
        if count >=2:
            l.append(count)

    result = sum(l)
    return result


def final_score(line):
    frequency_score = frequency_score_count(line)
    syllable_similarity_score = syllable_score_count(line)
    pronounciation_difficulty_score = pronounciation_difficulty_count(line)

    total = frequency_score + syllable_similarity_score + pronounciation_difficulty_score

    return total

score_list = []

with open('twister.txt', 'r') as file:
    total_lines = file.readlines()
    file.seek(0)
    for y in range(len(total_lines)):
        line = file.readline()
        line = line.lower()

        clean_line = remove_punctuations(line.strip())
        score = final_score(clean_line)
        score_list.append(score)

with open('twister.txt','r') as f:
    f.seek(0)
    max_index = score_list.index(max(score_list))
    for x in range(max_index+1):
        best_tongue_twister = f.readline()

    f.seek(0)

    print("\nTongue Twisters and their scores: \n")
    for i in score_list:
        print(f.readline(),i)
    print("\nBest Tongue Twister is and its score:")
    print(best_tongue_twister,max(score_list))
