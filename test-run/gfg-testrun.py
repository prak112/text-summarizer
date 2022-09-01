#%%
# import libraries
import mkl
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


print("Library imports successful\n")

# %%
# check stopwords available languages
print(f"List of available languages for stopwords : \n{stopwords.fileids()}\n")

# example text for English and Finnish
eng_text = """The government has finalised next year's state budget, i.e. the budget.
In the budget proposal, the Government aims to respond to the energy crisis and improve the purchasing power of Finns.
There will be tax breaks and direct support for households' electricity bills next winter. 
The government also hopes that the EU will take action to calm the rise in electricity prices.
The Government will support families with children, for example, with an additional child benefit in December. 
In addition, there will be a permanent discount on early childhood education fees.
The budget totals more than EUR 80 billion.
"""

fin_text = """Hallitus on saanut valmiiksi valtion ensi vuoden budjetin eli talousarvion.
Hallitus pyrkii budjettiesityksessä vastaamaan energiakriisiin ja parantamaan suomalaisten ostovoimaa.
Kotitalouksille on luvassa verohelpotuksia ja suoraa tukea ensi talven sähkölaskuihin. 
Hallitus toivoo myös EU:n toimia sähkön hinnan nousun rauhoittamiseksi.
Lapsiperheitä hallitus tukee esimerkiksi ylimääräisellä lapsilisällä joulukuussa. 
Lisäksi varhaiskasvatusmaksuihin tulee pysyvä alennus.
Talousarvion loppusumma on runsaat 80 miljardia euroa.
"""

#  assign stopwords for both English and Finnish
eng_stopwords = set(stopwords.words('english'))
fin_stopwords = set(stopwords.words('finnish'))

#%%
# tokenize words
eng_tokens = word_tokenize(eng_text, language='english', preserve_line=True)
fin_tokens = word_tokenize(fin_text, language='finnish', preserve_line=True)

print(f"English words tokenized, sample : \n{eng_tokens[:5]}\n\n\
Finnish words tokenized, sample : \n{fin_tokens[:5]}\n\n")

# assign tokens
engWords = eng_tokens
finWords = fin_tokens

# function to calculate frequency of words in a sentence
def freqTable(words_list, stopwords):
    """
    Args:
    words_list - list of tokenized words
    stopwords  - list of stopwords
    Returns:
    freqTable - dictionary of words with frequency freq
    """
    # define dictionary
    freqTable = {}

    # iterate through words_list
    for word in words_list:
        word = word.lower()
        if word in stopwords:
            continue
        elif word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    
    return freqTable

# calculate word frequency
engwordFreq = freqTable(engWords, eng_stopwords)
finwordFreq = freqTable(finWords, fin_stopwords)

print(f"Word frequencies : \nEnglish - {engwordFreq}\nFinnish - {finwordFreq}\n\n")

# %%
# tokenize sentences
engSentences = sent_tokenize(eng_text, language='english')
finSentences = sent_tokenize(fin_text, language='finnish')

print(f"English sentences, sample : {engSentences[:2]}\nFinnish sentences, sample : {finSentences[:2]}\n\n")

# function to calculate sentence value by word frequency in sentences
def sentence_score(sentences, freqTable):
    """
    Args:
    sentences - list of tokenized sentences
    freq_tabl - dictionary of words with their frequency 

    Returns:
    sentenceValue - dictionary of sentences with their frequency
    """
    # define dictionary
    sentenceValue = {}

    # assign sentence score based on words frequency
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    return sentenceValue

# calculate sentence frequency
engsentScore = sentence_score(engSentences, engwordFreq)
finsentScore = sentence_score(finSentences, finwordFreq)

print(f"English sentences frequency : {engsentScore}\n\nFinnish sentences frequency : {finsentScore}\n\n")

# %%
