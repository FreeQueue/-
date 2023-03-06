import re
line="this hdr-biz 123 model server 456"
pattern=r"this"
matchObj = re.match( pattern, line)
print(matchObj)

if(matchObj):
    print("s")