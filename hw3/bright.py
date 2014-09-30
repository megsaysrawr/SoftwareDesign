# -*- coding: utf-8 -*-
"""
Homework 3: Data Mining
bright
Created on Mon Sep 29 20:47:47 2014

@author: Meg McCauley
"""
from pattern.web import*
from pattern.en import parse
import pickle

bright = URL('https://www.cs.drexel.edu/~introcs/F2K/placement/bright.txt').download()

f = open('bright.pickle','w')
pickle.dump(bright,f)
f.close()
input_file = open('bright.pickle','r')
reload = pickle.load(input_file)

# print bright #Testing data mining only

#Taking out the characters that aren't letters or spaces
bright_plain = bright.translate(None, ',.!":;')

def process_snippet(s):
    #Test code with simple string
    #s = 'The dog jumped over the moon' #comment out to use riddle
    s_array = s.split() # Takes a string and makes each word an entry in an array
    # print s #Testing only
    s_parsed = parse(s,relations=True,lemmata=True)
    return s_parsed,s_array

def replace_noun(s_parsed, s_array):
    '''
    What I Want:
    Input: 
    The output is the word/**/blah blah 
    I want to substring the ** and then check it against the parts of speech.
    '''
    word_count = 0
    flag = 1
    for index in range(len(s_parsed)):
        if flag and s_parsed[index]=='/':
            flag = 0
            part_of_speech = s_parsed[index+1:index+3];
            # print part_of_speech # identification only
            if part_of_speech == 'NN':
                new_noun = raw_input('Enter a noun: ')
                s_array[word_count] = new_noun
            if part_of_speech == 'VB':
                new_verb = raw_input('Enter a verb: ')
                s_array[word_count] = new_verb
        if s_parsed[index]==' ':
            flag = 1
            word_count+=1
    # Prints final edited snippet in a single line without array formatting
    print '\nThanks for playing! Here\'s your story: \n'+ ' '.join(s_array)

# RUN, RUN AS FAST AS YOU CAN!!!
if __name__ == "__main__":
    print 'Welcome to Meg\'s Mad Libs!: '
    snippet = bright_plain
    processed_snippet = process_snippet(snippet)
    replace_noun(processed_snippet[0], processed_snippet[1])
    
print '\nOriginal Story:\n' + bright_plain #Prints the non-edited snippet
