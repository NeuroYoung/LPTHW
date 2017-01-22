import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):" :
     "Make a class named %%% that is-a %%%.",
    "class %%%(object): \n\tdef __init__(self, ***)" :
     "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object): \n\tdef ***(self, @@@)":
     "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
     "Set *** to an instance of class %%%.",
    "***.***(@@@)":
     "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
     "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))] # list comprehension
    other_names = random.sample(WORDS, snippet.count("***")) # random.sample() Return a k length list of unique elements chosen from the population sequence or set. Used for random sampling without replacement.


    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3) # Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]
        print "result =", result, " 'end!' " # debug

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1) # str.replace() str.replace(old, new[, max]) If this optional argument max is given, only the first count occurrences are replaced.

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)
        #print results # debug

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            # print "snippet =", snippet # debug
            # print "phrase =", phrase  # debug
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            raw_input(" > ")
            print("ANSWER: {!s}\n\n" .format(answer))
except EOFError:
    print("\nBye")
