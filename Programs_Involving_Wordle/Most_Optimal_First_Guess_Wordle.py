#Python Code To Find Most Optimal First Guess For Wordle By Finding The Most
#Frequently Used Letters And Finding The Word(s) That They Create

#Takes a text with all the answers and pushes them into a list without the dates
prev_ans = []
with open("Wordle_Answers.txt", "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        j = i[-6:-1]
        prev_ans.append(j)
        j = ""
    f.close
	
print(prev_ans)
	
	#Python3 program to Split string into characters
def split(word, l):
    l = [char for char in word]
    return l
	
#temp list to split each word in answers list
temp = []
#new list to hold all the split letters
split_ans = []
     
#Driver code
for i in prev_ans:
    temp = split(i, temp)
    for j in temp:
        split_ans.append(j)
print(split_ans)

#Finds a list of the most common letters
import collections as col
counter = col.Counter(split_ans)
print(counter.most_common(5))

#Puts the most common letters into a compact list
most_freq = counter.most_common(5)
most_com = []
for i in most_freq:
    most_com.append(i[0])
print(most_com)

#Takes the list of the most common letters and concatenates it into a single string
temp_string = ""
for i in most_com:
    temp_string = temp_string + i
print(temp_string)

#Finds all the permutations of the string using the itertools library
from itertools import permutations
perm_words = permutations(temp_string, 5)
perm_words_list = list(perm_words)

print(perm_words_list)

#Puts all the permutations into a list
perm = []
for i in perm_words_list:
    perm.append(''.join(i))
print(perm)

#Uses the PyEnchant library to see if there is an actual word in the permutations list and checks to see if it is a real word
import enchant
d = enchant.Dict("en_US")
for i in perm:
    if d.check(i):
        print(i)