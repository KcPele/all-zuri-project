# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here
    content = ''
    with open(filename, mode='r') as f:
         content = f.read()
    
    return content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    #split words and put them in an array
    texts = " ".join(text.split()).replace(',', '').replace('.', '')
    print(texts)
    splited_texts = texts.split(' ')
    # get the set of unque words and count there apperance in the splited texts
    result = dict((i, splited_texts.count(i)) for i in set(splited_texts))

    return result

