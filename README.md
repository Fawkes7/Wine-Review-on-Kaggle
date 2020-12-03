# Wine-Review-on-Kaggle
Visualization on Kaggle Wine Reviews dataset

The project aims to visualize the Kaggle Wine Reviews dataset with concentration on the dimension of Price, Score, Country of Origin, Grape Variety, and their reviewers. 

## Dataset
Download the dataset from https://www.kaggle.com/zynicide/wine-reviews. 
For this project, we mainly use 'winemag-data-130k-v2.csv' in the dataset. It should be stored in the main diretory of the repository.

## File Structure 
**dataProcessing.py:** It preprocesses the raw data, removing the duplicates and filling the missing information with the mean/mode of its category. The output serves as the input to featureExtractor.py and wine_reviews_visualization.ipynb. 

**Wine_reviews_visualization.ipynb:** The main visualizations for our analysis are present in this notebook. Change the path of the dataloader if custom directory is used. Otherwise, it works out-of-the-box. Each section with labeled titles can be executed independently to visualize the corresponding content. 

**featureExtractor.py:** The feature extractor utlizes spacy to parse the nouns and adjectives from wine descriptions. We also provided the parsed features for 'winemag-data-130k-v2' in the repository

**Feature.csv:** This is the generated csv file from featureExtractor.py. This file is used in the wine_reviews_visualization.ipynb for generating a word cloud.

## Third-party Modules
Following third-party modules were used for the project:
1. numpy
2. matplotlib
3. pandas
4. highcharts
5. plotly
6. wordcloud
7. seaborn
8. scipy
9. spacy
10. tqdm
