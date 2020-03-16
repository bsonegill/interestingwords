# Interesting Words

This programs opens documents placed in the 'testDocs' directory, iterates through each one, selecting interesitng words and then creating an HTML file displaying the words, sentences and files they appear in that pops up in your browser.

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
  * For the filtering, each word in the sentence is tagged with their corresponding part-of-speech tag, as well as being checked against the 'stop_words' that come with the 'nltk' library.
   * The tags I consider interesting are in the `interesting_tags` list on line 40, 


### Walk through

