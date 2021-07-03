#import 导入模块
import paramiko
import time
import getpass
# 定义两个个字符串类型的变量
username = input("Username: ")
password = getpass.getpass("Password: ")

#for循环
for i in range(11,16):
    ip = '192.168.242.' + str(i)
     # 开启SSH会话赋值给变量
    ssh_client = paramiko.SSHClient()
    # 开启可接收陌生的ssh服务会话
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username,password=password,look_for_keys=False)   
#  开启交互式会话
    command = ssh_client.invoke_shell()
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('已经成功登陆交换机 LSW-' + str(i-10) + ' ' + ip)
    # 关闭分屏功能
    command.send('terminal length 0\n')
   #向交换机发送指令
    # 进入特权模式
    command.send('en\n')
    # 进入全局模式
    command.send('conf t\n')
   #循环创建vlan
    for i in range(11,16):
        print('正在删除 VLAN ：' + str(i))
        command.send('no '+'vlan ' + str(i) + '\n')
        time.sleep(1)
    command.send('end\n')
    command.send('wr\n')
  # 延时2秒
    time.sleep(2)
# 设置截屏长度并打印出来
    output = command.recv(65535).decode('ASCII')
    print(output)
# 退出ssh会话
ssh_client.close()
