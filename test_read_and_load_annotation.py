from corpusutils import read_and_load_annotation, load_tweet_with_annotation, load_corpus_in_dataframe
from pytest import *
from coverage import *
from pytest_cov import *


def test_read_and_load_annotation():
    # Given
    filename = "143048389142134785.ann"
    # When
    annotations = read_and_load_annotation(filename)
    #Then
    assert annotations == {'topics' : [{ 'name' : "élection de #missfrance", 'opinion':'negative' }], 'negative_keywords': ["pas plaisir"], 'positive_keywords':["plaisir"]}
    # Given
    filename1 = "143059118180139008.ann"
    # When
    annotations1 = read_and_load_annotation(filename1)
    #Then
    assert annotations1 == {'topics' : [{ 'name' : "Languedoc", 'opinion':'positive' },{ 'name' : "Nord-Pas-De-Calais", 'opinion':'negative' } ], 'negative_keywords': ["pas aime"], 'positive_keywords':["jolie", "aime"]}


def test_load_tweet_with_annotation():
    return

def test_load_corpus_in_dataframe ():
    return
