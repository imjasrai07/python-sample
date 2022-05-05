import os

import pymongo

from wordpress_xmlrpc import Client, WordPressPost

from wordpress_xmlrpc.methods.posts import GetPosts, NewPost

from wordpress_xmlrpc.methods.users import GetUserInfo

dblink=os.environ['DBLK']

username=os.environ['UNLK']

password= os.environ['PWLK']

weblink=os.environ['ULK']

wp = Client(weblink, username, password)

myclient=pymongo.MongoClient(dblink)

mydb = myclient["articlebase"]

mycol = mydb["content"]

def status(id):

   mycol.update_one({'_id':id},{'$set' : {'status':0}})

def postr(x,n):

  id=x['_id']

  tit=x['title']

  rt=x['slug']

  which = 'publish'

  post = WordPressPost()

  post.post_status = which

  post.title= tit

  post.content=x['content']

  category=x['category']

  post.terms_names ==   { 

  'category' [category]}

  post.slug=rt

  

  wp.call(NewPost(post))

  status(id)

  print(n)

  print('-'*40)

  

y = mycol.find()

i=1

for x in y:

  #postr(x,i)

  id=x['_id']

  status(id)

  print(i)

  i+=1
