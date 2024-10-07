## Task-47 Data Preprocessing and Data Annotation for NLP Models Research 
Date(s): 
 - 07 October 2024 [General Overview: Preprocessing and Feature Engineering Research]

# Data Preprocessing:

Taking the newly cleaned text and breaking it down/organizing it into embeddings (contexts). Also involves Feature Engineering.

### General Overview:
 - Preprocessing:
    - Tokenization: Segmentation into a list of tokens.
      - Sentence tokenization should be before word tokenization.
    - Lowercasing: convert all text to lower casing.
    - Stop Word Removal: Removes commonly occurring words from data that contribute little value.
    - Stemming and Lemmatization: Reduces words to their base forms.
      - Stemming is the removal of suffixes to get the base form
      - Lemmatization is the reduction of words to their base form depending on their part of speech.
    - Removal of digit/punctuation: Self-explanatory.
    - Part of Speech tagging: Tags words with their part of speech.
    - Named entity recognition: Identifying and classifying named entities in text (people, organizations, locations).

 - Feature Engineering:
    - Representation of text in a numeric vector (text attributes), such that the model can understand.
    - Approaches:
      - Classical/Traditional:
        - Each word is converted to a unique id
        - Large vocab can be problematic for models
      - Neural/Word-embedding:
        - Words are represented by fixed dimension vectors of values that establishes relationships of a word to other words that appear next to that word (a decimal value).
        - Training our own embeddings:
          - Continuous Bag of Words: Prediction of center-word given a set of context words.
          - SkipGram: 	Predict context words based on center-word.
        - Can also use pretrained embeddings:
          - Word2vec by Google
          - GloVe by Stanford
          - fasttext by Facebook