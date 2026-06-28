import csv
import pandas as pd
from transformers import pipeline 
clf = pipeline("text-classification", model="s-nlp/roberta-base-formality-ranker") 

#loading parsed file and for every line classifying formality

with open("Kacper_data/SARC/pol/balanced_parsed.csv", "r", encoding="utf-8") as annotated_comms:
    reader = csv.DictReader(annotated_comms)

    for row in reader:
        text = row["text"]
        sarcasm = row["label"]
        formal_assessment = clf(text)
        formal_score = formal_assessment[0]["score"]
        formal = "1" if formal_assessment[0]["label"] == "formal" else "0"
        print(text, sarcasm, formal, formal_score)
