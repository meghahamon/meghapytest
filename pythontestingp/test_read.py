import read_index
def testempty():
    ret = read_index.ncharsempty("")
    assert ret == None
def testalpha():
    ret = read_index.alphachar("!@#$%") 
    assert ret == False
def testnum():
    ret = read_index.nchar("2adfg67")
    assert ret == 7
def testnwordsempty():
    ret = read_index.nwordsempty("")
    assert ret ==None
def testword():
    ret = read_index.nwords("Earn each day")
    assert ret == 2
def testemptysentence():
     ret=read_index.emptysentence('asdasfda pqrstuvwazjdjd')
     assert ret==None
def testsentence():
     ret=read_index.numsentences('What is yor name? Where are you going? I m good.be happy!')
     assert ret== 4
    


