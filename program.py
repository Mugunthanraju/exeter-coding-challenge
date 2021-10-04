import sys
import csv
import time
import tracemalloc
start_time = time.time()

tracemalloc.start()
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

dict_count = dict.fromkeys(fw, 0)

# 4) Read the file which need changes to it.
with open('t8.shakespeare.txt', 'r+') as fil:
    lines = fil.read()
fil.close()

# 5.a) For lower case
for i in fw:
    dict_count[i] += lines.count(i.lower())
    lines = lines.replace(i.lower(), french_dictionary[i])

# 5.b) For lower case
for i in fw:
    dict_count[i] += lines.count(i.upper())
    lines = lines.replace(i.upper(), french_dictionary[i].upper())

# 5.c) For lower case
for i in fw:
    dict_count[i] += lines.count(i.capitalize())
    lines = lines.replace(i.capitalize(), french_dictionary[i].capitalize())
    
for i in fw:
    freq_count.append([i, french_dictionary[i], dict_count[i]])


# 6) Modifying the original Text file
with open('t8.shakespeare.txt', 'w') as fi:
    fi.write(lines)
fi.close()

# 7) Storing the frequency in csv file.
filename = "frequency.csv"  
with open(filename, 'w') as csvfile: 
    wrote = csv.writer(csvfile) 
    wrote.writerows(freq_count) 
csvfile.close()

# 8) printing the memory and  time of execution.
print("Memory in bits:" ,tracemalloc.get_traced_memory()[1] - tracemalloc.get_traced_memory()[0])
tracemalloc.stop()

print("Time taken for execution :  %s sec" % (time.time() - start_time))
