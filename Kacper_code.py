from transformers import pipeline 
clf = pipeline("text-classification", model="s-nlp/roberta-base-formality-ranker") 
print(clf("Oh, how wonderful, another Monday."))
print(clf("skibidi toilet rizz is cool"))