import os.path
import csv
from textblob import TextBlob

i=1
file=input("Enter file name? ")

if(os.path.isfile(file)):  ##if file is non-existent, exit program
    with open(file, 'r') as myfile:
        r1 = str(myfile.read()) 
        print('File content is:\n',r1, '\n\n')

        r2 = TextBlob(r1)
        for sentence in r2.sentences:
            if (sentence.correct() != sentence):
                print("Incorrect spelling in - ", sentence)
            if (sentence.sentiment.polarity > 0):
                out='Positive'
            else:
                if (sentence.sentiment.polarity<0):
                    out='Negative'
                else:
                    out='Neutral'
            print(str(i),":",sentence.correct()," is ", out )
            i=i+1
        myfile.close()
else: 
    print("File not found.Exit program")
 