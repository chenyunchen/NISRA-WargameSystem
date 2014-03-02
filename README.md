#NISRA-WargameSystem

This is my first project in NISRA.

## Something I Use

```
HTML & CSS 
Python2.7.5 
Tornado 3.1 
Peewee        
Bootstrap     
Photoimpact 
```

## Python

Define some port if you don't give it in command line.

```python
define("port", default=8080, help="run on the given port", type=int)  
```

### DataBase

You can put data what you want in here.
And direct type for the data like: Charactor,Integer

```python
class register(Model):
    tmn = CharField()
    ...
    class Meta:
        database = db  
register.create_table()
```

Define some handler when user come to your website here.
I put my html in templates.Others are in static folder.
cookie_secret is a random string,you can put what you want here.
This will help you to crypte user's cookie.

```python
class Application(tornado.web.Application):   
    def __init__(self):
        handlers = [   
            (r"/", MainHandler),
            ...
        ]   
        settings = dict(   
            template_path=os.path.join(os.path.dirname(__file__), "templates"),   
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret="Kd4xtzDQQCy050xxbhFYEK5Q0jky501IurAcxNpUMfo=",               
        )   
        tornado.web.Application.__init__(self, handlers, **settings)
```

Then Give some action to your handler.
Here I give MainHandler to find cookie to know the user login status.
And welcome to the user after login.

```python
class MainHandler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
        else:
            cod = "You are not logged in now."   
        self.render(   
            "index.html",   
            page_title = "NISRA-WARGAME",
            condition = cod,
            logstate = log,               
        )
```

## HTML

All page are base on base.html in templates.
You can change base.html to add some element for all pages.
"extends" will help you to extend page

```
{% extends base.html %}
```
