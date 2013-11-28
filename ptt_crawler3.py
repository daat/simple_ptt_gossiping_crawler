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
tn.expect(["任意鍵繼續".encode("big5")], 3)
tn.write(b"\r\n")

#go to gossiping board
tn.write(b"sgossiping\r\n")
print("gossiping")

#skip welcome board
if tn.expect(["任意鍵繼續".encode("big5")], 0.5)[0] != -1:
	tn.write(b"\r\n")

tn.read_until("eqe toh ".encode("big5"), 1) #read the screen

f = open("0.txt", "w")
fn = 0;
begin_n = input("from(<0 for the latest one):")
if int(begin_n) > 0:
	tn.write(begin_n.encode("ascii")+b"\r")
tn.write("\u001b[C".encode("ascii")) #right arrow key, enter the first post

re_ansi = re.compile("\x1b\[[0-9;]*[mABCDHJKsu]")
re_cr = re.compile("\r")
p = 0
while(True):
	tn.read_until("eqe toh ".encode("big5"), 0.1)
	tn.write("\u000c".encode("ascii"))
	s = cn.decode(tn.read_until("eqe toh ".encode("big5"), 0.1))

	s = re.sub(re_ansi, "", s)
	s = re.sub(re_cr, "", s)
	last_line = s.find("瀏覽 第")
	if last_line != -1:
		s = s[:last_line]
	if "看板  Gossiping" in s:
		if "本板為PTT八卦板" in s:
			break
		f.close()
		fn = fn + 1
		f = open(str(fn)+".txt", "w")
#		if p == 0:
#			p = 1
#		else:
#			break
	elif "(b)進板畫面" in s:
		break
	else:	
		lines = s.rsplit("\n", 2)
		if len(lines) < 3:
			break
		s = lines[1]+"\n"
	print(s)
	f.write(s)
	tn.write("\u001b[B".encode("ascii")) #down arrow key

