# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    texts = open("story.txt", "r")

    d = dict()

    for text in texts:

        text = text.strip()

        text = text.lower()

        words = text.split(" ")

        for word in words:
            if word in d:

                d[word] = d[word] + 1
            else:

                d[word] = 1

    for key in list(d.keys()):
        print(key, ":", d[key])




read_file_content("story.txt")
