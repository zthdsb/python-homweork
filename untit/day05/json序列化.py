import json

def sayhi(name):
    print("helll",name)

info={
    "name":"alex",
    "age":23
}

f=open("text.text","w")
f.write( json.dumps(info) )
f.close()