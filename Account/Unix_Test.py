import socket,os,subprocess

print (socket.gethostname())
os.mkdir('test')
os.mkdir('test2')
os.system("cd test")
subprocess.call("touch",file1)
subprocess.call("mv ")