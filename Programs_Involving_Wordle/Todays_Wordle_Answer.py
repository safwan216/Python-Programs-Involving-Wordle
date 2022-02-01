#Takes a text with all the answers and pushes them into a list without the dates
ans = []
with open("All_Wordle_Answers.txt", "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        j = i[-6:-1]
        ans.append(j)
        j = ""
    f.close
	
#Takes a text with all the answers and pushes them into a list without the dates
all_dates = []
with open("All_Wordle_Answers.txt", "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        j = i[0:11]
        all_dates.append(j)
        j = ""
    f.close
	
#Find today's date
from datetime import date
today = date.today()
day = today.strftime("%b %d %Y")

#Finds the index of the answer in the 'ans' list by seeing where in the 'all_dates' list today's date is
index = 0
for i in all_dates:
    if i == day:
        break
    index = index + 1
	
#Prints today's date and today's wordle answer
print("Today's Date Is: ", day)
print("Today's Wordle Answer Is: ", ans[index])