import string
import re
import pandas as pd
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import time
from tqdm import tqdm

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

def getNounsAdjs(description):
    doc = nlp(description)
    features = [chunk.text for chunk in doc.noun_chunks]
    review = str(" ".join([i.lemma_ for i in doc]))
    docstring = nlp(review)
    for doc in docstring:
        if doc.pos_ in ("NOUN", "PROPN"):
            features.append(doc.text)
    return features

if __name__=='__main__':
    tqdm.pandas()
    feature = df['description_Cleaned_1'][0:1].progress_apply(getNounsAdjs)
    feature.to_csv('Feature.csv')