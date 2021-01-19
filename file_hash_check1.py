import hashlib, os

output = os.popen('dir').read()
print(output)
a = input("input file name :")
f = open(a, 'rb')
data = f.read()
f.close()

print("MD5: " + hashlib.md5(data).hexdigest())
print("SHA-1: " + hashlib.sha1(data).hexdigest())
print("SHA-256" + hashlib.sha256(data).hexdigest())


'''def sha1_largefile(a, blocksize=8192):
    sha1 = hashlib.sha1()
    try:
        f = open(a, "rb")
    except IOError as e:
        print("file open error", e)
        return
    while True:
        buf = f.read(blocksize)
        if not buf:
            break
        sha1.update(buf)
    return sha1.hexdigest()
'''
