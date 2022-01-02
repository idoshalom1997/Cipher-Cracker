##############################################################
# File: language_dict.py
# Writer: <Ido Shalom>, <Daniel Rodan>
# Exercise: intro2cs ex5 2021-2022
# Description: will be inside the README.py file.
##############################################################


# 1. Compute letters statistics for text
def compute_letters_frequencies(text):
    letters_frequencies = {}
    valid_chars = []                                           # list contains all the valid chars in text.
    for char in text:
        if str.isalpha(char):
            valid_chars.append(str.lower(char))                # convert to lower case.
    n = len(valid_chars)
    for char in "abcdefghijklmnopqrstuvwxyz":                  # count amount and covert to frequencies.
        letters_frequencies[char] = valid_chars.count(char) / n
    return letters_frequencies


# 2. Compute words statistics for text
def compute_words_frequencies(text):
    words_frequencies = {}
    words_text = ""                                     # for the valid words in text.
    for char in text:
        if str.isalpha(char) or char == " ":
            words_text += str.lower(char)
    words = []
    for word in str.split(words_text, " "):             # to isolate each word.
        if word:
            words.append(word)
    n = len(words)
    for word in words:                                  # count amount and covert to frequencies.
        words_frequencies.setdefault(word, 0)           # set 0 as default value if key not exists.
        words_frequencies[word] += 1 / n
    return words_frequencies


# 3. Concatenate items of dictionary to one string
def dict_to_string(d):
    pairs = []                                          # convert each key,value to a string in key:value format.
    for key, value in dict.items(d):                    # get tuple of key,value.
        pairs.append(f"{key}:{value}")                  # add to the key:valve format.
    return " ".join(pairs)                              # return with no extra spaces.


# 4. split string to dictionary
def string_to_dict(s):
    d = {}                                              # convert string to a dictionary format.
    pairs = str.split(s)                                # split by space to get key:valve pairs.
    for string in pairs:
        key, value = string.split(":")                  # split by : to get key and value.
        d[key] = float(value)                           # add the key:value to the dictionary.
    return d


# 5. Save to file
def write_dict(dict, filename):
    with open(filename, "w") as file:                   # open file in write mode.
        file.write(dict_to_string(dict))                # convert dict to string and write the file.


# 6. Load from file
def load_dict(filename):
    with open(filename, "r") as file:                   # open file in read mode.
        return string_to_dict(file.read())              # read the file and convert to dict.





