### 统计每秒文件中增加log的行数
```shell
DATE=$(date +%s)
count=$(grep -c "" /opt/nginx/log/www.log)
while true
do
        DATE_New=$(date +%s)
        if (( $(date +%s) == DATE+1))
        then

        DATE=$(date +%s)
        count_new=$(grep -c "" /opt/nginx/log/www.log)
        add=$((count_new - count))
        if [ ! -n "$add" ]    
        then
        add=0
        fi
        echo add line number is:$add    
        count=$count_new
        fi
done
```