class Role(object):
    n=123   #类变量 作用：节省内存开销
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        # 构造函数
        # 在实例化时做一些类的初始化工作
        self.name =name  #实例变量（静态属性），作用域是实例本身
        self.role=role
        self.weapon =weapon
        self.life_value=life_value
        self.money=money
        self.__life_value=life_value  #私有属性（前面加双下划线） 外部无法访问
    def __del__(self):
        #析构函数  在每次对象运行完后运行
        print("%s 彻底死了！"%self.name)

    def shot(self):   #类的方法（功能）（动态属性）
        print("shooting...")
    def got_shot(self):
        self.__life_value-=50
        print("a..I'm got shot")
    def buy_weapon(self):
        print("%s just bought %s"%(self.name,self.weapon))
    def show(self):

        print("name:%s life_value=%s"%(self.name,self.__life_value))

r1 = Role('Alex','police','Ak47')  #生成一个角色
r1.got_shot()
r1.show()

# r1.name="zhangteihai"   #修改
# r1.bull_prove=True   #增加
# del r1.weapon  #删除
# r1.n=789
# print(r1.n)
#
# print(r1.bull_prove)
# print(r1.n,r1.name)
#r2=Role('Teihai','terrist','B22')
# r1.buy_weapon()
# print(Role.n)