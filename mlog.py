#!/usr/bin/python3
import json
import os

def main():
	def check_file_exsistence():
		file="data.txt"
		check=os.path.isfile(file)
		if check:return file
		exit()
	fname=check_file_exsistence()
	
	def get_content(file):
		f=open(file)
		a=f.readlines()  
		for i in a:
			string=" "  
			string+=i
		return string
	get=get_content(fname)
		
	def get_symbols_count(a):
		count={}
		for l in a:     
			n=a.count(l)
			count[l]=n       
		return count
	symbol=get_symbols_count(get)
	
	def get_longest_word(a):
		string1 =a.split()
		longest=0
		for long in string1:
			if len(long)>longest:
				longest==len(long)
				wlong=long
		return wlong
	long_word=get_longest_word(get)

	def get_sentences_count(a):
		
		string2=a.split(".")
		c=str(len(string2))
		return c
	sentence=get_sentences_count(get)

	def get_text_with_words_reversed(a):
		string3 =a.split()
		reverse=""
		for rev in string3:
			rev=rev[ ::-1]
			reverse+=rev+" "
		return reverse
	reversed=get_text_with_words_reversed(get)

	def write_into_file(a,b,c,d):
		with open("result.txt", "w") as file:
			file.write(a+"\n")
			file.write("Long Word is: "+b+"\n")
			file.write(c+"\n")
			file.write(json.dumps(d))
	write_into_file(reversed,long_word,sentence,symbol)
main()