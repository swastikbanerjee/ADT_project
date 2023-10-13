import nltk
import string
import re
import os
# from django.http import HttpResponse
from sentence_transformers import SentenceTransformer, util
from nltk.stem import WordNetLemmatizer
import sqlite3

# HttpResponse('hello!')

def remove_punctuation(text):
  text = text.lower()
  punctuationfree="".join([i for i in text if i not in string.punctuation])
  return punctuationfree

def tokenization(text):
  tokens = re.split(' ',text)
  return tokens

def remove_stopwords(text):
  stopwords = nltk.corpus.stopwords.words('english')
  output = []
  for i in text:
    if i in stopwords:
      continue
    output.append(i)
  return output

def lemmatizer(text):
  wordnet_lemmatizer = WordNetLemmatizer()
  lemm_text = [wordnet_lemmatizer.lemmatize(word) for word in text]
  return lemm_text

def preprocessing(text):
  return lemmatizer(remove_stopwords(tokenization(remove_punctuation(text))))

def paraf(text1, text2):
    model = SentenceTransformer('paraphrase-MiniLM-L12-v2')
    return util.paraphrase_mining(model, [text1, text2])[0][0]

def gen(text1, text2):
    text1 = preprocessing(text1)
    text2 = preprocessing(text2)
    return paraf(text1, text2)

def generate_report(id, txarr):
    rep = {}
    for i in range(len(txarr)):
        rep[i] = gen(txarr[id], txarr[i])
    dict(sorted(rep.items(), key=lambda x:x[1], reverse=True))
    del rep[id]
    return rep


# folder_path = 'C:\StrangerCodes\ADT\Cherry\media\students'
file_contents = []
folder_path = 'C:/StrangerCodes/ADT/Cherry/media'
def readcontent(path):
    # for filename in os.listdir(path):
    #     if filename.endswith(".txt"):
    #         file_path = os.path.join(folder_path, filename)
    path = os.path.join(folder_path, path)
    with open(path, 'r') as file:
        file_content = file.read()
        file_contents.append(file_content)
    # for index, content in enumerate(file_contents):
    #     print(f"Content of file {index}:\n{content}")

con = sqlite3.connect('C:\StrangerCodes\ADT\Cherry\db.sqlite3', timeout=30)
cur = con.cursor()
res = cur.execute('SELECT * FROM evaluate_assignment')
rows = res.fetchall()
names = []
for i in range(len(rows)):
    names.append(rows[i][1])

for i in range(len(rows)):
    readcontent(rows[i][2])
con.commit()
cur.close()
con.close()

gen = generate_report(0, file_contents)

for i,j in gen.items():
    print('Plagiarism with',names[i],'is',j,'<br>')