查看哪个进程在占用IO
使用两个命令即可：pidstat和iotop
1. 使用pidstat查看
```shell
pidstat -d 1
表示只看io情况，每个1s查看一次
# pidstat -d 1
Linux 4.9.38-16.35.amzn1.x86_64  	2019年04月18日 	_x86_64_	(4 CPU)

17时16分01秒       PID   kB_rd/s   kB_wr/s kB_ccwr/s  Command
17时16分02秒      1601      0.00     28.00      0.00  jbd2/xvda1-8
17时16分02秒      2335      0.00      8.00      0.00  auditd
17时16分02秒      2356      0.00      4.00      0.00  rsyslogd
17时16分02秒      7002      0.00      8.00      0.00  supervise
17时16分02秒     19615      0.00    140.00      0.00  java

17时16分02秒       PID   kB_rd/s   kB_wr/s kB_ccwr/s  Command
17时16分03秒      7002      0.00      8.00      0.00  supervise
17时16分03秒     15403      0.00      4.00      0.00  java
17时16分03秒     19615      0.00    152.00      0.00  java
```
如果不想盯着的话，可以使用nohup 来使用
```shell
nohup pidstat -d 1 >> /tmp/pidstat_`date "+%Y%m%d%H%M"`.log 2>&1 &
```
3. 使用iotop查看
```shell
iotop -botq
-b, --batch #运行在非交互式的模式
-o, --only #显示进程或者线程实际上正在做的I/O，而不是全部的，可以随时切换按o
-t, --time #在每一行前添加一个当前的时间

不想盯着的话也可以写入到文件中
nohup iotop -botq >> /tmp/`date "+%Y%m%d%H%M"`_iotop.log 2>&1 &
```