# Example string for tokenization
example_string = "It's over 9000!"

# Method 1: White Space Tokenization
# This method splits the text based on white spaces
white_space_tokens = example_string.split()

# Method 2: WordPunct Tokenization
# This method splits the text into words and punctuation
from nltk.tokenize import WordPunctTokenizer
wordpunct_tokenizer = WordPunctTokenizer()
wordpunct_tokens = wordpunct_tokenizer.tokenize(example_string)

# Method 3: Treebank Word Tokenization
# This method uses the standard word tokenization of the Penn Treebank
from nltk.tokenize import TreebankWordTokenizer
treebank_tokenizer = TreebankWordTokenizer()
treebank_tokens = treebank_tokenizer.tokenize(example_string)

white_space_tokens, wordpunct_tokens, treebank_tokens
