
# Tokenizer
Tokenization of strings


## Installation

#### Add Virtual Environment
```bash
    python -m venv venv
    source venv/bin/activate
```

#### Install ntlk with pip

```bash
    pip install -U nltk
    pip install transformers
```
    
## Documentation

#### Why do we need to tokenize strings?
- break down complex text into manageable units
- present text in format easire to analyze or perfom operation
- specific linguistic task, part-of-speech tagging, syntatic parsing, NER
- NLP application and create structured training data

#### What are these tokens used for?
- Feature extraction - frequency, part-of-speech tags, poistion in sentence etc. In sentiment analysis the presence of certain tokens might be strongly indicative of +ve/-ve sentiment
- Vectorization - NLP tasks tokens are converted to numerical vectors using techniquest like Bag of Words, TF-IDF (Term Frequency-Inverse Document Frequency) or word embeddings (Word2Vec, GloVe)
- Sequence Modeling - translation, text generation tokens are used in sequence models like Recurrent Neural Networks (RNNs), Long Short-Term Memory Networks (LSTMs) or Transformers. Predict sequences of tokens understand the context and likelihood of token occurences
- Training the Model 
- Context Understanding

#### Why use such different and more complicated tokenization methods?
- tokens are more intricate representations of language than complete words
- address a large range of vocabulary
- smaller subunits is computationally more efficient
- help better contextual understanding
- more adaptable across languages that can be quite different from English
## Authors

- [@tragz](https://github.com/tragz)


## 🚀 About Me
I'm a full stack developer...


## Acknowledgements

 - [Explalined: Tokens  and Embeddings in LLMs](https://medium.com/the-research-nest/explained-tokens-and-embeddings-in-llms-69a16ba5db33)



 More on READEME
 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## Appendix

Any additional information goes here

