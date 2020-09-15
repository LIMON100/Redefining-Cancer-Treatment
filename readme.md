# Redefining-Cancer-Treatment


## Problem Statement:
~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ *

This was mainly a KAGGLE competition. So the description is as same as in kaggle page.

In this competition you will develop algorithms to classify genetic mutations based on clinical evidence (text).

There are nine different classes a genetic mutation can be classified on.

This is not a trivial task since interpreting clinical evidence is very challenging even for human specialists. Therefore, modeling the clinical evidence (text) will be critical for the success of your approach.

Both, training and test, data sets are provided via two different files. One (training/test_variants) provides the information about the genetic mutations, whereas the other (training/test_text) provides the clinical evidence (text) that our human experts used to classify the genetic mutations. Both are linked via the ID field.

Therefore the genetic mutation (row) with ID=15 in the file training_variants, was classified using the clinical evidence (text) from the row with ID=15 in the file training_text

Finally, to make it more exciting!! Some of the test data is machine-generated to prevent hand labeling. You will submit all the results of your classification algorithm, and we will ignore the machine-generated samples. 





## Dataset:

https://www.kaggle.com/c/msk-redefining-cancer-treatment/data




## Methodology:

This project is mainly find out the gene class by analysis different research article. There is 9 different class of gene. By processing the text we apply:



### Text-Preprocessing
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

#### Stop words
    
#### Replace all special character with SPACE

#### Every Space is connecting with underscore(_)

#### Replace double space with single space





    
### After preprocessing the text part we focus on Analysis every column. There are mainly 4 columns 
   **gene**
   
   **variation**
   
   **class**
   
   **text**



### Apply two differnet method for converting categorical value.
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-


#### 1.Response-Encoding

#### 2-One-hot-encoding





### Normalize Data
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-


### Combine all different type converting column together.
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-


### Apply Machine Learning Algorithm
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

#### 1 . Logistic Regression

#### 2 . KNN

#### 3 . Naive Bayes

#### 4 . SVM

#### 5 . Random Forest

#### 6 . Stacking Classifer

#### 7 . AdaBoost(Boosting tecnique)

#### 8 . XGBoost(Boosting tecnique)




### Apply all ML algorithm one is for response-encoding and also in one-hot-encoding
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-



### Apply ML algorithm on
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

#### 1. Balancing all classes

#### 2. Default





### Find the Interpretablility of a ML-Algorithm.
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-




### Result is check using,
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

#### Confusion-Matrix 

#### Precision

#### Recall

#### Log-Loss

#### Mis-Classified points
