#1.       ML is focused on making predictions rather than analyzing existing data. ML is interested in what will happen.

#2.       In supervised learning we work on a set of labeled data for train an algorithm (Random forest classification, 
#linear regression, support vector machines). In unsupervised learning we study clusters, distribution etc of unlabeled data 
#(Clustering, anomaly detection, association).

#3.       Test set is the sample of data used to provide an unbiased evaluation of a final model fit on the training dataset 
#while validation set refers to the sample of data held back from training the model. The validation set also play a role in 
#model selection and preparation, such as feature selection and tuning hyperparameters while test set is predominately used 
#to describe the evaluation of a final tuned model and provide an unbiased evaluation of a final model fit on the training dataset.

#4.       We need to prepare our data in order to transform raw data which is often incomplete and inconsistent into an understandable 
#format with certain behaviors or trends. Main preprocessing steps are;
#a.       Importing libraries and data: Numpy for mathematical operation in the code, pandas for importing and managing dataset, 
#matplotlib for plot any type of charts. In importing dataset process we identify and extract dependant and independant variables.
#b.       Missing value handling: Identify and correctly handle the missing values via deleting (less preferred, cause loss of data) 
#or calculating the mean / median values accordingly to the distribution of the dataset.
#c.       Checking the data types: ML modelling is based on mathematical equations. Thus, we have to identify categorical data and 
#encode it into numerical or dummy values.
#d.       Train and test splitting: Split dataset into two separate sets so ML model can learn from data to make predictions. 
#Splitting can be varies according to the dataset shape and size but generally the ratio is 70:30 (70% data for train and 30% 
#data for test) or 80:20 (80% data for train and 20% data for test).
#e.       Feature scaling: Feature scaling is a method to standardize the independent variables of a dataset within a specific 
#range so we can compare them on common grounds.

#5.       A discrete variable is a numeric variable that have a countable number of values between any two values. 
#A continuous variable is a numeric variable that have an infinite number of values between any two values.

#6.       The plot is a histogram for a discrete variable type. Distribution is binomial thus in preprocess step 
#we can check if we could split the data into subgroups.
