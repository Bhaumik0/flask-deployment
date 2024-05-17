from flask import Flask,request,current_app,g,session
import logging

log=loggig.getLogger("werkzeug")
log.setLever(logging.error)

application=Flask(__name__)

@application.route("/")
def indexMethod():
    html="<!DOCTYPE HTML>"
    html+="<html lang='eng'>"
    html+="<head>"
    html+="<title> The Blog</title>"
    html+="</head>"
    html+="<body>"
    html+="<h1>The Blog</h1>"
    html+="<a href='/register'>Register</a></br>"
    html+="<a href='/login'>Login</a>"
    html+="</body>"
    html+="</html>"
    return html

def register():
    return "User is register"

@application.route("/register")
def login():
    return "This is the loginIn page"

application.add_url_rule("/register","rgstr",register)

#################### For learning #####################

@application.route("/org/<organization>/<city>")
def sam(organization,city):
    print(g) 
    print(session)
    print(request)
    print(current_app)
    client=request.header.get("User-Agent")
    return f"Cool {organization} from {city}" 

@appication.route("/tom")
def tom():
    print(request.method)
    return good
  
@application.route("/john",methods=["POST"])
def john():
    return great

@application.route("/ramesh")
def ramu():
    print(request.args)
    print(request.form)
    print(request.query_string)
    print(request.scheme)
    print(request.is_secure)
    print(request.host)
    print(request.path)
    print(request.full_path)
    print(request.url)
    print(request.base_url)
    print(request.remote_addr)
    return "whatever"