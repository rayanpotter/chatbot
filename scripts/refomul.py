from spellchecker import SpellChecker
from textblob import TextBlob

spell = SpellChecker()

def correct_spelling(input_text):
    input_text = input_text.lower().strip()
    words = input_text.split()
    misspelled = spell.unknown(words)
    corrected_words = [spell.correction(word) if word in misspelled else word for word in words]
    corrected_text = " ".join(corrected_words)
    corrected_text = str(TextBlob(corrected_text).correct())

    return corrected_text

