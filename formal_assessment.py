import csv
from transformers import pipeline 
clf = pipeline("text-classification", model="s-nlp/roberta-base-formality-ranker") 

#loading parsed file and for every line classifying formality

with open("Kacper_data/SARC/pol/balanced_parsed.csv", "r", encoding="utf-8") as input, open("Kacper_data/SARC/pol/data.csv", "w", encoding="utf-8") as output:
    reader = csv.DictReader(input)
    writer = csv.writer(output)
    writer.writerow(["text", "is_sarcasm", "is_formal", "formal_score"])

    for row in reader:
        text = row["text"]
        sarcasm = row["label"]
        formal_assessment = clf(text)
        formal_score = formal_assessment[0]["score"]
        formal = "1" if formal_assessment[0]["label"] == "formal" else "0"
        writer.writerow([text, sarcasm, formal, formal_score])