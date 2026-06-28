#import pol comments.json
#go through all lines in train_balanced.csv
#parse each line and extract comment text and sarc label (0=not sarcastic, 1=sarcastic)
#sample line:  hq08e c1xebbp|c1xf3xx c1xf53i|1 0

# parse algorithm
# split line by | to separate variables (context IDs, response IDs, label values)
# split response IDs by whitespace
# split labels by whitespace
# iterate over response IDs, extract text and assign to labels
# print line

import csv
import json

with open("Kacper_data/SARC/pol/comments.json", "r", encoding="utf-8") as f:
    data = json.load(f)

line = "hq08e c1xebbp|c1xf3xx c1xf53i|1 0"

context_ids, responses_ids, labels = line.split("|")
print(responses_ids)
responses_ids_split = responses_ids.split()
print(responses_ids_split)
labels_split = labels.split()
print(labels_split)

#printing text
print(data[responses_ids_split[1]]["text"], labels_split[1])

with open("Kacper_data/SARC/pol/balanced_parsed.csv", "w", encoding="utf-8", newline="") as output, open("Kacper_data/SARC/pol/test-balanced.csv", "r", encoding="utf-8") as input:
    writer = csv.writer(output)
    writer.writerow(["text", "label"])
    for line in input:
        context_ids, responses_ids, labels = line.split("|")
        responses_ids_split = responses_ids.split()
        labels_split = labels.split()
        writer.writerow([data[responses_ids_split[0]]["text"], labels_split[0]])
        writer.writerow([data[responses_ids_split[1]]["text"], labels_split[1]])