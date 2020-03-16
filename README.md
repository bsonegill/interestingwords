# Interesting Words

This programs opens documents placed in the 'testDocs' directory, iterates through each one, selecting interesitng words and then creating an HTML file displaying the words, sentences and files they appear in that pops up in your browser.

NOTE: the `output.html` file in the repository is mainly jsut for reference, this file contains the output that is generated from main.py and when you run the code you should get an identical file

## Getting Started

### Prerequisites 

Apart from the standard libraries, you will need to install, 'nltk', 'bs4' and 'pandas'. If you don't have them already you can simply use pip install in your command prompt.

```
pip install nltk
pip install bs4
pip install pandas
```
All very straight forward


### Installing 'nltk'

If you have never used 'nltk' on your local machine before you first need to write the following two liner and run in python:

```
import nltk
nltk.download()
```

When you run the above you will get a pop up window, select 'all' and click 'download', after that you are all set to run Interesting Words.

### TestDocs

In the test directory you will find 6 test .txt documents, feel free to drop others or more in there, these are the files that we will be analysing using main.py

## main.py

The program has 4 main parts to it under the main comment block. 

### 1. Find interesting words in files

* Gets a list of all files in the directory and iterates through each one, make sure that the script is being run from the main directory, else you may not find the right directory
* Each file is broken into sentences
* Each sentence is run through the `indersting_words()` function
* The `interesting_words()` function filters out words that are not interesting, taking the ones that are and adding to a list that is returned  
  * For the filtering, each word in the sentence is tagged with their corresponding part-of-speech (POS) tag, as well as being checked against the 'stop_words' that come with the 'nltk' library.
   * The tags I consider interesting are in the `interesting_tags` list on line 40, if you want to change what tags are consdiered interesitng, you can see a list of the POS tags [here](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)
 * The function also uses `WordNetLemmatizer()` to find the root of the word, this is to avoid separating words like "Iraq" and "Iraq's" when for context they probably should be grouped together
   *NOTE: this does make the bolding of the interesting word in the sentence less accurate when displayed to the user, example: countries has the root country
* The list of interseting words is then passed thourgh the `dict_add()` function that adds the word to a dictionary that contains all the interesting words and their corresponding sentences and files as well as keep track of the count, if the interesting word has already been found then it updates the word's dictionary
   
### 2. Create dataframe and output an HTML table

* Creates a pandas dataframe from the dictionary of interesting words
* Organizes the dataframe to show most frequently mentioned words first
* Creates HTML file (temp.html) containing the table

### 3. Edit HTML table to make results more readable

* Creates a BeautifulSoup object from temp.html
* Iterates through the table rows to do the following:
 * Word column: Capitalize the word
 * Sentences column: Separate sentences where the words appears and bold the word to make it stand out
 * Files: Separate the file names

### 4. Create output file and open

* Creates the final output file (Output.html) from the modified BeautifulSoup object
* Deletes temp.html and opens the output in the browser

## In hindsight...

When I decided to put the final output into HTML I was not thinking of how a client might use this program. 

If I am a client and asked for a program with this functionality I will most likely be putting the output into some sort of report or presentation, not just looking at it and that is that.

Better would have been to create a word doc to put the table into, this would allow client then to copy/paste the table into a report/presentation, for this I could have used the `docx` library.

Also, it would be cool to create a wordcloud of the most frequetnly mentioned interesting words or a bar chart, this could have been done with `matplotlib`
