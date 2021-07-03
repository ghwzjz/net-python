# import 导入模块
import paramiko
import time
# 定义三个字符串类型的变量
ip = '192.168.242.11'
username = 'python'
password = '123'
# 开启SSH会话赋值给变量
ssh_client = paramiko.SSHClient()
# 开启可接收陌生的ssh服务会话
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip, username=username, password=password, look_for_keys=False)
#  开启交互式会话
command = ssh_client.invoke_shell()
print ('已经成功登陆路由器' + ip)
# 向路由器发出命令
command.send('configure terminal\n')
command.send('interface loop 0\n')
command.send('ip add 1.1.1.1 255.255.255.255\n')
command.send('end\n')
command.send('wr mem\n')
# 延时5秒
time.sleep(5)
# 设置截屏长度并打印出来
output = command.recv(65535).decode('ascii')
print (output)
# 退出ssh会话
ssh_client.close
