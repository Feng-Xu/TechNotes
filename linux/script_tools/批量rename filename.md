### 批量rename filename
将filename-2018-07-01.log 该成 filename.log.2018-07-01
```
for name in `ls /opt/xxxx/service-name/logs/filename-2018-07-*.log`;
    do
        name2=`echo $name|sed -r 's/filename-(.*).log/filename.log.\1/'`
        echo  $name $name2
        rename $name $name2 $name
    done
```