import hashlib

m=hashlib.md5()
m.update(b"text")
m.update(b"abc")
h=hashlib.md5()
h.update(b"textabc")
print(m.hexdigest())
print(h.hexdigest())