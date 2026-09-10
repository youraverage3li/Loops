target_words = ["james", "london", "paris", "classified", "asset", "midnight", "nuclear"]
sentence = input("what sentence")
words = sentence.split (" ")

for word in words:
    if word.lower() in target_words:
        print ("[REDACTED]", end="")
    else:
        print( word + " ", end="")
