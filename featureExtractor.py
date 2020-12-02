import string
import re
import pandas as pd
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from tqdm import tqdm
from dataProcessing import data_processing


def normalize_text(text):
    '''this function normalizes the text and \n'''
    tm1 = re.sub('<pre>.*?</pre>', '', text, flags=re.DOTALL)
    tm2 = re.sub('<code>.*?</code>', '', tm1, flags=re.DOTALL)
    tm3 = re.sub('<[^>]+>©', '', tm1, flags=re.DOTALL)
    return tm3.replace("\n", "")


def getNounsAdjs(description):
    '''get the nouns and adjs from the description'''
    doc = nlp(description)
    features = [chunk.text for chunk in doc.noun_chunks]
    review = str(" ".join([i.lemma_ for i in doc]))
    docstring = nlp(review)
    for doc in docstring:
        if doc.pos_ in ("NOUN", "PROPN"):
            features.append(doc.text)
    return features

if __name__=='__main__':

    #reading the dataset
    df = pd.read_csv('./winemag-data-130k-v2.csv', index_col=0)
    # doing data processing
    df=data_processing(df)
    
    #Loading the pretrained model. Assigns word vectors, POS tags, dependency parses and named entities.
    nlp = spacy.load('en_core_web_lg') 
    
    #normalizing the text
    df['description_Cleaned_1'] = df['description'].apply(normalize_text)
    
    #tqdm shows the progress
    tqdm.pandas()
    
    # applying getNounAdjs to the normalized column
    feature = df['description_Cleaned_1'].progress_apply(getNounsAdjs)
    
    #saving the extracted features to csv
    feature.to_csv('Features.csv')