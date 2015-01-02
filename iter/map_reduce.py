__author__ = 'instancetype'

from functools import reduce


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

def main():
    total_counts = reduce(combine_counts, counts)
    for word, count in total_counts.items():
        print('{}: {}'.format(word, count))

if __name__ == '__main__':
    main()