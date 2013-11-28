#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
#vim set fileencoding=utf-8:

import telnetlib
import getpass
import Cnencoding
import re

HOST = "ptt.cc"

tn = telnetlib.Telnet(HOST)
cn = Cnencoding.Cnencoding()

#log in
print(chr(27)+"[2J")
while(True):
	user = input("Username:")
	password = getpass.getpass()
	tn.expect(["請輸入代號".encode("big5")])
	tn.write(user.encode("ascii")+b"\r")

	tn.expect(["您的密碼".encode("big5")])
	tn.write(password.encode("ascii")+b"\r")
# if username or password is wrong
	t = tn.expect(["密碼不對".encode("big5")], 0.5)
	if t[0] != -1:
		print("Wrong username or password")
		continue
	break

if tn.expect(["刪除其他重複登入的連線嗎".encode("big5")], 0.5)[0] != -1:
	tn.write(b"Y\r")

print("log in successfully")
#log in successfully, press any key to continue;
tn.expect(["任意鍵繼續".encode("big5")], 1)
tn.write(b"\r\n")

#go to gossiping board
tn.write(b"sgossiping\r\n")
#skip welcome board
if tn.expect(["任意鍵繼續".encode("big5")], 0.5)[0] != -1:
	tn.write(b"\r\n")

tn.read_until("eqe toh ".encode("big5"), 1) #read the screen
f = open("1.txt", "w")
tn.write("\u001b[C".encode("ascii")) #right arrow key
s = cn.decode(tn.read_until("eqe toh ".encode("big5"), 1))
f.write(s)
tn.write("\u001b[B".encode("ascii")) #down arrow key
s = cn.decode(tn.read_until("eqe toh ".encode("big5"), 1))
f.write(s)
tn.write("\u001b[B".encode("ascii"))
s = cn.decode(tn.read_until("eqe toh ".encode("big5"), 1))
f.write(s)
tn.write("\u001b[B".encode("ascii"))
s = cn.decode(tn.read_until("eqe toh ".encode("big5"), 1))
f.write(s)
tn.write("\u001b[B".encode("ascii"))
s = cn.decode(tn.read_until("eqe toh ".encode("big5"), 1))
f.write(s)

