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
		source = bytearray(s)
		print source
		while(i<len(source)-1):
			if(source[i]>=0x81 and source[i]<=0xfe and source[i+1]>=0x40 and source[i+1]<=0xfe):
#				dest+= str(self.ucs[((source[i])<<8|source[i+1])-33088])
				dest += str(source[i:i+1], encoding="big5")
				i = i+1
				n = n+1
			else:
				dest+=str(source[i])
				if i==len(source)-2:
					i = i+1
					dest+=str(source[i])
			i=i+1
		print(n)
		return dest


class main:
	import telnetlib2
	import getpass
	HOST = "ptt.cc"

	tn = telnetlib2.Telnet(HOST)
	cn = Cnencoding()

	print cn.decode(u"我".encode("big5"))

#log in
	while(True):
		user = raw_input("Username:")
		password = getpass.getpass()
		tn.expect([u"請輸入代號".encode("big5")])
		tn.write(user+"\r")

		tn.expect([u"您的密碼".encode("big5")])
		tn.write(password+"\r")
# if username or password is wrong
		t = tn.expect([u"密碼不對".encode("big5")], 0.5)
		if t[0] != -1:
			print "Wrong username or password"
			continue
		break

#if tn.expect([u"刪除其他重複登入的連線嗎".encode("big5")], 0.5)[0] != -1:
#	print "other"
#	tn.write("Y\r")

	print "log in successfully"
#log in successfully, press any key to continue;
	tn.expect([u"任意鍵繼續".encode("big5")], 1)
	tn.write(b" \r\n")

	print (tn.expect([u"jiahborg".encode("big5")], 1))[2].decode("utf-8")
	#print(tn.read_until("任意鍵繼續".encode("big5"), 1).decode("big5"))
