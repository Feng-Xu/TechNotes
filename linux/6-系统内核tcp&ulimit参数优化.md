### 系统内核tcp&ulimit参数优化.md
最近初始化ali机器，发现内核参数不是以下的值。以下是这些参数正确的值和原因  
1. max user processes = 65535
max user processes用来限制每个用户的最大processes数量，每个linux用户可以派生出来的process就会被限制再这个数值之内   
如果这个值过低，那么用户就不能创建新的process了。
将该参数设置成65535，保证用户可以创建process，所以对于长连接较多的服务，这个参数还是很重要的。  
具体设置方法：
```shell
vim /etc/security/limits.d/90-nproc.conf
# * 表示对所有用户生效
*          soft    nproc     65535
```
2. open files = 65535
open files表示单个进程能够打开的最大文件句柄数量(socket连接也算在里面)。系统默认值1024。因为任何设备在linux下都是文件，通信的接口也有专门的接口文件负责，所以linux下进程tcp链接的最大并发量也受限于该值。  
如果系统并发特别大，很有可能会超过1024。这时候就必须要调整系统参数，以适应应用变化。
3. net.ipv4.tcp_keepalive_time = 10
因为 TCP 的上层调用是 Socket，客户端和服务端都会启动 Socket。**如果客户端关闭了 Socket，而服务端不知道，一直会为客户端保持着连接，这样是很浪费资源的**。为了解决这个问题，TCP协议规定，当超过一段时间之后，TCP自动发送一个数据为空的报文给对方，如果对方回应了这个报文，说明对方还在线，连接可以继续保持，如果对方没有报文返回，并且重试了多次之后则认为连接丢失，应该关闭连接。   
Linux 内核包含了对 keepalive 的支持，使用下面三个参数（默认单位为秒）
```shell
# 表示TCP链接在多少秒之后没有数据报文传输时启动探测报文（发送空的报文）
cat /proc/sys/net/ipv4/tcp_keepalive_time 
7200

# 表示前一个探测报文和后一个探测报文之间的时间间隔
cat /proc/sys/net/ipv4/tcp_keepalive_intvl
75

# 表示探测的次数
cat /proc/sys/net/ipv4/tcp_keepalive_probes
9
```
这些参数是在_etc_sysctl.conf文件中定义的，默认文件中没有定义这三个参数，但系统提供的有默认值。可以根据需要进行修改，修改后，执行sysctl -p命令让其生效。  
显然tcp_keepalive_time默认为7200s（2h），对于服务在socket编程时没有指定tcp_keepalive_time的，高并发环境client断开连接，而服务端tcp连接不释放，资源机会被耗尽，服务就会被怼死。
