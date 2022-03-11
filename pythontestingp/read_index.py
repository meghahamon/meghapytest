import math
def ncharsempty(char):
    if len(char) == 0:
     return None
def alphachar(char):
        if not char.isalnum():
          return False
def nchar(char):
  acc = 0
  for i in char:
    acc+=1
  return acc
def nwordsempty(char):
  if " " not in char:
    return None
def nwords(char):
  acc = 0
  for i in char:
    if i ==' ':
      acc+=1
  return acc
def emptysentence(char):
     if "." or "!" or"?" not in char:
          return None         
def numsentences(char):
     acc=0
     for i in char:
      if i == '!' or i == '?' or i == '.':
          acc+=1
     return acc
def calculation(string):
  index= math.ceil(4.71*(nchar(string)//nwords(string))+0.5*(nwords(string)//numsentences(string))-21.43)
  dict={
          1:"5-6 Kindergarten",
          2:"6-7 First Grade",
          3:"7-8 Second Grade",
          4:"8-9 Third Grade",
          5:"9-10 Fourth Grade",
          6:"10-11 Fifth Grade",
          7:"11-12 Sixth Grade",
          8:"12-13 Seventh Grad",
          9:"13-14 Eighth Grade",
          10:'14-15 Ninth Grade',
          11:'15-16 Tenth Grade',
          12:'16-17 Eleventh Grade',
          13:'17-18 Twelfth Grade',
          14:'18-22 College student'
          }
  return dict[index]













