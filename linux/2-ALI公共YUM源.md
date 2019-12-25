### ALI公共YUM源
ali的公共yum源如下设置：
```shell
# cat CentOS-Base.repo
[base]
name=CentOS-$releasever
enabled=1
failovermethod=priority
baseurl=http://mirrors.aliyun.com/centos/$releasever/os/$basearch/
gpgcheck=1
gpgkey=http://mirrors.aliyun.com/centos/RPM-GPG-KEY-CentOS-7

[updates]
name=CentOS-$releasever
enabled=1
failovermethod=priority
baseurl=http://mirrors.aliyun.com/centos/$releasever/updates/$basearch/
gpgcheck=1
gpgkey=http://mirrors.aliyun.com/centos/RPM-GPG-KEY-CentOS-7

[extras]
name=CentOS-$releasever
enabled=1
failovermethod=priority
baseurl=http://mirrors.aliyun.com/centos/$releasever/extras/$basearch/
gpgcheck=1
gpgkey=http://mirrors.aliyun.com/centos/RPM-GPG-KEY-CentOS-7

# cat CentOS-Epel.repo
[epel]
name=Extra Packages for Enterprise Linux 7 - $basearch
enabled=1
failovermethod=priority
baseurl=http://mirrors.aliyun.com/epel/7/$basearch
gpgcheck=0
gpgkey=http://mirrors.aliyun.com/epel/RPM-GPG-KEY-EPEL-7
```
以上是CentOS 7对应的yum源，如果是CentOS 6，那就修改成6即可。