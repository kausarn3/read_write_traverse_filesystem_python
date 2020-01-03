import os
name="editnote.txt"
s=0
for root, dirs, files in os.walk("F:"):
 s += 1
 if name in files:
     #a=os.path.join(root,"editnote.txt")
     #print(a)

     fh = open(os.path.join(root,name),"w")
     fh.write("D")
     fh.close()
print(s)

