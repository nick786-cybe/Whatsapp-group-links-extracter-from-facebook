import http.cookiejar
from colored import fg
import urllib.request
import requests
import bs4

color = fg('light_green')
color1 = fg('light_blue')
color2 = fg('light_red')
color3 = fg('yellow')
cj = http.cookiejar.CookieJar()
def login():
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)
    authentication_url = "https://m.facebook.com/login.php"
    idd = input('Enter Your Id number: 1/2/3/4:')


    if idd == '1':
        payload = {
            'email':"8574310086",
            'pass':"786786786"
        }

    elif idd == '2':
        payload = {
        
            'email':"anartemp161@gmail.com",
            'pass':"9920948068"   
        }
    elif idd == '3':
        payload = {
            'email':"lovishgarg0709@gmail.com",
            'pass':"subscribemychannel"
        }
    elif idd == '4':
        payload = {
            'email':"nick.r786",
            'pass':"apjabdulkapam"
        }
    else:
        payload = {
            'email':"nikhilrathour024@gmail.com",
            'pass':"786786786"
        }

    data = urllib.parse.urlencode(payload).encode('utf-8')
    req = urllib.request.Request(authentication_url, data)
    resp = urllib.request.urlopen(req)
    contents = resp.read()


count = 0
def search_url():
    comments = ''
    comment = ''
    link = ''
    count1 = 0
    url = input("enter Your Group URL:" + color1)
    url = url.replace('https://www.facebook.com/','https://mbasic.facebook.com/')
    count = int(input(color1 +'Enter pages in no:'))
    a_file = open("url.txt")
    lines = a_file.readlines() 

    with open(f"url.txt","a")as f:
            f.write('\n')
            f.write(url)
            f.close()
    a_file.close()
 
    index = 0
    

    while(index < count):
        #print(index)
        data = requests.get(url,cookies=cj)
        soup = bs4.BeautifulSoup(data.content,'html.parser')
        #print(soup.text)
        for i in soup.find_all('a',href=True):
            #print(i.text)
            if 'Comments' in i.text:
                print(i.text)
                if (i['href']) not in comment:
                    numeric_filter = (i.text[0:2])
                    numeric_filter = int(numeric_filter)
                    if numeric_filter > 10:
                        comments = (i['href'])
                        comment += (i['href'])
                        comments = comments.replace('https://mbasic.facebook.com/','https://www.facebook.com/')
                        with open("comments.txt","a",encoding="utf-8")as f:
                                f.write('\n')
                                f.write(comments)
                                f.write('\n')
                                f.write(i.text)
                                f.close()
                        print(color3 + i.text,'Comments','saved')

            if 'टिप्पणियाँ' in i.text:
                print(i.text)
                if (i['href']) not in comment:
                    numeric_filter = (i.text[0:2])
                    numeric_filter = int(numeric_filter)
                    if numeric_filter > 10:
                        comments = (i['href'])
                        comment += (i['href'])
                        comments = comments.replace('https://mbasic.facebook.com/','https://www.facebook.com/')
                        with open("comments.txt","a",encoding="utf-8")as f:
                                f.write('\n')
                                f.write(comments)
                                f.write('\n')
                                f.write(i.text)
                                f.close()
                        print(color3 + i.text,'saved')
                
                
            if 'https://chat.whatsapp.com/' in i.text:
                if (i.text) not in link:
                    count1 = count1+1
                    link += (i.text)+'\n'
                    print(color + 'found',i.text,count1)
                    with open("links.txt","a", encoding="utf-8")as f:
                        f.write('\n')
                        f.write(link)
                    
            if i.text == 'See more posts':
                url = 'https://mbasic.facebook.com' +i['href']
            if i.text == 'अधिक पोस्ट देखें':
                url = 'https://mbasic.facebook.com' +i['href']

        index = index+1
        if index == count:
            print(index)
            count = int(input(color1+"Do you wan't to add more page? add num:"+color2))
    
while True:
  try:
    login()
    search_url()
  except Exception as e:
      e = str(e)
      print(color2 + e)
      
    




