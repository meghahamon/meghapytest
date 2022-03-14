from unicodedata import name
import postfix
def emptypostfix():
   ret = postfix.post_eval("")
   assert ret == None
def test_Charpostifix():
    ret = postfix.post_eval("abcde")
    assert ret == False
def test_postfix():
    ret = postfix.post_eval("123*+")
    assert ret == 7   
