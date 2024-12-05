# QueryCraft
Query Craft is an innovative project focused on automating question generation from textual content. By utilizing advanced natural language processing (NLP) techniques as well as pretrained model like META LLAMA 2. Query Craft has managed to pull out important info from text and generated personalized questions that are appropriate as well as thoughtful. Because of this automation, there are now a lot hours saved off work for those who teach and those responsible for producing material.

# Implementation 
We have self-created the dataset ‘dataset.csv’.
The actions that were taken to prepare the dataset were as follows:
•	selection of different text inputs, such as paragraphs and PDFs.
•	extraction of pertinent textual content with PyPDF2 and other tools.
•	headers, footers, and special characters are eliminated during preprocessing.
•	Utilizing natural language processing methods to extract keywords.
•	The collected keywords are organized into paragraphs.
•	Using the keywords that were retrieved, questions are generated from each structured paragraph.
•	There are four possible answers (A, B, C, and D) for every multiple-choice question.
•	Subject matter experts validate questions to ensure correctness and applicability.
The prepared dataset screenshot is shown below:

![image](https://github.com/user-attachments/assets/214030be-38d9-4d1f-ab40-6a4405d68103)
Figure showing the prepared dataset including the following attributes
•	Questions
•	OptionA
•	OptionB
•	OptionC
•	OptionD
•	Answer
•	Explanation


# Project Architecture
![image](https://github.com/user-attachments/assets/3d719b29-917f-49ea-908c-bdc6b7c66384)

This Figure showing the process from input till we get the output. As shown in the figure firstly we prepare the actual dataset called as input data from the raw data after normalizing it. Then we try to split the data into training and testing part then after preprocessing, the preprocessed data then goes to the encoder and then goes to the decoder and as the model gets trained more the more accurately it generated the corresponding output.



# Results
![image](https://github.com/user-attachments/assets/af8da901-3b10-41bd-854d-cd338da717f2)

This figure shows the basic fronted landing page where user input the textual data and filling the proper information required and click on generate button.



![image](https://github.com/user-attachments/assets/90b93301-bc4e-4e37-a635-b410bfc017e6)

This is the example showing how the user has entered the passage and selected the features like the number of questions he/she wants, the type of question.



![image](https://github.com/user-attachments/assets/7cbd1f6b-ab82-491a-8bf9-4c45df174b7e)

The figure shows the final generated.txt file which has 3 questions as user entered before including the ques, Ans, options, explanations.



# Limitations
•	Difficulty of content: Craft queries process may find difficult such content that is complicated or is deeply specialized such that it needs an expert understanding for it to come up with pertinent queries. Thus, human interference or further development is needed so that the questions will be well asked.

•	Language Dependence: Query Craft’s effectiveness may differ across languages due to differences in grammar, syntax, and semantics, making it language-dependent. The tool requires language adaptation as well as ‘native” training data in order to perform well with non-English languages.

•	Data Bias in Training: The data on which Query Craft's machine learning processes are based affects how it functions and its ability to generalize. Biases in training data may result in question generation outcomes that are either misleading or unbalanced.


