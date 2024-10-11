# Data Preprocessing and Feature Engineering
October 11, 2024
### Overview
Data preprocessing: A step in preparing raw text for machine learning models. This involves cleaning, organizing,  
and transforming text data into formats that models can understand. Preprocessing includes both traditional data  
cleaning and advanced feature engineering techniques to create effective text embeddings for downstream tasks.

- **Preprocessing Steps**:
  - **Tokenization**: Split text into smaller units called tokens. Start with sentence tokenization, followed by  
   word tokenization.
  - **Lowercasing**: Convert all text to lowercase to reduce variability in the data.
  - **Stop Word Removal**: Remove commonly used words (e.g., "the", "and") that do not contribute significant  
  meaning.
  - **Stemming & Lemmatization**:
    - **Stemming**: Strip suffixes to obtain the root form of a word (e.g., "running" becomes "run").
    - **Lemmatization**: Reduce words to their base or dictionary form, considering their part of speech  
     (e.g., "better" becomes "good").
  - **Removing Digits and Punctuation**: Clean text by removing numbers and punctuation marks to focus on  
  meaningful content.
  - **Part of Speech Tagging (POS)**: Assign each word its grammatical category (e.g., noun, verb).
  - **Named Entity Recognition (NER)**: Identify and classify named entities such as people, locations, dates,  
  and organizations.

- **Feature Engineering**:
  - **Text Representation**: Convert processed text into numerical form that machine learning models can  
  understand.
  - **Approaches**:
    - **Traditional Representations**:
      - **Unique ID Assignment**: Assign a unique identifier to each word. This method can become inefficient   
      with large vocabularies.
      - **TF-IDF (Term Frequency-Inverse Document Frequency)**: Compute the importance of a word based on its   
      frequency in a document versus its rarity in a corpus. Effective for smaller NLP tasks, but limited for  
      deep contextual understanding.
      - **Bag of Words (BoW)**: Create a word frequency vector, ignoring the order of words. It captures word  
      occurrence but lacks context awareness.
    - **Word Embeddings**:
      - **Neural Embeddings**: Use neural networks to create dense, fixed-size vector representations of words.
        - **Pretrained Embeddings**:
          - **Word2Vec** (Google): Captures semantic relationships between words.
          - **GloVe** (Stanford): Produces vectors that capture global word relationships.
          - **fastText** (Facebook): Extends Word2Vec by including subword information, useful for rare words.
          - **BERT** (Google): Contextual embeddings that use bidirectional transformers, allowing words to be   
          understood in different contexts. This is our planned choice due to its high performance and versatility.
      - **Training Custom Embeddings**:
        - **Continuous Bag of Words (CBOW)**: Predict the target word given its surrounding context words.
        - **SkipGram**: Predict context words given a target word, useful for capturing relationships in larger corpora.

# Data Annotation

### Overview
Data annotation: create high-quality training data for NLP models. It involves labeling text data  
to provide contextual meaning to words and phrases, allowing models to learn relationships, entities, and emotions  
within the data.

- **Challenges in Data Annotation**:
  - Large datasets require substantial manual work, which can be time-consuming.
  - Identifying suitable data for annotation can be challenging, especially when the context is specific.
  - Natural language is inherently ambiguous, leading to variability in annotators' interpretations.
  - Bias can be introduced during annotation, affecting the model's learning process.

- **Annotation Methods**:
  - **Manual Annotation**: Performed by human annotators; generally yields high accuracy but is labor-intensive.
  - **Automated Annotation**: Uses algorithms to label data quickly, suitable for large datasets but may lead to inaccuracies.
  - **Hybrid Approach**: Combines manual validation with automated methods to balance accuracy and efficiency.

- **Types of Annotations**:
  - **Entity Annotation**: Identifying and labeling entities such as people, places, or objects.
  - **Entity Linking**: Linking entities in text to a specific knowledge base or identifying relationships among them.
  - **Text & Document Classification**: Categorizing text or documents into predefined classes.
  - **Sentiment Annotation**: Labeling text as positive, negative, or neutral based on emotional content.
  - **Linguistic Annotation**: Adding syntactic and semantic information to text, such as part of speech or grammatical roles.
  - **POS Tagging**: Assigning part of speech to each word based on its function in the sentence.
  - **Coreference Resolution**: Identifying when different expressions refer to the same entity.

- **Best Practices for Annotation**:
  - Establish clear guidelines and standard operating procedures to ensure consistency.
  - Implement quality control through auditing and verification by domain experts.
  - Use **Human-in-the-Loop (HITL)**: Keep humans involved in the annotation process even when automating, to catch and correct potential errors.
  - **Active Learning**: Use model predictions to identify ambiguous or high-value samples for manual review, thereby reducing the amount of data that requires annotation.

