import pandas as pd
import numpy as np
import re
import time
import warnings
from sklearn.decomposition import TruncatedSVD
from nltk.corpus import stopwords
from sklearn.preprocessing import normalize
from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer
from sklearn.manifold import TSNE
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB , MultinomialNB
from sklearn.metrics import accuracy_score , confusion_matrix , log_loss , normalized_mutual_info_score
from sklearn.linear_model import SGDClassifier , LogisticRegression
from imblearn.over_sampling import SMOTE
from collections import Counter , defaultdict
from scipy.sparse import hstack
from sklearn.multiclass import OneVsRestClassifier
#from sklearn.model_selection import StatifiedKFold
from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import train_test_split , GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from mlxtend.classifier import StackingClassifier
import math
warnings.filterwarnings("ignore")

dataset11 = pd.read_csv('G:/Software/Machine learning/1/26. Project  Kaggle/training/training_variants.csv')
data_text = pd.read_csv('G:/Software/Machine learning/1/26. Project  Kaggle/training/training_text.csv' , sep = "\|\|"  , engine = 'python' , names = ["ID" , "TEXT"] , skiprows = 1)

sns.countplot(x = 'Class' , data = dataset11)

print(dataset11.head())

stop_words = set(stopwords.words('english'))

def data_text_preprocess(total_text, ind, col):
    # Remove int values from text data as that might not be imp
    if type(total_text) is not int:
        string = ""
        # replacing all special char with space
        total_text = re.sub('[^a-zA-Z0-9\n]', ' ', str(total_text))
        # replacing multiple spaces with single space
        total_text = re.sub('\s+',' ', str(total_text))
        # bring whole text to same lower-case scale.
        total_text = total_text.lower()
        
        for word in total_text.split():
        # if the word is a not a stop word then retain that word from text
            if not word in stop_words:
                string += word + " "
        
        data_text[col][ind] = string
        
        
for index, row in data_text.iterrows():
    if type(row['TEXT']) is str:
        data_text_preprocess(row['TEXT'], index, 'TEXT')
        
        
        

def data_int_preprocess(total_text, ind, col):
    # Remove int values from text data as that might not be imp
    if type(total_text) is not int:
        string = ""
        # replacing all special char with space
        total_text = re.sub('[^a-zA-Z0-9\n]', ' ', str(total_text))
        # replacing multiple spaces with single space
        total_text = re.sub('\s+',' ', str(total_text))
        # bring whole text to same lower-case scale.
        total_text = total_text.lower()
        
        for word in total_text.split():
        # if the word is a not a stop word then retain that word from text
            if not word in stop_words:
                string += word + " "
        
        data_text[col][ind] = string
        
        
for index, row in data_text.iterrows():
    if type(row['ID']) is str:
        data_int_preprocess(row['ID'], index, 'ID')
        
        

result = pd.merge(dataset1, data_text,on='ID', how='left')
result.head()

r = pd.concat([dataset1 , data_text] , axis = 1)
r1 = r.iloc[:,:4]
r2 = r['TEXT']

new_dataset = pd.concat([r1 , r2] , axis = 1)

print(new_dataset[new_dataset.isnull().any(axis = 1)])


new_dataset.Gene = new_dataset.Gene.str.replace('\s+' , '_')
new_dataset.Variation = new_dataset.Variation.str.replace('\s+' , '_')

y = new_dataset['Class'].values
#new_dataset1 = new_dataset.drop(['Class'] , axis = 1)

x_train , test_df , y_train , y_test = train_test_split(new_dataset , y , stratify = y , test_size=0.2)

train_df , cv_df , y_train , y_cv = train_test_split(x_train , y_train , stratify = y_train, test_size=0.2)



cv_class_distribution = cv_df['Class'].value_counts().sort_index()


