
## Python-Prediction-Model

### Prerequisites:
- Python3  `brew install python3`
or you can install python from **official website** from link below
 https://www.python.org/download/releases/3.0/
- Scikit Learn `pip3 install scikit-learn`
**installation instructions**: https://scikit-learn.org/stable/install.html

### Predicting 2014 general election result using Machine Learning technique
In order to predict the 2014 general election turnout, I used a supervised machine learning algorithm based on certain features of individuals and their voting history. I used the Python programming language. To understand the data better, I assumed that people’s willingness to be involved in the general and primary elections differed. Therefore, to predict the 2014 general election turnout level, I trained my model using the past data of general election turnouts. Voting history, for instance, “vh00g”, comes as a string variable rather than an integer value. When initializing the attributes of the “Voter” class, fields prefixed with “vh” were converted to integer values. Additionally, the values of the remaining fields such as marital status, ethnicity, and occupational industry are represented as integer values. However, a few cells under the “age”  and “precinct” fields were empty, so I assigned “0” for those empty cells for the program to run.
### Choosing the prediction method 

Considering the fact that the program should predict if an individual is going to show up at a polling station or not, the machine learning method was the best fit for this model. Scikit-learn library is used, as the library consists of various classification and regression algorithms. After trying different machine learning techniques, I noticed that KNeighbors and Decision Tree methods gave more accurate predictions than the other classifiers. I chose KNeighbors, a supervised machine learning method, because KNeighbors analyses the “n” neighbors around the chosen data plot. More specifically, in my model, the KNeighbors (n=10) algorithm examines the ten nearest neighbors of the chosen voter. Each of these data plots represents one voter. Using the KNeighbors classifier, the algorithm learns patterns of these voters’ voting histories to predict the voter turnout for the 2014 general election. 
### Training the model
To train the model, I used certain features that are essential to the prediction output. Instead of considering all of the variables in the dataset given, I chose certain variables from each category. For instance,  “income” and “net worth” represent the same type of information, which is an individual’s financial stability. Therefore, I only used “income” as a feature in the machine learning process. Using specific features from each category improved the model’s accuracy level. Also, I did not use primary election data as a feature variable, as the model works to predict the general election turnout. 
### Evaluating the model 
After training the model on the training dataset, I tested my model by predicting the 2012 general election turnout and comparing the output to the actual 2012 results. The algorithm predicted the 2012 general election with 91.2% accuracy. According to my model, 2955 people will vote for the 2014 general election. The general election turnout for 2014 is lower than it was in previous years, as the model predicts. Therefore, more campaigners and NGOs should take action to spread the word, and raise awareness about the importance of voting to increase the election turnout. 
