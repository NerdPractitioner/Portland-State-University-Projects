def check_word_horizontal(ws,word,i,j):
    for w_i in range(len(word)):
        if ws[i][j] != word[w_i]:
            return False
        i+=0
        j+=1
    return True

def check_word_vertical(ws,word,i,j):
    for w_i in range(len(word)):
        if ws[i][j] != word[w_i]:
            return False
        i+=1
        j+=0
    return True


def check_word_diagonal(ws,word,i,j):
    for w_i in range(len(word)):
        if ws[i][j] != word[w_i]:
            return False
        i+=1
        j+=1
    return True



def check_word_reversehorizontal(ws,word,i,j):
    for w_i in range(len(word)):
        if ws [i][j] != word[w_i]:
            return False
        i+=0
        j+=-1
    return True

def pad_wordsearch(ws):
    padding_top = "-"*len(ws[0])
    padding_bottom = "-"*len(ws[0])

    ws.insert(0,padding_bottom)
    ws.append(padding_bottom)
        
    for i in range(len(ws)):
        ws[i] = "-" + ws[i] + "-"


def check_word(ws,i,j,di,dj,word):
#    last_position = len(word)-1
#    if not (last_position*di+i < n and 
#            last_position*di+i >=0 and 
#            last_position*dj+j < n and 
#            last_position*dj+j >=0):
#        print ("Out of bounds")
#        return False
    
    for w_i in range(len(word)):
        if ws[i][j] != word[w_i]:
            return False
        i+=di
        j+=dj
    
    return True


def contains_word(ws,word):
    return False

wordsearch= ["cate",
             "apen",
             "peao",
             "ptao"]
#pad_wordsearch(wordsearch)
m = len(wordsearch)
n = len(wordsearch[0])

        
    
