import tornado.web   
import tornado.httpserver   
import tornado.ioloop   
import tornado.options   
import os.path
from datetime import datetime   
from tornado.options import define, options
from peewee import *
db = SqliteDatabase("register.db") 
define("port", default=8080, help="run on the given port", type=int)  

class register(Model):
    tmn = CharField()
    tmm1 = CharField()
    tmm2 = CharField()
    tmm3 = CharField()
    un = CharField()
    pas = CharField()
    conpas = CharField()
    pts = DecimalField()
    pasd = DecimalField()
    ti = DateTimeField()
    r1 = CharField()
    r2 = CharField()
    r3 = CharField()
    r4 = CharField()
    r5 = CharField()
    w1 = CharField()
    w2 = CharField()
    w3 = CharField()
    w4 = CharField()
    w5 = CharField()
    b1 = CharField()
    b2 = CharField()
    b3 = CharField()
    b4 = CharField()
    b5 = CharField()
    f1 = CharField()
    f2 = CharField()
    f3 = CharField()
    f4 = CharField()
    f5 = CharField()
    p1 = CharField()
    p2 = CharField()
    p3 = CharField()
    p4 = CharField()
    p5 = CharField()
    class Meta:
        database = db  
register.create_table()
class Application(tornado.web.Application):   
    def __init__(self):
        handlers = [   
            (r"/", MainHandler),
            (r"/register.html", Register),
            (r"/registerhandler.html", RegisterHandler),
            (r"/challengers.html", ChallengersHandler),
            (r"/login.html",Login),
            (r"/loginhandler.html",LoginHandler),
            (r"/logout.html",LogoutHandler),
            (r"/R1.html", R1Handler),
            (r"/R11.html", R11Handler),
            (r"/R2.html", R2Handler),
            (r"/R22.html", R22Handler),
            (r"/R3.html", R3Handler),
            (r"/R33.html", R33Handler),
            (r"/R4.html", R4Handler),
            (r"/R44.html", R44Handler),
            (r"/R5.html", R5Handler),
            (r"/R55.html", R55Handler),
            (r"/W1.html", W1Handler),
            (r"/W11.html", W11Handler),
            (r"/W2.html", W2Handler),
            (r"/W22.html", W22Handler),
            (r"/W3.html", W3Handler),
            (r"/W33.html", W33Handler),
            (r"/W4.html", W4Handler),
            (r"/W44.html", W44Handler),
            (r"/W5.html", W5Handler),
            (r"/W55.html", W55Handler),
            (r"/B1.html", B1Handler),
            (r"/B11.html", B11Handler),
            (r"/B2.html", B2Handler),
            (r"/B22.html", B22Handler),
            (r"/B3.html", B3Handler),
            (r"/B33.html", B33Handler),
            (r"/B4.html", B4Handler),
            (r"/B44.html", B44Handler),
            (r"/B5.html", B5Handler),
            (r"/B55.html", B55Handler),
            (r"/F1.html", F1Handler),
            (r"/F11.html", F11Handler),
            (r"/F2.html", F2Handler),
            (r"/F22.html", F22Handler),
            (r"/F3.html", F3Handler),
            (r"/F33.html", F33Handler),
            (r"/F4.html", F4Handler),
            (r"/F44.html", F44Handler),
            (r"/F5.html", F5Handler),
            (r"/F55.html", F55Handler),
            (r"/P1.html", P1Handler),
            (r"/P11.html", P11Handler),
            (r"/P2.html", P2Handler),
            (r"/P22.html", P22Handler),
            (r"/P3.html", P3Handler),
            (r"/P33.html", P33Handler),
            (r"/P4.html", P4Handler),
            (r"/P44.html", P44Handler),
            (r"/P5.html", P5Handler),
            (r"/P55.html", P55Handler),
        ]   
        settings = dict(   
            template_path=os.path.join(os.path.dirname(__file__), "templates"),   
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret="Kd4xtzDQQCy050xxbhFYEK5Q0jky501IurAcxNpUMfo=",               
        )   
        tornado.web.Application.__init__(self, handlers, **settings)   
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
class Register(tornado.web.RequestHandler):   
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
        msg = ""
        self.render(   
            "register.html",
            message = msg,
            condition = cod,
            logstate = log,            
        )
class RegisterHandler(tornado.web.RequestHandler):   
    def post(self):
        log = ""
        cod = ""
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
        else:
            cod = "You are not logged in now."
        teamname = self.get_argument("teamname")
        teammember1 = self.get_argument("teammember1")
        teammember2 = self.get_argument("teammember2")
        teammember3 = self.get_argument("teammember3")
        username = self.get_argument("username")
        password = self.get_argument("password")
        confirmpassword = self.get_argument("confirmpassword")
        points = 0
        passed = 0
        time = datetime.now()
        sr1 = ""
        sr2 = ""
        sr3 = ""
        sr4 = ""
        sr5 = ""
        sw1 = ""
        sw2 = ""
        sw3 = ""
        sw4 = ""
        sw5 = ""
        sb1 = ""
        sb2 = ""
        sb3 = ""
        sb4 = ""
        sb5 = ""
        sf1 = ""
        sf2 = ""
        sf3 = ""
        sf4 = ""
        sf5 = ""
        sp1 = ""
        sp2 = ""
        sp3 = ""
        sp4 = ""
        sp5 = ""
        if teammember2 == "":
            teammember2 = ""
        if teammember3 == "":
            teammember3 = ""
        if teamname == "":
            msg = "*Please enter the teamname!!"
        elif teammember1 == "":
            msg = "*Please enter the teammember1!!"
        elif username == "":
            msg = "*Please enter the username!!"
        elif password == "":
            msg = "*Please enter the password!!"
        elif confirmpassword == "":
            msg = "*Please enter the confirm password!!"
        elif password != confirmpassword:
            msg = "*Password is different with confirm password!!"
        elif register.select().where(register.tmn == teamname).exists():
            msg = "*Teamname has already been taken!!"
        elif register.select().where(register.un == username).exists():
            msg = "*Username has already been taken!!"
        else:
            msg = "*Success!!"
            person = register.create(tmn=teamname,tmm1=teammember1,tmm2=teammember2,tmm3=teammember3,un=username,pas=password,conpas=confirmpassword,pts=points,pasd=passed,ti=time,
                                     r1=sr1,r2=sr2,r3=sr3,r4=sr4,r5=sr5,w1=sw1,w2=sw2,w3=sw3,w4=sw4,w5=sw5,
                                     b1=sb1,b2=sb2,b3=sb3,b4=sb4,b5=sb5,f1=sf1,f2=sf2,f3=sf3,f4=sf4,f5=sf5,
                                     p1=sp1,p2=sp2,p3=sp3,p4=sp4,p5=sp5)
            person.save()
        self.render(   
            "register.html",
            message = msg,
            condition = cod,
            logstate = log,
        )
class ChallengersHandler(tornado.web.RequestHandler):   
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
        num=0;
        data = ["","","","","","","",
                "","","","","","","",
                "","","","","","","",
                "","","","","","","",
                "","","","","","","",
                "","","","","","","",
                "","","","","","","",
                "","","","","","","",
                "","","","","","","",
                "","","","","","","",
                "","","","","","","",
                "","","","","","","",
                "","","","","","","",
                "","","","","","","",
                "","","","","","","",
                "","","","","","","",
                "","","","","","","",
                "","","","","","","",
                "","","","","","","",
                "","","","","","",""];
        bigguy = ""
        people = [guy for guy in register.select().order_by(register.pts.desc())]
        for i in range(1,len(people)):
            for j in range(0,len(people)-1*i):
                if people[j].ti > people[j+1].ti and people[j].pts == people[j+1].pts:
                    bigguy = people[j]
                    people[j] = people[j+1]
                    people[j+1] = bigguy
        for person in people:
            data[num]=person.tmn
            num=num+1
            data[num]=person.tmm1
            num=num+1
            data[num]=person.tmm2
            num=num+1
            data[num]=person.tmm3
            num=num+1
            data[num]=person.pts
            num=num+1
            data[num]=person.pasd
            num=num+1
            data[num]=person.ti
            num=num+1
        self.render(   
            "challengers.html",
            condition = cod,
            logstate = log,
            teamname_1 = data[0],teammember1_1 = data[1],teammember2_1 = data[2],teammember3_1 = data[3],points_1 = data[4],passed_1 = data[5],time_1 = data[6],
            teamname_2 = data[7],teammember1_2 = data[8],teammember2_2 = data[9],teammember3_2 = data[10],points_2 = data[11],passed_2 = data[12],time_2 = data[13],
            teamname_3 = data[14],teammember1_3 = data[15],teammember2_3 = data[16],teammember3_3 = data[17],points_3 = data[18],passed_3 = data[19],time_3 = data[20],
            teamname_4 = data[21],teammember1_4 = data[22],teammember2_4 = data[23],teammember3_4 = data[24],points_4 = data[25],passed_4 = data[26],time_4 = data[27],
            teamname_5 = data[28],teammember1_5 = data[29],teammember2_5 = data[30],teammember3_5 = data[31],points_5 = data[32],passed_5 = data[33],time_5 = data[34],
            teamname_6 = data[35],teammember1_6 = data[36],teammember2_6 = data[37],teammember3_6 = data[38],points_6 = data[39],passed_6 = data[40],time_6 = data[41],
            teamname_7 = data[42],teammember1_7 = data[43],teammember2_7 = data[44],teammember3_7 = data[45],points_7 = data[46],passed_7 = data[47],time_7 = data[48],
            teamname_8 = data[49],teammember1_8 = data[50],teammember2_8 = data[51],teammember3_8 = data[52],points_8 = data[53],passed_8 = data[54],time_8 = data[55],
            teamname_9 = data[56],teammember1_9 = data[57],teammember2_9 = data[58],teammember3_9 = data[59],points_9 = data[60],passed_9 = data[61],time_9 = data[62],
            teamname_10 = data[63],teammember1_10 = data[64],teammember2_10 = data[65],teammember3_10 = data[66],points_10 = data[67],passed_10 = data[68],time_10 = data[69],
            teamname_11 = data[70],teammember1_11 = data[71],teammember2_11 = data[72],teammember3_11 = data[73],points_11 = data[74],passed_11 = data[75],time_11 = data[76],
            teamname_12 = data[77],teammember1_12 = data[78],teammember2_12 = data[79],teammember3_12 = data[80],points_12 = data[81],passed_12 = data[82],time_12 = data[83],
            teamname_13 = data[84],teammember1_13 = data[85],teammember2_13 = data[86],teammember3_13 = data[87],points_13 = data[88],passed_13 = data[89],time_13 = data[90],
            teamname_14 = data[91],teammember1_14 = data[92],teammember2_14 = data[93],teammember3_14 = data[94],points_14 = data[95],passed_14 = data[96],time_14 = data[97],
            teamname_15 = data[98],teammember1_15 = data[99],teammember2_15 = data[100],teammember3_15 = data[101],points_15 = data[102],passed_15 = data[103],time_15 = data[104],
            teamname_16 = data[105],teammember1_16 = data[106],teammember2_16 = data[107],teammember3_16 = data[108],points_16 = data[109],passed_16 = data[110],time_16 = data[111],
            teamname_17 = data[112],teammember1_17 = data[113],teammember2_17 = data[114],teammember3_17 = data[115],points_17 = data[116],passed_17 = data[117],time_17 = data[118],
            teamname_18 = data[119],teammember1_18 = data[120],teammember2_18 = data[121],teammember3_18 = data[122],points_18 = data[123],passed_18 = data[124],time_18 = data[125],
            teamname_19 = data[126],teammember1_19 = data[127],teammember2_19 = data[128],teammember3_19 = data[129],points_19 = data[130],passed_19 = data[131],time_19 = data[132],
            teamname_20 = data[133],teammember1_20 = data[134],teammember2_20 = data[135],teammember3_20 = data[136],points_20 = data[137],passed_20 = data[138],time_20 = data[139],
        )
class Login(tornado.web.RequestHandler):
    def get(self):
        log = ""
        cod = ""
        btnstate = ""
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = "disabled"
        else:
            cod = "You are not logged in now."
        self.render(
            "login.html",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class LoginHandler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        btnstate = ""
        user = self.get_argument("username")
        passw = self.get_argument("password")
        person = register.select().where(register.un == user).exists()
        if person:
            person=register.select().where(register.un == user).get()
            if person.pas == passw:
                cod = "Welcome!! Team: "+person.tmn+" Points:"+str(person.pts)
                log = "Logout"
                btnstate = "disabled"
                self.set_secure_cookie("teamname",person.tmn)
            else:
                cod = "Oops!! Your account data is wrong."
        else:
            cod = "Oops!! Your account data is wrong."
        self.render(
            "login.html",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        log = ""
        cod = "You are not logged in now."
        btnstate = ""
        self.clear_cookie("teamname")
        self.render(
            "login.html",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class R1Handler(tornado.web.RequestHandler):    
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.r1
        else:
            cod = "You are not logged in now."        
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Roulette 100 points",
            wargame_type = "Roulette",
            score = "100",            
            message = msg,
            process = "R11.html",
            question = "Hack the ______!",
            qlink = "http://www.google.com.tw",
            qlinkname = "Google",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class R11Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.r1
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "planet" and decide == "yes" and person.r1 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 100
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.r1 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Roulette 100 points",
            wargame_type = "Roulette",
            score = "100",
            process = "R11.html",            
            message = msg,
            question = "Hack the ______!",
            qlink = "http://www.google.com.tw",
            qlinkname = "Google",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class R2Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.r2
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Roulette 200 points",
            wargame_type = "Roulette",
            score = "200",
            message = msg,
            process = "R22.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class R22Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.r2
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.r2 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 200
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.r2 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Roulette 200 points",
            wargame_type = "Roulette",
            score = "200",
            process = "R22.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class R3Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.r3
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Roulette 300 points",
            wargame_type = "Roulette",
            score = "300",
            message = msg,
            process = "R33.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class R33Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.r3
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.r3 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 300
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.r3 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Roulette 300 points",
            wargame_type = "Roulette",
            score = "300",
            process = "R33.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class R4Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.r4
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Roulette 400 points",
            wargame_type = "Roulette",
            score = "400",
            message = msg,
            process = "R44.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class R44Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.r4
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.r4 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 400
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.r4 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Roulette 400 points",
            wargame_type = "Roulette",
            score = "400",
            process = "R44.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class R5Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.r5
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Roulette 500 points",
            wargame_type = "Roulette",
            score = "500",
            message = msg,
            process = "R55.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class R55Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.r5
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.r5 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 500
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.r5 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Roulette 500 points",
            wargame_type = "Roulette",
            score = "500",
            process = "R55.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class W1Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.w1
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Web Security 100 points",
            wargame_type = "Web Security",
            score = "100",
            message = msg,
            process = "W11.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class W11Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.w1
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.w1 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 100
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.w1 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Web Security 100 points",
            wargame_type = "Web Security",
            score = "100",
            process = "W11.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class W2Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.w2
        else:
            cod = "You are not logged in now."  
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Web Security 200 points",
            wargame_type = "Web Security",
            score = "200",
            message = msg,
            process = "W22.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class W22Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.w2
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra"and decide == "yes" and person.w2 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 200
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.w2 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Web Security 200 points",
            wargame_type = "Web Security",
            score = "200",
            process = "W22.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class W3Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.w3
        else:
            cod = "You are not logged in now." 
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Web Security 300 points",
            wargame_type = "Web Security",
            score = "300",
            message = msg,
            process = "W33.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class W33Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.w3
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.w3 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 300
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.w3 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Web Security 300 points",
            wargame_type = "Web Security",
            score = "300",
            process = "W33.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class W4Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.w4
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Web Security 400 points",
            wargame_type = "Web Security",
            score = "400",
            message = msg,
            process = "W44.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class W44Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.w4
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.w4 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 400
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.w4 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Web Security 400 points",
            wargame_type = "Web Security",
            score = "400",
            process = "W44.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class W5Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.w5
        else:
            cod = "You are not logged in now." 
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Web Security 500 points",
            wargame_type = "Web Security",
            score = "500",
            message = msg,
            process = "W55.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class W55Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.w5
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.w5 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 500
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.w5 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Web Security 500 points",
            wargame_type = "Web Security",
            score = "500",
            process = "W55.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class B1Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.b1
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Binary Processing 100 points",
            wargame_type = "Binary Processing",
            score = "100",
            message = msg,
            process = "B11.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class B11Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.b1
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.b1 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 100
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.b1 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Binary Processing 100 points",
            wargame_type = "Binary Processing",
            score = "100",
            process = "B11.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class B2Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.b2
        else:
            cod = "You are not logged in now." 
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Binary Processing 200 points",
            wargame_type = "Binary Processing",
            score = "200",
            message = msg,
            process = "B22.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class B22Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.b2
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.b2 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 200
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.b2 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Binary Processing 200 points",
            wargame_type = "Binary Processing",
            score = "200",
            process = "B22.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class B3Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.b3
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Binary Processing 300 points",
            wargame_type = "Binary Processing",
            score = "300",
            message = msg,
            process = "B33.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class B33Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.b3
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.b3 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 300
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.b3 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Binary Processing 300 points",
            wargame_type = "Binary Processing",
            score = "300",
            process = "B33.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class B4Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.b4
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Binary Processing 400 points",
            wargame_type = "Binary Processing",
            score = "400",
            message = msg,
            process = "B44.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class B44Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.b4
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.b4 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 400
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.b4 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Binary Processing 400 points",
            wargame_type = "Binary Processing",
            score = "400",
            process = "B44.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class B5Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.b5
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Binary Processing 500 points",
            wargame_type = "Binary Processing",
            score = "500",
            message = msg,
            process = "B55.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class B55Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.b5
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.b5 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 500
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.b5 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Binary Processing 500 points",
            wargame_type = "Binary Processing",
            score = "500",
            process = "B55.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class F1Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.f1
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Forensics 100 points",
            wargame_type = "Forensics",
            score = "100",
            message = msg,
            process = "F11.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class F11Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.f1
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.f1 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 100
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.f1 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Forensics 100 points",
            wargame_type = "Forensics",
            score = "100",
            process = "F11.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class F2Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.f2
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Forensics 200 points",
            wargame_type = "Forensics",
            score = "200",
            message = msg,
            process = "F22.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class F22Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.f2
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.f2 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 200
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.f2 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Forensics 200 points",
            wargame_type = "Forensics",
            score = "200",
            process = "F22.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class F3Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.f3
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Forensics 300 points",
            wargame_type = "Forensics",
            score = "300",
            message = msg,
            process = "F33.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class F33Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.f3
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.f3 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 300
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.f3 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Forensics 300 points",
            wargame_type = "Forensics",
            score = "300",
            process = "F33.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class F4Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.f4
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Forensics 400 points",
            wargame_type = "Forensics",
            score = "400",
            message = msg,
            process = "F44.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class F44Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.f4
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.f4 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 400
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.f4 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Forensics 400 points",
            wargame_type = "Forensics",
            score = "400",
            process = "F44.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class F5Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.f5
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Forensics 500 points",
            wargame_type = "Forensics",
            score = "500",
            message = msg,
            process = "F55.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class F55Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.f5
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.f5 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 500
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.f5 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Forensics 500 points",
            wargame_type = "Forensics",
            score = "500",
            process = "F55.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class P1Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.p1
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Pwn3d 100 points",
            wargame_type = "Pwn3d",
            score = "100",
            message = msg,
            process = "P11.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class P11Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.p1
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.p1 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 100
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.p1 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Pwn3d 100 points",
            wargame_type = "Pwn3d",
            score = "100",
            process = "P11.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class P2Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.p2
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Pwn3d 200 points",
            wargame_type = "Pwn3d",
            score = "200",
            message = msg,
            process = "P22.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class P22Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.p2
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.p2 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 200
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.p2 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Pwn3d 200 points",
            wargame_type = "Pwn3d",
            score = "200",
            process = "P22.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class P3Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.p3
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Pwn3d 300 points",
            wargame_type = "Pwn3d",
            score = "300",
            message = msg,
            process = "P33.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class P33Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.p3
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.p3 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 300
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.p3 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Pwn3d 300 points",
            wargame_type = "Pwn3d",
            score = "300",
            process = "P33.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class P4Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.p4
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Pwn3d 400 points",
            wargame_type = "Pwn3d",
            score = "400",
            message = msg,
            process = "P44.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class P44Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.p4
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.p4 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 400
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.p4 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Pwn3d 400 points",
            wargame_type = "Pwn3d",
            score = "400",
            process = "P44.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class P5Handler(tornado.web.RequestHandler):   
    def get(self):
        log = ""
        cod = ""
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            btnstate = person.p5
        else:
            cod = "You are not logged in now."
        msg = ""
        self.render(   
            "questions.html",   
            page_title = "Pwn3d 500 points",
            wargame_type = "Pwn3d",
            score = "500",
            message = msg,
            process = "P55.html",
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
class P55Handler(tornado.web.RequestHandler):
    def post(self):
        log = ""
        cod = ""
        decide = "no"
        btnstate = "disabled"
        cookie = self.get_secure_cookie("teamname")
        if cookie:
            person = register.select().where(register.tmn == cookie).get()
            cod = "Welcome!! Team:"+cookie+" Points:"+str(person.pts)
            log = "Logout"
            decide = "yes"
            btnstate = person.p5
        else:
            cod = "You are not logged in now."
        answer = self.get_argument("answer")
        person = register.select().where(register.tmn == cookie).get()
        if answer == "nisra" and decide == "yes" and person.p5 == "":
            msg="Correct!! :)"
            person = register.select().where(register.tmn == cookie).get()
            person.pts = person.pts + 500
            person.pasd = person.pasd +1
            person.ti = datetime.now()
            person.p5 = "disabled"
            person.save()
            btnstate = "disabled"
        else:
            msg="Wrong QQ"
        self.render(
            "questions.html",   
            page_title = "Pwn3d 500 points",
            wargame_type = "Pwn3d",
            score = "500",
            process = "P55.html",            
            message = msg,
            question = "",
            qlink = "",
            qlinkname = "",
            hint = "",
            condition = cod,
            logstate = log,
            buttonstate = btnstate,
        )
if __name__ == "__main__":   
    tornado.options.parse_command_line()   
    http_server = tornado.httpserver.HTTPServer(Application())   
    http_server.listen(options.port)   
    tornado.ioloop.IOLoop.instance().start()  