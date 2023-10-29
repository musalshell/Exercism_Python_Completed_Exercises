"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Add the prefix 'un' to the given word."""
    return "un" + word
   


def make_word_groups(vocab_words):
    """Create word groups with common prefixes."""
    prefix = vocab_words[0]
    words = vocab_words[1:]
    prefixed_words = [prefix + word for word in words]
    return f"{prefix} :: {' :: '.join(prefixed_words)}"




def remove_suffix_ness(word):
    """Remove 'ness' suffix and handle special cases."""
    root = word[:-4]  # Remove 'ness'
    if root[-1] == 'i':
        return root[:-1] + 'y'
    return root


import string

def adjective_to_verb(sentence, index):
    """Extract an adjective and convert it to a verb."""
    words = sentence.split()
    adjective = words[index].translate(str.maketrans('', '', string.punctuation))
    return adjective + "en"