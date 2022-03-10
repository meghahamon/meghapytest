
import programs
def testSame():
    ret = programs.counts("aaa")
    assert ret== {"a":3}

def testMultiple():
    ret = programs.counts("aaabbcccc")
    assert ret == {"a":3,"b":2,"c":4}
        
def testEmpty():
    ret = programs.counts("")
    assert ret == {} 

def  testSuccessFulPanagram():
    ret = programs.panagram("qwertyuiopasdfghjklzxcvbnm")
    assert ret == True
    
def  testFalsePenagram():
    ret = programs.panagram("qwertyuiopasdfghjklzxcvbn")
    assert ret == False

def testAverage():
    ret = programs.average( [10, 10] )
    assert ret == 10
def  testFalseAverage():
    ret = programs.average( [-10,-10])
    assert ret != -20   
def testEmptyAverage():
    ret = programs.average([])
    assert ret == None
