DEFAULT_NUMBER = 100   ## You can change the number of words to be listed in the output !!!


stop_words = ['able', 'about', 'above', 'abroad', 'according', 'accordingly',
                  'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against',
                  'ago', 'ahead', 'aint', 'all', 'allow', 'allows', 'almost', 'alone',
                  'along', 'alongside', 'already', 'also', 'although', 'always', 'am',
                  'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any',
                  'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways',
                  'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are',
                  'arent', 'around', 'as', 'as', 'aside', 'ask', 'asking', 'associated',
                  'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards',
                  'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been',
                  'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below',
                  'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both',
                  'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', 'cant',
                  'caption', 'cause', 'causes', 'certain', 'certainly', 'changes',
                  'clearly', 'cmon', 'co', 'co', 'com', 'come', 'comes', 'concerning',
                  'consequently', 'consider', 'considering', 'contain', 'containing',
                  'contains', 'corresponding', 'could', 'couldnt', 'course', 'cs',
                  'currently', 'dare', 'darent', 'definitely', 'described', 'despite',
                  'did', 'didnt', 'different', 'directly', 'do', 'does', 'doesnt',
                  'doing', 'done', 'dont', 'down', 'downwards', 'during', 'each', 'edu',
                  'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end',
                  'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even',
                  'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything',
                  'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far',
                  'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed',
                  'following', 'follows', 'for', 'forever', 'former', 'formerly',
                  'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore',
                  'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going',
                  'gone', 'got', 'gotten', 'greetings', 'had', 'hadnt', 'half',
                  'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he',
                  'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter',
                  'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes',
                  'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit',
                  'however', 'hundred', 'id', 'ie', 'if', 'ignored', 'ill', 'im',
                  'immediate', 'in', 'inasmuch', 'inc', 'inc', 'indeed', 'indicate',
                  'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead',
                  'into', 'inward', 'is', 'isnt', 'it', 'itd', 'itll', 'its', 'its',
                  'itself', 'ive', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known',
                  'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least',
                  'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'likewise',
                  'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made',
                  'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'maynt', 'me',
                  'mean', 'meantime', 'meanwhile', 'merely', 'might', 'mightnt', 'mine',
                  'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs',
                  'much', 'must', 'mustnt', 'my', 'myself', 'name', 'namely', 'nd',
                  'near', 'nearly', 'necessary', 'need', 'neednt', 'needs', 'neither',
                  'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine',
                  'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone',
                  'noone', 'nor', 'normally', 'not', 'nothing', 'notwithstanding',
                  'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh',
                  'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'ones', 'only',
                  'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought',
                  'oughtnt', 'our', 'ours', 'ourselves', 'out', 'outside', 'over',
                  'overall', 'own', 'particular', 'particularly', 'past', 'per',
                  'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably',
                  'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather',
                  'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding',
                  'regardless', 'regards', 'relatively', 'respectively', 'right',
                  'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second',
                  'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems',
                  'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously',
                  'seven', 'several', 'shall', 'shant', 'she', 'shed', 'shell', 'shes',
                  'should', 'shouldnt', 'since', 'six', 'so', 'some', 'somebody', 'someday',
                  'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat',
                  'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying',
                  'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking',
                  'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that',
                  'thatll', 'thats', 'thats', 'thatve', 'the', 'their', 'theirs', 'them',
                  'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby',
                  'thered', 'therefore', 'therein', 'therell', 'therere', 'theres',
                  'theres', 'thereupon', 'thereve', 'these', 'they', 'theyd', 'theyll',
                  'theyre', 'theyve', 'thing', 'things', 'think', 'third', 'thirty',
                  'this', 'thorough', 'thoroughly', 'those', 'though', 'three',
                  'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together',
                  'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try',
                  'trying', 'ts', 'twice', 'two', 'un', 'under', 'underneath', 'undoing',
                  'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up',
                  'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using',
                  'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz',
                  'vs', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome',
                  'well', 'well', 'went', 'were', 'were', 'werent', 'weve', 'what',
                  'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever',
                  'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres',
                  'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while',
                  'whilst', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl',
                  'whom', 'whomever', 'whos', 'whose', 'why', 'will', 'willing', 'wish',
                  'with', 'within', 'without', 'wonder', 'wont', 'would', 'wouldnt',
                  'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre', 'yours',
                  'yourself', 'yourselves', 'youve', 'zero', 'a', 'hows', 'i', 'whens',
                  'whys', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o',
                  'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'i', 'www',
                  'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt',
                  'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen',
                  'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give',
                  'hasnt', 'herse', 'himse', 'interest', 'itse', 'mill', 'move', 'myse',
                  'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten',
                  'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance',
                  'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah',
                  'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent',
                  'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol',
                  'briefly', 'ca', 'date', 'ed', 'effect', 'etal', 'ff', 'fix', 'gave',
                  'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately',
                  'importance', 'important', 'index', 'information', 'invention', 'itd',
                  'keys', 'kg', 'km', 'largely', 'lets', 'line', 'll', 'means', 'mg',
                  'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted',
                  'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages',
                  'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present',
                  'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran',
                  'readily', 'ref', 'refs', 'related', 'research', 'resulted',
                  'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes',
                  'showed', 'shown', 'showns', 'shows', 'significant', 'significantly',
                  'similar', 'similarly', 'slightly', 'somethan', 'specifically',
                  'state', 'states', 'stop', 'strongly', 'substantially', 'successfully',
                  'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto',
                  'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til',
                  'tip', 'ts', 'ups', 'usefully', 'usefulness', 've', 'vol', 'vols',
                  'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words',
                  'world', 'youd', 'youre']

punct = """0123456789:;,.`+-()“!#$%&'*/<>=?[]\|_’“—^‘”"""

def convert_book_file_to_string(fileRead):  ## This function pulls data from the book. And assigns the retrieved data to a string.
    line = " "
    All = ""
    while line != "":
        line = fileRead.readline()

        All += line.strip('\n') + " "    ## combining words in text.

    All = All.lower()

    return All

def clean_punctuation_mark(stringText): ## This function removes punctuation marks from text held as strings.

    for i in range (len(punct)):
        stringText = stringText.replace(punct[i],"")

    return stringText

def remove_stop_words(words):   ## This function, deletes stop words from words array of words that are free of punctuation marks.
    cleanWords = []
    for i in range(len(words)):
        flagStop = False
        for j in range(len(stop_words)):
            if words[i] == stop_words[j]:    ## If stop words exist in text. flagStop = true.
                flagStop = True
                break
        if flagStop == False and words[i] != "":  ## If flag stop is equal false, and words[i] is not equal null.
            cleanWords.append(words[i])            ## add words in clearWords list.
    return cleanWords

def list_words_respect_to_order(cleanWords,WordOrder):  ##This function assigns cleared words to a new sequence based on the number of entered word orders.
    # This algorithm works according to the word order number.
    # let a b c d e f be a sequence of words.
    # Word order works as a-b-c-d-e-f if 1 is entered, list[0] = "a", list[1] = "b"
    # as ab-bc-cd-de-ef if 2 is entered, list[0] = "ab", list[1] = "bc"
    # as abc-bcd-cde-def if 3 is entered. list[0] = "abc", list[1] = "bcd"
    flag = True
    lowerLimit = 0
    upperLimit = WordOrder
    S = ""
    orderedWords = []
    while flag:
        for i in range(lowerLimit,upperLimit):
            S += cleanWords[i]    ## Words are collected in strings according to the given word order.
            if (i < upperLimit - 1):       ##  Let order word = 2, This prevents  word1 + space + word2 + space ( the last space should not be added).
                S += " "          ## So the S = word1 + space + word2
        orderedWords.append(S)    ## In a new list, it is assigned to an index.
        lowerLimit = lowerLimit + 1                 ## Increase lower and upper limits, when for loop end.
        upperLimit = upperLimit + 1
        S = ""
        if (upperLimit == len(cleanWords)):  ## When upperlimit equal to len(cleanWords), it will be stop and exit from loop.
            flag = False
            break
    return orderedWords

def assign_ordered_words_in_dictionary(orderedWords): ## Transferring the words thrown into the array according to Word order to the dictionary data structure.
    wordsDictionary = {}
    for i in range(len(orderedWords)):
        if (orderedWords[i] in wordsDictionary):      ## If key is exist, value += 1
            wordsDictionary[orderedWords[i]] += 1
        else:
            wordsDictionary[orderedWords[i]] = 1     ## If key is not exist, assign value = 1

    return wordsDictionary

def sort_and_print_output(dictionary,fileOutput): ## The words from the dictionary are taken ordered and printed to the output file.
    sortWords = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    ## As we know, the data added to the dictionary data structure is not added sequentially.
    ## So we need to scan dictionaries with nested loops and get a sort by the order of magnitude of the values.
    ## It takes as much time as log(n^2) to set up the sorting algorithm with loops. Because of this, we can use the sorted function and save time.
    ## In this function, we see the spelling x:x[1]. This is the dictionary structure itself. x = key and x[1] = value.
    ## The "Sorted" function allows us to perform a sort from the largest to the smallest value.

    count = 1

    fileOutput.write('{:<14}{:<14}{:<}'.format("| WORD", "| WORD","|") + "\n")
    fileOutput.write('{:<14}{:<14}{:<}'.format("| ORDER", "| ORDER","|") + "\n")
    fileOutput.write('{:<14}{:<14}{:<}'.format("| FREQUENCY", "| SEQUENCE" ,"|") + "\n")
    fileOutput.write("-----------------------------" + "\n")
    fileOutput.write('{:<14}{:<14}{:<}'.format("| <freq_bk_1>","| <word_list>","|") + "\n")

    for i in sortWords:
        if (count > DEFAULT_NUMBER):   ##DEFAULT_NUMBER was defined 100.
            break
        else:
            fileOutput.write('{:^14}{:^14}'.format(str(i[1]), i[0]) + "\n")    ## i[1] = value i[0] = key
            count = count + 1

def Word_Order_Frequency_One_Book(Book,WordOrder,FileOutput):

    if Book[-4:] != ".txt":
        print("""Wrong format! Please enter a file with the extension ".txt" \nError : """, Book)
        exit()
    if FileOutput[-4:] != ".txt":
        print("""Wrong format! Please enter a file with the extension ".txt" \nError : """, FileOutput)
        exit()
    try :
        fileRead = open(Book, "r", encoding='UTF8')
    except:
        print("Book 1 was not found \nThe program will be close")
        exit()
    try :
        fileOutput = open(FileOutput, "w", encoding='UTF8')
    except:
        print("The output file could not be created.\nThe program will be closed ")
        exit()


    allText = convert_book_file_to_string(fileRead)  ## Read the file and assign all the text to the all Textvariable.

    punctuationlessText = clean_punctuation_mark(allText) ## Cleaning Punctuation from all text.

    words = punctuationlessText.split(" ")  ##The text stored as a string is assigned word-by-word to the words array using the split method.


    cleanWords = remove_stop_words(words)  ##Remove the stop words from the Words array.

    orderedWords = list_words_respect_to_order(cleanWords,WordOrder)  ## Rebuilding the list according to word order.



    wordsInDictionary = assign_ordered_words_in_dictionary(orderedWords)  ## clean and ordered words in Dictionary.


    sort_and_print_output(wordsInDictionary,fileOutput)    ## Sorting algorithm and output function.

    fileRead.close()
    fileOutput.close()

def assign_books_in_two_dictionary(orderedWords1, orderedWords2): ## 2 assignment of separately sorted words of the book to the dictionary,

    ## Scaning words(book1) in dictionary.
    wordsDictionary1 = {}

    for i in range(len(orderedWords1)):
        if wordsDictionary1.__contains__(orderedWords1[i]):
            wordsDictionary1[orderedWords1[i]] += 1
        else:
            wordsDictionary1[orderedWords1[i]] = 1

    ## Scaning words(book2) in dictionary.

    wordsDictionary2 = {}

    for i in range(len(orderedWords2)):
        if wordsDictionary2.__contains__(orderedWords2[i]):
            wordsDictionary2[orderedWords2[i]] += 1
        else:
            wordsDictionary2[orderedWords2[i]] = 1

    ## Assignment of common words to a new dictionary
    dictionaryCommonWords = {}

    for key1 in wordsDictionary1:
        if key1 in wordsDictionary2:
            dictionaryCommonWords[key1] = wordsDictionary1[key1] + wordsDictionary2[key1]

    return dictionaryCommonWords,wordsDictionary1,wordsDictionary2

    for key1 in wordsDictionary1:
        if key1 in wordsDictionary2:
            dictionaryCommonWords[key1] = wordsDictionary1[key1] + wordsDictionary2[key1]

        else:
            wordsDictionary2[key1] = 0
            dictionaryCommonWords[key1] = wordsDictionary1[key1] + wordsDictionary2[key1]

    return dictionaryCommonWords, wordsDictionary1, wordsDictionary2

def two_book_sort_and_print_output(wordsDictionaryFinal,wordsDictionary1,wordsDictionary2,fileOutput):  ##writing and sorting of common words of 2 books according to the data of 2 books.
    sort_words = sorted(wordsDictionaryFinal.items(), key=lambda x: x[1], reverse=True)

    ## As we know, the data added to the dictionary data structure is not added sequentially.
    ## So we need to scan dictionaries with nested loops and get a sort by the order of magnitude of the values.
    ## It takes as much time as log(n^2) to set up the sorting algorithm with loops. Because of this, we can use the sorted function and save time.
    ## In this function, we see the spelling x:x[1]. This is the dictionary structure itself. x = key and x[1] = value.
    ## The "Sorted" function allows us to perform a sort from the largest to the smallest value.

    count = 1

    fileOutput.write('{:<14}{:<14}{:<14}{:<14}{:<}'.format("| TOTAL","| BOOK 1","| BOOK 2","| WORD","|") + "\n")
    fileOutput.write('{:<14}{:<14}{:<14}{:<14}{:<}'.format("| ORDER", "| ORDER", "| ORDER", "| ORDER","|") + "\n")
    fileOutput.write('{:<14}{:<14}{:<14}{:<14}{:<}'.format("| FREQUENCY", "| FREQUENCY", "| FREQUENCY", "| FREQUENCY","|") + "\n")
    fileOutput.write("---------------------------------------------------------" + "\n")
    fileOutput.write('{:<14}{:<14}{:<14}{:<14}{:<}'.format("|<freq_total>", "| <freq_bk_1>", "| <freq_bk_2>", "| <word_list>", "|") + "\n")
    for i in sort_words:
        if (count > DEFAULT_NUMBER):  ## DEFAULT_NUMBER was defined 100.
            break
        else:
            ## i[1] = value of common words, i [0] = keys (words)
            fileOutput.write('{:^14}{:^14}{:^14}{:^14}'.format(str(i[1]), str(wordsDictionary1[i[0]]),str(wordsDictionary2[i[0]]), i[0]) + "\n")

            count = count + 1

def Word_Order_Frequency_Two_Books(Book1, Book2, WordOrder,FileOutput):

    if Book1[-4:] != ".txt":
        print("""Wrong format ! Please enter a file with the extension ".txt" \nError (Book1 file) : """ , Book1)
        exit()
    if Book2[-4:] != ".txt":
        print("""Wrong format ! Please enter a file with the extension ".txt" \nError (Book2 file) : """, Book2)
        exit()
    if FileOutput[-4:] != ".txt":
        print("""Wrong format! Please enter a file with the extension ".txt" \nError (Output file) : """ , FileOutput)
        exit()
    try:
        fileRead1 = open(Book1, "r", encoding='UTF8')
    except:
        print("Book1 was not found\nThe program will be closed ")
        exit()
    try:
        fileRead2 = open(Book2, "r", encoding='UTF8')
    except:
        print("Book2 was not found\nThe program will be closed ")
        exit()
    try:
        fileOut = open(FileOutput, "w", encoding='UTF8')
    except:
        print("The output file could not be created.\nThe program will be closed ")
        exit()

    ## Read the files and assign all the texts to the all1 and all2 Textvariable.
    All1 = convert_book_file_to_string(fileRead1)
    All2 = convert_book_file_to_string(fileRead2)

    ## Cleaning Punctuation from book1 (All1) and book2 (All2)  text.
    All1 = clean_punctuation_mark(All1)
    words1= All1.split(" ")
    All2 = clean_punctuation_mark(All2)
    words2 = All2.split(" ")

    ##Remove the stop words from the Words arrays (words1 and words2).
    cleanWords1 = remove_stop_words(words1)
    cleanWords2 = remove_stop_words(words2)

    ## Rebuilding the lists according to word orders.
    orderedWords1 = list_words_respect_to_order(cleanWords1,WordOrder)
    orderedWords2 = list_words_respect_to_order(cleanWords2,WordOrder)

    ## Dictionary(book1) Dictionary(book2) and dictionary(book1+book2) --- > wordsDictionaryCommon are created.
    dictionaryCommonWords, wordsDictionary1, wordsDictionary2 = assign_books_in_two_dictionary(orderedWords1,orderedWords2)

    ## Sorting and printing outputs.
    two_book_sort_and_print_output(dictionaryCommonWords,wordsDictionary1,wordsDictionary2,fileOut)

    fileRead1.close()
    fileRead2.close()
    fileOut.close()




