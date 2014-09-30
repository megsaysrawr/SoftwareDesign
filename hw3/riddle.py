# -*- coding: utf-8 -*-
"""
Homework 3: Data Mining
riddle
Created on Mon Sep 29 20:47:47 2014

@author: Meg McCauley
"""
from pattern.web import*
from pattern.en import parse
import pickle
import array


def get_snippet():
    # Data Mining from set website
    riddle = URL('https://www.cs.drexel.edu/~introcs/F2K/placement/riddle.txt').download()
    
    # Save snippet by pickling it
    f = open('riddle.pickle','w')
    pickle.dump(riddle,f)
    f.close()
    input_file = open('riddle.pickle','r')
    reload = pickle.load(input_file)
    return riddle #add back in to use without hard code


def get_offline_snippet():
    riddle = open('/home/megsaysrawr/SoftwareDesign/hw3/riddle.pickle','r')
    print riddle.read()
    riddle_plain = riddle.translate(None, ',.!":;')
    print riddle_plain
    
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
        if s_parsed[index]==' ':
            flag = 1
            word_count+=1
    # Prints final edited snippet in a single line without array formatting
    print '\nThanks for playing! Here\'s your story: \n'+ ' '.join(s_array)

# RUN, RUN AS FAST AS YOU CAN!!!
if __name__ == "__main__":
    print 'Welcome to Meg\'s Mad Libs!: '
    snippet = get_offline_snippet()
    processed_snippet = process_snippet(snippet)
    replace_noun(processed_snippet[0], processed_snippet[1])
