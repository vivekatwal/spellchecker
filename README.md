

## working
-   we will need a corpus C of correct words for reference
-   On a request word will be checked in corpus C, if word exists then word is correct else 
    using edit distance candidates are created and these candidates if present in Corpus C will be shortlisted
-   For joint words we create candidates by slicing single word into two from i to len(word) and these two words 
    are checked in Corpus C, present words will be returned to user.


## Follow below steps to test 
python app.py

curl localhost:5000/spellCorrect -d '{"word": "vivek"}' -H 'Content-Type: application/json'


## Improvement Scope
-   Use probability of word from corpus for candidate word shortlistings.
-   Use trie data structure for speeding up of checking
-   Use elasticserach for context based spellchecker
-   Language model for re-ranking of words