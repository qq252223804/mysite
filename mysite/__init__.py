# import hashlib
#
#
# def save( pwd):
#         pwd1 = hashlib.sha1(pwd.encode("utf8")).hexdigest()
#
#
#         print(pwd1)
# save('123')
import uuid
uid=uuid.uuid1()
suid = ''.join(str(uid).split('-'))
print(suid)