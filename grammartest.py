import nltk
from nltk import CFG
nltk.download('punkt')

# Define a context-free grammar
grammar = CFG.fromstring("""
    O -> P N Pr O2
    O2 -> 'and' O | 'or' O | 
    P -> 'i am' | 'you are' | 'he is' | 'she is' | 'it is' | 'we are' | 'they are'
    N -> 'running' | 'sleeping' | 'eating' | 'climbing' | 'thinking'
    Prep -> 'behind' | 'by' | 'near' | 'around' | 'beside' | 'in' | 'on' | 'at'
    Plcs -> 'park' | 'cinema' | 'school' | 'house'
    Pr -> Prep 'the' Plcs

""")

# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)

# Input sentences to be parsed
original_sentences = [
    # Part of the language
    "She is running in the park and He is sleeping in the cinema or You are eating near the school"
]

# Convert all sentences to lowercase for parsing
sentences_lowercase = [sentence.lower() for sentence in original_sentences]

# Parse each sentence and print the parse tree or "Unable to parse"
for sentence, sentence_lowercase in zip(original_sentences, sentences_lowercase):
    print()
    print("Input Sentence:", sentence)
    tokens = nltk.word_tokenize(sentence_lowercase)  # Tokenize the lowercase sentence
    trees = list(parser.parse(tokens))
    if trees:
        print("LL(1) Parsing:")
        for tree in trees:
            tree.pretty_print()
    else:
        print("Unable to parse")