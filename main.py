import pronouncing
from collections import Counter
import string
import pyttsx3
import numpy as np

def text_to_speech(line):
    '''
    Converts any string to speech
    '''
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(line)
    engine.runAndWait()

def choice_for_listening(temp = 0):
    '''
    Returns the choice input
    '''
    while temp == 1:
        print("\nDo you want to listen again?\nIf yes type 1, if no type 0")
        ch = input("Enter your choice: ")
        if ch.isdigit():
            ch = int(ch)
        if ch not in [1, 0]:
            print("INVALID CHOICE!\nTRY AGAIN")
            continue
        if ch == 0:
            return 0
        if ch == 1:
            return 1

    while temp == 0:
        print("\nDo you want to listen to any of the tongue twisters?\nIf yes type 1, if no type 0")
        choice = input("Enter your choice: ")
        if choice.isdigit():
            choice = int(choice)
        if choice not in [1, 0]:
            print("INVALID CHOICE!\nTRY AGAIN")
            continue
        return choice

    while temp ==2:
        print("\nLet's first listen to the best tongue twister!\nEnter 1 for listening, 0 for exit")
        choice = input("Enter your choice: ")
        if choice.isdigit():
            choice = int(choice)
        if choice not in [1, 0]:
            print("INVALID CHOICE!\nTRY AGAIN")
            continue
        return choice

def choose_which_tongue_twister(n):
    '''
    returns the serial number of tongue twister
    '''
    l = np.arange(1,n+1)
    print("\nWhich tongue twister you want to listen to?")
    choice = input("Enter its serial number: 1 or 2 or 3 or....: ")
    if choice.isdigit():
        choice = int(choice)
    if choice not in l:
        print("INVALID CHOICE!\nTRY AGAIN")
        choose_which_tongue_twister(n)
    return choice

def remove_punctuations(input_string):
    '''
    returns string after removing all the punctuation marks from the string input
    '''
    translator = str.maketrans("", "", string.punctuation)
    no_punct = input_string.translate(translator)
    return no_punct

def frequency_score_count(line):
    '''
    returns frequency score of the tongue twister
    '''
    word_occurance = Counter(line)
    list_frequency = []
    for key in word_occurance:
        if key not in ['a','e','i','o','u'] and word_occurance[key]>1:
            list_frequency.append(word_occurance[key])

    result = sum(list_frequency)
    return result


def syllable_score_count(line):
    '''
    returns syllable score of the tongue twister
    '''
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
    '''
    returns pronouniciation difficulty score of the tongue twister
    '''
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
    '''
    returns final score of the tongue twister
    '''
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
    for i in range(len(score_list)):
        print(i+1,")",f.readline(),score_list[i])

    print("\nBest Tongue Twister is and its score:")
    print(best_tongue_twister,max(score_list))

    if(choice_for_listening(2)):
        text_to_speech(best_tongue_twister)

    choice = choice_for_listening()

    while choice == 1:
        f.seek(0)
        serial_num = choose_which_tongue_twister(len(score_list))
        for x in range(serial_num):
            line_to_listen = f.readline()
        text_to_speech(line_to_listen)
        choice = choice_for_listening(1)

    else:
        print("\nTHANK YOU")
