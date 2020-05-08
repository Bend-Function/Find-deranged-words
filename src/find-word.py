# Author: Bend Function
import csv

words = input().lower()
# read dictionary from csv
csvFile = open("ecdict.csv", "r", encoding="utf-8")
reader = csv.reader(csvFile)
dic = []
for item in reader:
    if reader.line_num == 1:
        continue
    # add English to 0, Chinese translation to 1
    dic.append([item[0], item[3]])
    
csvFile.close()

def process(words, loc, now):
    loc.append(now)
    for i in range(len(words)):
        if i not in loc:
            process(words, loc, i)
            
    if len(words) == len(loc):
        out = ""
        for i in range(len(words)):
            out += words[loc[i]]

        # find words in dictionary
        for w in range(len(dic)):
            if out == dic[w][0]:
                print(dic[w])
    del loc[-1]    

for k in range(len(words)):
    process(words,[],k)
