## Task-47 Data Preprocessing and Data Annotation for NLP Models Research 
Date(s): 
 - 07 October 2024 
  - Work Completed:
    - General Overview: Preprocessing and Feature Engineering Research
 - 09 October 2024
  - Work Completed:
    - Corrected data preprocessing section to include original links to sources
      - Also added more information found in new articles when researching data annotation
    - Researched data annotation section and documented notes


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
        - Articles regarding word embeddings:
          - https://www.ibm.com/topics/word-embeddings
          - https://www.turing.com/kb/guide-on-word-embeddings-in-nlp
        - Words are represented by fixed dimension vectors of values that establishes relationships of a word to other words that appear next to that word (a decimal value).
        - Term frequency-inverse document frequency:
          - ML algorithm used for word embeddings for text, comprised of term frequency (TF) and inverse document frequency (IDF)
            - TF: Measures the frequency of a words appearance in a document
            - IDF: How rare a word is in a document
          - Note: This likely would not apply to our application since it is only useful for smaller NLP problems (stop word removal, info retrieval)
          - The structure (vector) itself is not interpretable by a human being due to it being solely numeric representations of various information
            - A general example:
              [
                word1_embedding: [val1, ..., valn],
                word2_embedding: [val1, ..., valn],
                ...
              ]
          - The more dimensions to embeddings, the more information related to a word captured but more computationally demanding
        - Bag of Words: 
          - Vectorization of words based on context in a document/sentence. Generally one of the more popular techniques.
          - Steps:
            - Tokenize the text into sentences
            - Tokenize the sentences into words
            - Remove stopwords/punctuation
            - Convert words to lowercase
            - Create a frequency distribution chart of the words
          - Generally not a good strategy since it does not consider other words in determining context.
        - Training our own embeddings:
          - Continuous Bag of Words: Prediction of center-word given a set of context words.
          - SkipGram: Predict context words based on center-word.
            - The inverse of CBOW
        - Can also use pretrained embeddings:
          - Word2vec by Google
            - This is actually often used to help with training a custom embedding.
          - GloVe by Stanford
          - fasttext by Facebook
          - BERT***
            - What we intend on using since it is pretrained on a considerable amount of data, and should make training less tedious
          - spaCy

# Data Annotation:

Taking raw data and preestablishing context of individual words or groups of words.

### General Overview:
  - Generally one of the most intensive tasks in developing an NLP model
  - Articles used for research:
    - https://www.habiledata.com/blog/text-annotation-for-nlp/
    - https://keymakr.com/blog/expert-guide-to-annotating-text-data-for-nlp/

  - Challenges:
    - Generally require a large amount of training data to properly train the model. This in turn results in a lot of work for preparing the data (manual annotation)
    - Takes a while to locate data to be annotated, since the data needs to meet the contextual requirements the model is being trained for. This also contributes to the workload.
    - Natural language is ambiguous from person to person, and different words/phrases can mean different things to different people
      - This makes accurate annotations more difficult, since two annotators can have drastically different outputs.
    - Introduction of bias when training
      - Annotation is where this problem occurs
  - Methods:
    - Manual: 
      - Process of handling the labeling process by hand, rather than using an automated tool
      - Tends to be more accurate, and easier to catch problems
      - Drawback is that it takes a considerable amount of time
    - Automatic:
      - Use of automated tools to label the data (use with algorithms and NLP models)
      - Quick at handling large sets of data
      - Can result in inaccurate labels being applied, which can introduce major issues when training the model (bias)
    - Hybrid approach:
      - Best of both worlds
      - Generally the best approach since it takes the pros of both manual and automated Methods
      - Drawback is that it can be complex to manage both at the same time effectively

  - Types of annotations:
    - Entity Annotation
      - Identification and labeling of specific entities in text (person, place, thing)
    - Entity Linking
      - Identifying connections in the text to other entities
    - Text Classification
      - Classification of an text into a predetermined grouping
    - Sentiment Annotation ***
      - Labeling of a text/document as positive, negative or neutral
    - Linguistic Annotation
      - Identifies linguistic properties in a text including syntax and semantics
    - Part-of-Speech (POS) Tagging
      - Identifies a given words part of speech within its use
    - Document Classification
      - Same as text classification but for an entire document
    - Coreference Resolution
      - Identifying different words/phrases that mean the same thing as other words/phrases

  - Best Practices:
    - Establish a guideline/process for annotation and set standards for how to properly annotate for the use case
    - Establish a method for validating accurate annotations
      - QA auditing by checking annotated data to ensure accuracy (inspecting the data post-annotation) would be a good strategy
      - Use a Human in the loop approach if process is automation intensive3846
        - Catch issues that occur in the automated process
        - Be able to manage complex edge cases that automation may have trouble with
        - Can implement an active training process where a model is trained while performing its functions under the supervision of a human


# For Our Applications:
    - Preprocessing: 
      - We will probably use already established tools/libraries
        - NLTK, PyTorch, TensorFlow all have well defined and fully vetted tools for preprocessing data
    - Data annotation:
      - We are still trying to find the best course of action for preparing training data for the model
      - Current plan is to prepare a small data set of of manually labeled data to start tuning the model
        - Once the model is up and running, we will transition to a Human-in-the-loop approach where the model trains itself while being supervised and corrected when incorrect labels are applied