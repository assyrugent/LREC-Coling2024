# We import the random and os packages
import random
import os

# Download the data and define the directory
# Here we chose the folder as the one this script is saved in
folder_location = os.path.dirname(__file__)
# For our dataset the filenames are either: transliteration_PoS+Morph, transliteration_PoS or unicode_transliteration_PoS.
file_name = 'transliteration_PoS'
f = open(f"{folder_location}/{file_name}.txt","r")
texts = f.readlines()

# Choose the line seperation method, either: EoL (End of Line), EoT (End of Text) or V (Verb seperation).
seperator = 'V'

# Make a list of all lines from the text (all_lines) and also a temporary list to hold the lines that are to be joined into sentences based on the chosen seperator (segment)
all_lines = []
segment = []

# Check first the seperator type, then iterate through each line, join together lines into sentences and add to all_lines
if seperator == 'EoL': # End of Line seperator
    for line in texts:
        if line != '<EoL>\n' and line != '<EoL><EoT>\n':
            segment.append(line)
        else: 
            print(segment)
            all_lines.append(segment)
            segment = []
elif seperator == 'EoT': # End of Text seperator
    for line in texts:    
        if line == '<EoL>\n':
            continue
        elif line != '<EoL><EoT>\n':
            segment.append(line)
        else: 
            all_lines.append(segment)
            segment = []
elif seperator == 'V': # Verb seperator
    for line in texts:
        if line == '<EoL>\n' or line == '<EoL><EoT>\n' or line == '\n':
            continue
        elif '\tV' not in line:
            segment.append(line)
        else: 
            segment.append(line)
            all_lines.append(segment)
            segment = []
        

# Now we will make five parts and distribute the sentences from all_lines randomly
len_all_lines = len(all_lines)
# We make a counter to know which part to add to and we make five empty lists for the parts
counter = 1
part_1 = []
part_2 = []
part_3 = []
part_4 = []
part_5 = [] 
# Now we iterate over each line of the all_lines and move lines one by one to a part until there is none left
while len_all_lines != 0:
    # Get a random index in the all_lines list
    rnd_ = all_lines[random.randint(0, len_all_lines-1)]
    # Depending on the counter we add the sentence from the all_lines with rnd_ index to a fold
    if counter % 5 == 1:
        part_1.append(all_lines[all_lines.index(rnd_)])
    elif counter % 5 == 2:
        part_2.append(all_lines[all_lines.index(rnd_)])
    elif counter % 5 == 3:
        part_3.append(all_lines[all_lines.index(rnd_)])
    elif counter % 5 == 4:
        part_4.append(all_lines[all_lines.index(rnd_)])
    elif counter % 5 == 0:
        part_5.append(all_lines[all_lines.index(rnd_)])
    # Remove the sentence we just added to a part from the all_lines
    all_lines.pop(all_lines.index(rnd_))
    # Update the loop counter and the part counter
    len_all_lines -= 1
    counter += 1

# The last step is to divide the data into train and test data sets by folding the part in five different ways
# Each dataset will be placed in a file that is named after the seperation type and each fold (fold_0X)
all_parts = [part_1,part_2,part_3,part_4,part_5]
folding = [[0,1,2,3,4],[1,2,3,4,0],[2,3,4,0,1],[3,4,0,1,2],[4,0,1,2,3]]
os.mkdir(f'{folder_location}/sep_{seperator}/')
for i in range(0,5):
    train = ''
    for x in all_parts[folding[i][0]]:
        for y in x:
            train += f'{y[0:-1]}\n'
        train += '\n'
    for x in all_parts[folding[i][1]]:
        for y in x:
            train += f'{y[0:-1]}\n'
        train += '\n'
    for x in all_parts[folding[i][2]]:
        for y in x:
            train += f'{y[0:-1]}\n'
        train += '\n'
    for x in all_parts[folding[i][3]]:
        for y in x:
            train += f'{y[0:-1]}\n'
        train += '\n'
    test = ''
    for x in all_parts[folding[i][4]]:
        for y in x:
            test += f'{y[0:-1]}\n'
        test += '\n'

    result_path = f'{folder_location}/sep_{seperator}/{file_name}_fold0{i}/'
    os.mkdir(result_path)
    with open(f'{result_path}/train.txt', 'w') as f:    
        f.write(train)
    with open(f'{result_path}/test.txt', 'w') as f:
        f.write(test)
