import string
import re
import pandas as pd
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
import spacy

# Importing our dataset in variable df_wine1
df = pd.read_csv('./data/winemag-data-130k-v2.csv', index_col=0)
df.drop_duplicates(('description', 'title'), inplace=True)
df[pd.notnull(df.price)]
total = df.isnull().sum().sort_values(ascending = False)
percent = (df.isnull().sum()/df.isnull().count()*100).sort_values(ascending = False)
missing_data  = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])

# Imputing missing values
for col in ('region_2', 'designation', 'taster_twitter_handle', 'taster_name', 'region_1'):
    df[col]=df[col].fillna('Unknown')
df['province'] = df['province'].fillna(df['province'].mode())
df['price'] = df['price'].fillna(df['price'].mean())


nlp = spacy.load('en_core_web_lg')
def normalize_text(text):
    tm1 = re.sub('<pre>.*?</pre>', '', text, flags=re.DOTALL)
    tm2 = re.sub('<code>.*?</code>', '', tm1, flags=re.DOTALL)
    tm3 = re.sub('<[^>]+>©', '', tm1, flags=re.DOTALL)
    return tm3.replace("\n", "")


df['description_Cleaned_1'] = df['description'].apply(normalize_text)
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS

punctuations = string.punctuation
stopwords = STOP_WORDS

def process_one_description(description):
    doc = nlp(description)
    nouns = [chunk.text for chunk in doc.noun_chunks]
    adjs = []
    review = str(" ".join([i.lemma_ for i in doc]))
    docstring = nlp(review)
    for doc in docstring:
        if doc.pos_ in ("NOUN", "PROPN"):
            adjs.append(doc)
    return nouns, adjs

tmp = df['description_Cleaned_1'][0:3].apply(process_one_description)
print(tmp)




# POS tagging
# for i in nlp(review):
#     print(i, "=>", i.pos_)

# parser = English()
# def spacy_tokenizer(sentence):
#     mytokens = parser(sentence)
#     mytokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]
#     mytokens = [ word for word in mytokens if word not in stopwords and word not in punctuations ]
#     mytokens = " ".join([i for i in mytokens])
#     return mytokens
#
# df["processed_description"] = df["description"].progress_apply(spacy_tokenizer)
#


# def FeatureExtractor(location, )

# def EncodeDescription(descriptions):
