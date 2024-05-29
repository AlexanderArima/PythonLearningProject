
# encode()和decode()方法
import encodings


str = "风扇";
print(str.encode())
bytes1 = str.encode();
print(bytes1.decode())

#bytes类型
name = bytes("111", encoding = "UTF-8")
name2 = b""
name3 = b"Cherry"
print(name3)

#删除空白
hello = "  hello world   "
print(hello)
print(hello.lstrip())
print(hello.rstrip())
print(hello.strip())
