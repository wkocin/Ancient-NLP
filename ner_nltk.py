# HELPER FUNCTION USED FOR NER WITH NLTK
import nltk
import pandas as pd


def preprocess(corpus):
    """
    Tokenization and POS tagging using nltk methods.

    A list is returned.
    """
    tokenized_corpus = nltk.word_tokenize(corpus)

    tagged_corpus = nltk.pos_tag(tokenized_corpus)

    return tagged_corpus


def extract_lables(ne_chunk_tree):
    """
    Extract the laabelled catogires from a product of nltk.ne_chunk().

    A pandas.DataFrame is returned.
    """
    words = []
    labels = []

    for tree in ne_chunk_tree:
        if isinstance(tree, nltk.tree.tree.Tree):

            assert len(tree) == 1

            words.append(tree[0][0])
            labels.append(tree.label())

    labels_table = (
        pd.DataFrame({'words': words, 'labels': labels}).
        drop_duplicates()
    )

    return labels_table
