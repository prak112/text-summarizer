#%%
# import libraries
import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize, sent_tokenize

print("Library imports successful\n")

# %%
# check stopwords available languages
print(f"List of available languages for stopwords : \n{stopwords.fileids()}\n")

# example text for English and Finnish
eng_text = """
    Corpus means a collection of text. It could be datasets of anything containing texts 
    be it poems by a certain poet, bodies of work by a certain author, etc. It divides a text into a series of tokens. 
    There are three main tokenizers-word, sentence, and regex tokenizer.
"""

fin_text = """
    Muumipeikko (ruots. Mumintrollet) on Muumi-tarinoiden päähenkilö, ja ensimmäinen Tove Janssonin luoma Muumi-hahmo. 
    Muumipeikko asuu Muumitalossa yhdessä vanhempiensa Muumipapan ja Muumimamman kanssa. 
    Muumipeikosta käytetään toisinaan myös lyhyempää nimitystä Muumi, mikä tosin on hyvin harvinaista. 
    Muumipeikko-nimitystä puolestaan käytetään toisinaan puhuttaessa muumeista yleensä.
"""

#  assign stopwords for both English and Finnish
eng_stopwords = set(stopwords.words('english'))
fin_stopwords = set(stopwords.words('finnish'))

#%%
# tokenize words -- LookUp error
eng_tokens = nltk.word_tokenize(eng_text, 'english')
fin_tokens = nltk.word_tokenize(fin_text, 'finnish')

print(f"English words tokenized, sample : \n{eng_tokens[:5]}\n\
    Finnish words tokenized, sample : {fin_tokens[:5]}")

# %%
