#!/usr/bin/python

def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_words(words):
	word = words.pop(0)
	print word

def print_last_words(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print words

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	words = sort_sentencee(sentence)
	print_first_word(words)
	print_last_word(words)
