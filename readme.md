

Open file
iterate through each line
  Iterate through each word in the line
    If the word is interesting, add to container for interesting words with context

print out each interesting word, occurances and contexts


interesting_tags: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

## *I do not want*: CC, DT, EX, FW, IN, JJR, JJS, LS, MD, PDT, POS (the 's ending)
### PRP, PRP$, RB, RBR, RBS, RP, TO, UH, VBD, VBP, VBZ, WDT, WP, WP$, WRB

## *Maybe I want*: CD (written numbers and digits), VB (contains interesting verbs such as protect, stabilize etc)
### VBG (contains interesting verbs such as failing, fighting), VBN

## *I want*: JJ, NN, NNS, NNP (note includes names (first and last separate)),
### NNPS, SYM (for some reason returns only 'anthrax')


country and countries
