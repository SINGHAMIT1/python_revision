f=open("C:\\Users\\ASUS\\Desktop\\Data\\funny.txt","r")
f_out=open("C:\\Users\\ASUS\\Desktop\\Data\\funnyw.txt","w")
for line in f:
    token=line.split()
    f_out.write( "word count:"+str(len(token))+line)

f.close()
f_out.close()