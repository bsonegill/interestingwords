from nltk.tag import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup as bs
import pandas as pd
import webbrowser as wb
import os
import re

lemmatizer = WordNetLemmatizer()

################################################################################
#                              Functions
################################################################################

# Creates and maintains dictionary of interesting words as well as a word list
# of interesting words already found

def dict_add(word, sentence, file):
    if word in WORDS:
        word_data[word]["count"] += 1
        if not sentence in word_data[word]["sentences"]:
            word_data[word]["sentences"].append(sentence)
        if not file in word_data[word]["files"]:
            word_data[word]["files"].append(file)
    else:
        WORDS.append(word)
        word_data[word] = {
        "word": word,
        "count": 1,
        "sentences": [sentence],
        "files": [file]
        }


# Runs through a sentence and finds interesting words

stop_words = set(stopwords.words("english"))
interesting_tags = ["JJ", "NN", "NNS", "NNP", "NNPS"] #https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

def interesting_words(sentence):
    rtn_words = []
    tag_sentence = pos_tag(word_tokenize(sentence))
    for word in tag_sentence:
        if word[1] in interesting_tags and len(word) > 1 and not word[0].lower() in stop_words:
            if word[1] == "JJ":
                type = "a"
            else:
                type = "n"
            rtn_words.append(lemmatizer.lemmatize(word[0].lower(), pos=type))
    return rtn_words

# Fixes style of 'files' column
def fix_files(text, parent):
    parent.clear()
    text = text[1:-1]
    list_text = text.split(", ")
    for item in list_text:
        new_p = soup.new_tag("p")
        parent.append(new_p)
        new_p.string = item

# Separates sentences into spaced p tags and boldens the interesting word
def fix_sentences(text, parent, word):
    parent.clear()
    text = text[1:-1]
    list_text = text.split("., ")
    for item in list_text:
        new_p = soup.new_tag("p")
        match = re.search(word, item.lower())
        if not match == None:
            start, end = match.start(), match.end()
            new_p.append(item[:start])
            bold = soup.new_tag("strong")
            bold.string = word.upper()
            new_p.append(bold)
            new_p.append(item[end:])
            parent.append(new_p)
        else:
            # Just in case of exceptions where the stem is to different from the
            # interesting word
            parent.append(new_p)
            new_p.string = item

################################################################################
#                              MAIN
################################################################################


############ Iterate through each file and find words considered interesting####
script_dir = os.path.dirname(__file__)
FILES = os.listdir('testDocs/')

WORDS = []
word_data = {}

for file in FILES:
    fpath = os.path.join(script_dir, "testdocs/{}".format(file))
    with open(fpath, encoding="utf8") as fhandle:
        for line in fhandle:
            for sentence in sent_tokenize(line):
                words = interesting_words(sentence)
                if len(words) != 0:
                    for word in words:
                        dict_add(word, sentence, file)

############ Create a dataframe and create HTML file to display ################
df = pd.DataFrame(word_data).T
df = df.sort_values('count', ascending=False)
df = df.set_index('word')
df.to_html('temp.html')


############ Edit output file to make for a better reading #####################
with open("temp.html", encoding="utf8") as html_df:
    soup = bs(html_df, "html.parser")
    table_rows = soup.tbody.find_all("tr")

    for row in table_rows:
        th = row.find("th")
        word = th.get_text()

        tds = row.find_all("td")
        index = 0
        for td in tds:
            td_text = td.get_text()
            if index == 1:
                fix_sentences(td_text, td, word)
            elif index == 2:
                fix_files(td_text, td)
            index += 1

        th.string = word.capitalize()


############ Create and open program output ####################################
output = "Output.html"
with open(output, "w") as file:
    file.write(str(soup))

os.remove("temp.html")
wb.open(output, new=2)
