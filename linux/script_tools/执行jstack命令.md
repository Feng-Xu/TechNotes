### 执行jstack命令脚本
在Jenkins定义了一个通用任务，用来执行jstack。其中targetHost，storeDir，jstackParameter和operation都是Jenkins job中定义的string parameter，然后传给以下脚本。 
```
#!/bin/bash
set +x

if [ $operation == "run" ];then
        for host in ${targetHost}
    do
         echo "*********机器ip地址:$host********************"
         ec2Pid=$(ssh -o "StrictHostKeyChecking no" root@$host "ps -ef|grep ec2-user|grep -v grep|awk '{print \$2}'")
         if [ $ec2Pid ];then
                echo "*********服务的pid:$ec2Pid********************"
         else
                echo -e "\033[31m服务没有运行\033[0m"
                exit 1
         fi
         DATE=$(date +%H-%M)
         echo "jstack $jstackParameter -l $ec2Pid > $storeDir/jstack-$DATE"
         ssh -o "StrictHostKeyChecking no" root@$host "jstack $jstackParameter  -l $ec2Pid > $storeDir/jstack-$DATE"
         if [ $? -ne 0 ];then
                echo -e "\033[31mjstack执行失败，请看以上log信息\033[0m"
                exit 1
         fi
         ssh -o "StrictHostKeyChecking no" root@$host "cd $storeDir;ls|grep jstack|xargs chmod 777"
         ssh -o "StrictHostKeyChecking no" root@$host "ls -al $storeDir|grep jstack"
    done
fi
```