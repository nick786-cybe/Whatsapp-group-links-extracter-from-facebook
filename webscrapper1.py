import http.cookiejar
import random
import os
from colored import fg
import urllib.request
import requests
import bs4
import time
print('____________________________________')
print('Facebook to whatsapp links extracter')
print('____________________________________')
print('<<<<<Created By Nikhil Rathore>>>>>>>')
print('____________________________________')
color = fg('light_green')
color1 = fg('light_blue')
color2 = fg('light_red')
color3 = fg('yellow')
cj = http.cookiejar.CookieJar()
def login():
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)
    authentication_url = "https://m.facebook.com/login.php"
    idd = input('Enter Your Id number: 1/2:')

    #idd = random.choice(['1','2','3','4','5','7','8',''])
    print('ID:',idd)
    
    if idd == '1':
        payload = {
            'email':"anartemp161@gmail.com",
            'pass':"9920948068"  
        }

    elif idd == '2':
        payload = {
        
            'email':"anartemp121@gmail.com",
            'pass':"9920948068"   
        }


    data = urllib.parse.urlencode(payload).encode('utf-8')
    req = urllib.request.Request(authentication_url, data)
    resp = urllib.request.urlopen(req)
    contents = resp.read()


def vpn():
    codeList = [ "US-C", "US", "US-W"]
    try:
	    # connect to VPN
	    #os.system("windscribe connect")

	    # assigning a random VPN server code
	    choiceCode = random.choice(codeList)
	    # connecting to a different VPN server
	    print("!!! Changing the IP Address........")
	    os.system("windscribe connect ")#+ choiceCode)
            #os.system("windscribe disconnect")
    except Exception as e:
        #print(e)
	    os.system("windscribe disconnect")
	    print("sorry, some error has occurred..!!")

def comment_scrape(url):
    commen = 0
    blue = True
    link = ''
    count1 = 0
    url = url.replace('https://www.facebook.com','https://mbasic.facebook.com')
    print('--------------------------------------------------------------')
    while blue:
            blue = False
            try:
                data = requests.get(url)#,cookies=cj)
                soup = bs4.BeautifulSoup(data.content,'html.parser')
            except Exception:
                print('Trying to connect..')
                continue
            for i in soup.find_all('a',href=True):
                #print(i.text)
                if 'पिछली टिप्पणियाँ देखें…' in i.text:
                    #print(i.text)
                    #pages += i['href']+'\n'
                    url = i['href']
                    blue = True

                if 'उत्तर' in i.text:
                    print(i.text)
                    if 'https://mbasic.facebook.com' not in i['href']:
                        commen = 'https://mbasic.facebook.com'+(i['href'])
                        with open("comments.txt","a",encoding="utf-8")as f:
                            f.write('\n')
                            f.write(str(commen))
                            f.write('\n')
                            f.write(i.text)
                            f.close()
                    else:
                        with open("comments.txt","a",encoding="utf-8")as f:
                            f.write('\n')
                            f.write(str(commen))
                            f.write('\n')
                            f.write(i.text)
                            f.close()
                if 'जवाब' in i.text:
                    print(i.text)
                    if 'https://mbasic.facebook.com' not in i['href']:
                        commen = 'https://mbasic.facebook.com'+(i['href'])
                        with open("comments.txt","a",encoding="utf-8")as f:
                            f.write('\n')
                            f.write(str(commen))
                            f.write('\n')
                            f.write(i.text)
                            f.close()
                    else:
                        with open("comments.txt","a",encoding="utf-8")as f:
                            f.write('\n')
                            f.write(str(commen))
                            f.write('\n')
                            f.write(i.text)
                            f.close() 
                if 'https://chat.whatsapp.com' in i.text:
                    if (i.text) not in link:
                        count1 = count1+1
                        link += (i.text)+'\n'
                        print(color + 'found',i.text,count1)
                        with open("links.txt","a", encoding="utf-8")as f:
                            f.write('\n')
                            f.write(i.text)
                if i.text == 'Forgotten password?':
                    print('You are logged out')
                    time.sleep(10)
                    
                if i.text == 'पासवर्ड भूल गए?':
                    print('You are logged out')
                    time.sleep(10)
                    
                if i.text == 'टाइमलाइन देखें':
                    break

count = 0
def search_url():
    tri = ''
    add = 0
    comments = ''
    comment = ''
    link = ''
    count1 = 0
    a_file = open("url.txt",encoding='utf-8')
    lines = a_file.readlines()
    url = input("enter Your Group URL:" + color1)
    url = url.replace('https://www.facebook.com','https://mbasic.facebook.com')
    count = int(input(color1 +'Enter pages in no:'))
    print(url)
    a_file = open("url.txt",encoding='utf-8')
    lines = a_file.readlines()
    for line in lines:
        if url in line:
            answer = input("You have used this url do you still wan't to continue (y/n):")
            if answer ==  'y':
                pass
            else:
                search_url()
            break
        else:
            if url not in tri:
                tri += url
                with open("url.txt","a", encoding="utf-8")as f:
                    f.write('\n')
                    f.write(url)
                    

    index = 0
    while(index < count):
        try:
            data = requests.get(url)
            soup = bs4.BeautifulSoup(data.content,'html.parser')#,cookies=cj)
        except Exception:
            print('Trying to connect..')
            continue
        
        #print(soup.text)
        for i in soup.find_all('a',href=True):
            print(i.text)
            if 'Comments' in i.text:
                #print(i.text)
                if (i['href']) not in comment:
                     comment_scrape(i['href'])  
                     comment += (i['href'])
        

                                    
                         


            if 'टिप्पणियाँ' in i.text:
                print(i.text)
                if (i['href']) not in comment:
                     comment_scrape(i['href'])  
                     comment += (i['href'])
                     print(color3 + i.text,'saved')
                
                
            if 'https://chat.whatsapp.com/' in i.text:
                if (i.text) not in link:
                    count1 = count1+1
                    link += (i.text)+'\n'
                    print(color + 'found',i.text,count1)
                    with open("links.txt","a", encoding="utf-8")as f:
                        f.write('\n')
                        f.write(i.text)
            if i.text == 'Forgotten password?':
                print('You are logged out')
                input('enter to continue:')
                
            if i.text == 'पासवर्ड भूल गए?':
                print('You are logged out')
                input('enter to continue:')
            
            if i.text == 'let us know':
                print(i.text)
                input('enter to continue:')

            if i.text == '忘記密碼？ ':
                print(i.text)
                input('enter to continue:')
                         
            if i.text == 'See more posts':
                url = 'https://mbasic.facebook.com' +i['href']
                break
            if i.text == 'अधिक पोस्ट देखें':
                url = 'https://mbasic.facebook.com' +i['href']
                break
        index = index+1
        if index == count:
            print(index)
            f.close()
            count = int(input(color1+"Do you wan't to add more page? add NUMBER:"+color2))
#login() 
while True:
  try:
    search_url()
  except Exception as e:
      e = str(e)
      print(color2 + e)
      
    




