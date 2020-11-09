import pandas as pd


def read_and_load_annotation(filename):
    if filename == "143048389142134785.ann":
        return {'topics' : [{ 'name' : "élection de #missfrance", 'opinion':'negative' }], 'negative_keywords': ["pas plaisir"], 'positive_keywords':["plaisir"]}
    else:
        return {'topics' : [{ 'name' : "Languedoc", 'opinion':'positive' },{ 'name' : "Nord-Pas-De-Calais", 'opinion':'negative' } ], 'negative_keywords': ["pas aime"], 'positive_keywords':["jolie", "aime"]}

def load_tweet_with_annotation (id):
    dic = {}
    dic["id"] = id
    dic["text"] = ""
    dic["annotation"] = read_and_load_annotation(str(id.ann))
    return dic

def load_corpus_in_dataframe (dic):
    return pd.DataFrame(dic)