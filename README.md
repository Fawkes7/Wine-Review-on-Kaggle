# Wine-Review-on-Kaggle
Prediction and Visualization on Kaggle Wine Reviews dataset

This repo contains the necessary code and files for running visualizations of the wine review dataset.

## Dataset
To download the dataset, head over to the following link: https://www.kaggle.com/zynicide/wine-reviews. 
For this project, we will be using the following dataset: 'winemag-data-130k-v2.csv'. Save this in the same folder where the clone for the repo is.

## File Structure 
**Wine_reviews_visualization.ipynb:** The main visualizations for our analysis are present in this notebook. If you have saved the dataset in the same folder
as the notebook, then simply run the notebook line by line, and you can see the visualizations; otherwise, set the path of your dataset in the code. The code has headings with numbering to make you understand what is being being visualized. Simply run the entire notebook, and you can review the visualizations.

**featureExtractor.py:** This code was used for extracting the nouns and adjectives from the 'description' column of the dataset. This function outputs a 
.csv file. You don't need to run this in order to generate the csv file. It is already present in the repo.

**Feature.csv:** This is the generated csv file from the featureExtractor.py code. This file is used in the wine_reviews_visualization.ipynb for generating a word cloud.

