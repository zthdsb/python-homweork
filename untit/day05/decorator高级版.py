import time
user,passwd="alex","123456"
def auth(auth_type):
    print("the auty_type is:",auth_type)
    def out_wrapper(func):
        def wrapper(*args,**kwargs):
            if auth_type == "local":
                username=input("Username:").strip()
                password=input("Password:").strip()
                if username==user and password==passwd:
                    print("\033[32;1m User has passed authentication\033[0m")
                    func(*args,**kwargs)
                else:
                    print("\033[31;1m Invalid username or password!\033[0m")
            elif auth_type=="ladp":
                print("ladp isn't recower")
        return wrapper
    return out_wrapper

def index():
    print("welcome to index page")
@auth(auth_type="local")
def home():
    print("welcome to home page")
@auth(auth_type="ladp")
def bbs():
    print("welcome to bbs page")

index()
home()
bbs()