# ML_HW3
CS6375 MNB

Naïve Bayesian Classifier Implementation [70 points]

In this part, you will implement the naïve Bayes algorithm for text classification tasks. The
version of naïve Bayes that you will implement is called the multinomial naïve Bayes (MNB). The
details of this algorithm can be read from chapter 13 of the book "Introduction to Information
Retrieval" by Manning et al. This chapter can be downloaded from:
http://nlp.stanford.edu/IR-book/pdf/13bayes.pdf

Read the introduction and sections 13.1 and 13.2 carefully. The MNB model is presented in
Figure 13.2 Note that the algorithm uses add-one Laplace smoothing. Make sure that you do all
the calculations in log-scale to avoid underflow as indicated in equation 13.4.
To test your algorithm, you will use the 20 newsgroups dataset, which is available for download
from here: http://qwone.com/~jason/20Newsgroups/

You will use the "20 Newsgroups sorted by date" version. The direct link for this dataset is:
http://qwone.com/~jason/20Newsgroups/20news-bydate.tar.gz

This dataset contains folders for training and test portions, with a sub-folder for different
classes in each portion. For example, in the train portion, there is a sub-folder for computer
graphics class, titled "comp.graphics" and a similar sub-folder exists in the test portion. To
simplify storage and memory requirements, you can select any 5 classes out of these 20 to
use for training and test portions. As always, you have to train your algorithm using the
training portion and test it using the test portion.

IMPORTANT:

• To implement the multinomial Naive Bayes classifier, you may use any of the following
languages: Java, Python, C, C++. You cannot use any machine learning library, but are free to
use any data loading or processing library. You have to specify the libraries used and their
source clearly in the README file. If you have any doubts, first contact the TA and then post the
question on Piazza.

• Your program should be able to read all files from at least 5 sub-folders from the training
portion and create a naïve Bayes model. The model will be tested on test files from the same
classes on the test portion and accuracy on the test dataset should be outputted by your
program. Your program should exclude the header portion from each file. Generally, this means
excluding lines from start of the file up to the line starting with "Lines: xxx"

• Your program should allow exactly two arguments to be specified in the command line
invocation of your program: location of training root folder and test root folder. Your program
should be able read at least 5 sub-folders within each portion and assign the words to
appropriate classes.
