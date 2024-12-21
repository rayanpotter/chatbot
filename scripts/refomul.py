from spellchecker import SpellChecker
from textblob import TextBlob
import language_tool_python


spell = SpellChecker()
tool = language_tool_python.LanguageTool('en-US')


def correct_spelling(input_text):
   
    input_text = input_text.lower().strip()


    words = input_text.split()
    misspelled = spell.unknown(words)
    corrected_words = [spell.correction(word) if word in misspelled else word for word in words]
    corrected_text = " ".join(corrected_words)


    corrected_text = str(TextBlob(corrected_text).correct())

    matches = tool.check(corrected_text)
    corrected_text = language_tool_python.utils.correct(corrected_text, matches)

   

    return corrected_text
