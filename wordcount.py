def words(sentence):
    modified_sentence = ' '.join(sentence.split())
    words_list = modified_sentence.split(" ")
    output = {}
    for d in range(0, len(words_list)):
        word = words_list[d]
        if word in output: continue
        try:
            output[int(word)] = words_list.count(word)
        except:
            output[word] = words_list.count(word)
    return output
