import sys
import csv
import time
start_time = time.time()


# 1) Read French Dictionary and stored all the values in py dictionary
french_dictionary = {}
with open('french_dictionary.csv', mode='r') as csv_file:
    cr = csv.reader(csv_file)
    for row in cr:
        french_dictionary[row[0]] = row[1]
csv_file.close()

# 2) Read Find Words and stored all the values in py list
fw=[]
with open('find_words.txt','r') as f:
    for li in f:
        value = li.replace("\n","")
        fw.append(value)
f.close()


# 3) Intializing a list for counting the replacement
freq_count = []

# 4) Read the file which need changes to it.
with open('t8.shakespeare.txt', 'r+') as fil:
    lines = fil.read()
fil.close()

for i in fw:
    freq_count.append([i, french_dictionary[i], lines.count(i)])
    lines = lines.replace(i, french_dictionary[i])
    
# 5) Modifying the original Text file
with open('t8.shakespeare.txt', 'w') as fi:
    fi.write(lines)
fi.close()

# 6) Storing the frequency in csv file.
filename = "frequency.csv"  
with open(filename, 'w') as csvfile: 
    wrote = csv.writer(csvfile) 
    wrote.writerows(freq_count) 
csvfile.close()

# 7) printing the time of execution.
print("Time taken for execution :  %s sec" % (time.time() - start_time))