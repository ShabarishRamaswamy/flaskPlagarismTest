from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
from scipy import spatial
import gensim.downloader as api
from gensim.models import doc2vec
from nltk.corpus import stopwords  
import spacy
from app import *


def givejson():
    nlp = spacy.load('en_core_web_md')
    final = {}

    d2v_model = doc2vec.Doc2Vec.load('d2v.model')
    extras = set(stopwords.words('english'))

    jss = app.inputValues() #json
    #jss = {"A":"Hello,it's me","B":"Hi, how are you?","C":"Greetings!"}

    for i in range(len(jss)):
        l1 = []
        for j in range(len(jss)):
            if i!=j:
                first_text = jss[list(jss.keys())[i]]
                second_text = jss[list(jss.keys())[j]]
                #print('"'+first_text+'"'+'"'+second_text+'"',end=":")
                fn1_doc = first_text.split(' ')
                f1 = [word for word in fn1_doc if word not in extras]
                fn2_doc = second_text.split(' ')
                f2 = [word for word in fn2_doc if word not in extras]
                
                doc1 = nlp(''.join(map(str,f1)))    
                doc2 = nlp(''.join(map(str,f2)))
                spacysim = doc1.similarity(doc2)
                #print(spacysim)

                vec1 = d2v_model.infer_vector(first_text.split())
                vec2 = d2v_model.infer_vector(second_text.split())

                d2vsim = spatial.distance.cosine(vec1, vec2)
                #print(d2vsim)

                if 100*spacysim==100:
                    l1.append(spacysim*100)
                elif 100*d2vsim==100:
                    l1.append(d2vsim*100)
                elif (70*d2vsim + 30*spacysim) <= 100:
                    l1.append(round(70*d2vsim + 30*spacysim))
                elif 100*spacysim>=80:
                    l1.append(round(spacysim*100))
                elif 100*d2vsim<=100:
                    l1.append(round(d2vsim*100))
        final[first_text]=l1

    #print(final)
    return final



#givejson()
