#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
#vim set fileencoding=utf-8:
class Cnencoding:
	ucs = []
#	def __init__(self):
#		uao = open("big5uao", "rb")
#		i = 0
#		while(True):
#			c = uao.read(2)
#			b = bytes(c);
#			if b== b"":
#				break
#			self.ucs.append(b)
#			i = i+1

	def decode(self, s):
		dest=""
		i = 0
		n = 0
		source = bytes(s)
#		print(source)
		while(i<len(source)-1):
			if(source[i]>=0x81 and source[i]<=0xfe and source[i+1]>=0x40 and source[i+1]<=0xfe):
#				dest+= str(self.ucs[((source[i])<<8|source[i+1])-33088])
				t = source[i:i+2]
				try:
					tt = str(t, "big5hkscs")
				except:
					dest+=chr(source[i])
					if i==len(source)-2:
						i = i+1
						dest+=chr(source[i])
				
#				print(tt)
				dest += tt
				i = i+1
				n = n+1
			else:
				dest+=chr(source[i])
				if i==len(source)-2:
					i = i+1
					dest+=chr(source[i])
			i=i+1
#		print(n)
		return dest

