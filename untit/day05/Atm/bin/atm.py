print(__file__)#返回绝对路径
import os,sys
print(os.path.abspath(__file__))#返回相对路径
print(os.path.dirname(os.path.abspath(__file__)))#返回路径名，不要文件名
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)
from conf import setting
from core import main
main.login()