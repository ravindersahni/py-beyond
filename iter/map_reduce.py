__author__ = 'instancetype'


def count_words(doc):
    normalized_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    for word in normalized_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

documents = [
    'Here is some random text that I am writing.',
    'Nothing to see here really... nope nope nope.',
    'Hmm, I wonder why Jitsu is making so much noise.',
    'I should probably go to sleep soon, yeah?'
]

counts = map(count_words, documents)

def combine_counts(d1, d2):
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d