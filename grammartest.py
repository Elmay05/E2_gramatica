# ELIMINAR RECURSIVIDAD IZQUIERDA
import nltk
from nltk import CFG
nltk.download('punkt')
nltk.download('punkt_tab') # Descarga el recurso punkt_tab
# Define a context-free grammar
grammar = CFG.fromstring("""
    O -> T Oa
    Oa -> 'and' T Oa |
    T -> F Ta
    Ta -> 'or' F Ta |
    F -> P N Pr | P N
    P -> 'i' 'am' | P1 'are' | P2 'is'
    Pr -> Prep 'the' Plcs
    P1 -> 'you' | 'we' | 'they'
    P2 -> 'he' | 'she' | 'it'
    N -> 'running' | 'sleeping' | 'eating' | 'climbing' | 'thinking'
    Prep -> 'behind' | 'by' | 'near' | 'around' | 'beside' | 'in' | 'on' | 'at'
    Plcs -> 'park' | 'cinema' | 'school' | 'house'





""")
# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)
# Input sentences to be parsed
original_sentences = [
    # Part of the language
    "she is running in the park and He is sleeping in the cinema or You are eating near the school",
    "you are sleeping behind the park",
    "we are eating at the school",
    "he is climbing on the house",
    "she is thinking around the cinema",
    "they are running by the school and we are sleeping",
    "he is eating near the house or she is thinking at the school",
    "it is climbing in the park and you are sleeping by the cinema or I am thinking on the school",


    "I is running",
    "They is sleeping",
    "We are eating the house",
    "She sleeping near the park",
    "He is near the park",
    "It is climbing in park",
    "You are",
    "Running in the school"

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
        print("No se puede analizar")

def parse_sentence(sentence):
    # Convertir a minúsculas
    sentence_lowercase = sentence.lower()
    # Tokenizar
    tokens = nltk.word_tokenize(sentence_lowercase)
    # Parsear
    trees = list(parser.parse(tokens))
    print("\nInput Sentence:", sentence)
    if trees:
        print("LL(1) Parsing:")
        for tree in trees:
            tree.pretty_print()
    else:
        print("No se puede analizar")

parse_sentence("she is running in the park and He is sleeping in the cinema or You are eating near the school")
