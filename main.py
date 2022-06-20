import requests
import html5lib
from bs4 import BeautifulSoup
import pymongo
srv=
client=pymongo.MongoClient('srv')
db=client['ezineart']
cc=db['categories']
def subcat(li):
    jk=[]
    it=1
    for x in li:
        as=x.find('a')
        mj={
            '_id':it,
            'name':as.text,
            'link':f"https://ezinearticles.com{as['href']}"
        }
        jk.append(mj)
        it+=1
    return jk
l= 'https://ezinearticles.com/sitemap.html'
r=requests.get(l)
soup=BeautifulSoup(r.content,'html5lib')
ls=soup.find_all('div',attrs={'class':'accordion'})
i=1
for x in ls:
    m=x.find('a',attrs={'class':''})
    li=x.find_all('li')
    ghg=subcat(li)
    dict={
        '_id':i,
        'name':m.text,
        'link':f"https://ezinearticles.com{m.['href']}",
        'subcategory':ghg
    }
    cc.insert_one(dict)
    print(inserted_id)
    i+=1
