'''
import matplotlib.pyplot as plt

from collections import Counter

with open('Peter.txt','r') as file:
    my_str = file.read()
    words = my_str.split()


stop = ['is','are', 'we','you','the','this','on','in','of','at','an','it','they','us','and','our','over','a','to','can','if']
non_stop_words = []
new_text =''
for x in words:
    if x.lower() not in stop:
        new_text = new_text + x + " "
        #non_stop_words.append(x)

#print(new_text)
#print(non_stop_words)
file.close()

with open('newfile.txt','w+') as f:
    f.write(new_text)
    f.seek(0)
    strr = f.read()

word_occurance = Counter(strr.split())
#print(word_occurance)

words_list = list(word_occurance.keys())
frequency = list(word_occurance.values())


plt.barh(words_list, frequency)


for index, value in enumerate(frequency):
    plt.text(value, index, str(value))


plt.xlabel('Frequency')
plt.ylabel('Words')
plt.title('Horizontal Bar Graph with Value Labels')

plt.show()
'''

'''
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)
engine.setProperty('rate', 150)
# engine.say("Hello, How are you ?")
engine.runAndWait()

def speak(str):
    engine.say(str)
    engine.runAndWait()

speak("Hello, What's going on")



import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Function to check if a word has a difficult pronunciation
def has_difficult_pronunciation(word):
    # Set the word to be spoken by the engine
    engine.say(word)
    engine.runAndWait()

    # Get the phonetic pronunciation of the word
    phonetic = engine.phonemes(word)

    # Check the complexity of the phonetic representation
    # You can define your own criteria for determining difficulty
    if len(phonetic) >= 10:
        return True
    else:
        return False

# Example usage
words = ['python', 'xylophone', 'complicated', 'hello']

for word in words:
    if has_difficult_pronunciation(word):
        print(f"{word} has a potentially difficult pronunciation.")
    else:
        print(f"{word} does not have a difficult pronunciation.")
'''

import pronouncing
pronunciation_list1 = pronouncing.phones_for_word("cat")
pronunciation_list2 = pronouncing.phones_for_word("witch")
pronunciation_list3 = pronouncing.phones_for_word("swtiched")

print(pronouncing.syllable_count(pronunciation_list1[0]))
print(pronouncing.syllable_count(pronunciation_list2[0]))
#print(pronouncing.syllable_count(pronunciation_list3))

print(pronunciation_list1[0])
print(pronunciation_list2[0])
print(pronunciation_list3)
