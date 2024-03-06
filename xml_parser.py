import xml.etree.ElementTree as ET


def check_subtree_list(subtree_list, subtree_name):
    """
    Check wheter list of subtrees is empty and wheter it has more then one
    element.
    """

    assert isinstance(subtree_list, list)

    assert all([isinstance(subtree, ET.Element) for subtree in subtree_list])

    if len(subtree_list) == 0:
        raise NameError(f"No element tagged {subtree_name}")

    if len(subtree_list) > 1:
        raise ValueError(f"More then one xml elements tagged {subtree_name}")


def parse_perseus_xml(xml_file_path):
    """
    Parse documents in xml format, downloaded from
    https://www.perseus.tufts.edu/ .
    """

    # read a file
    xml_doc = ET.parse(xml_file_path)

    root = xml_doc.getroot()

    # find 'text' child
    text_subtree = [c for c in root.iter('text')]

    check_subtree_list(subtree_list=text_subtree, subtree_name='text')

    text_subtree = text_subtree[0]

    # find 'body' inside 'text'
    body_subtree = [c for c in text_subtree.iter('body')]

    check_subtree_list(subtree_list=body_subtree, subtree_name='body')

    body_subtree = body_subtree[0]

    # extract all paragraphs (element 'p')
    # (method findall returnes empty list)
    p_elements = [p for p in body_subtree.iter('p')]

    # extract text from paragraphs
    ptext = []
    for p_element in p_elements:
        ptext.extend([t for t in p_element.itertext()])

    # mergeing list elements into one corpus
    corpus = ' '.join(ptext)

    assert isinstance(corpus, str)

    # preliminary clean up: deleting \n
    corpus = corpus.replace('\n', '')

    return corpus
