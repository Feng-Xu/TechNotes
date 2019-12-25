### GoAccess实时监控access日志

1. 安装

   `yum install goaccess`

2. 使用说明

   ```shell
   goaccess -f logs/openresty_test.log -o html/openresty_test.html --real-time-html --time-format='%T' --date-format='%d/%b/%Y' --log-format='%d:%t %^|%^|%h|%^|%T|%^|%^|%s|%^|-|%b|-|-|%^|%r|%u|%R|%v|second|^_^|%^|%^|%^|%^|^_^|%^|%^|%^|%^|%^|%^'
   WebSocket server ready to accept new client connections
   ```

   *如果需要后台运行，则使用nohup...... &的形式*

   -f：分析的日志文件，可以跟多个

   -o：分析结果，放在这个文件中

   --read-time-html：实时更新分析数据

   --time-format：nginx的时间格式都是%T

   --date-format：nginx的日期格式都是‘%d/%b/%Y’

   --log-format：具体的日志格式可以根据nginx的日志格式来定。

   - log-format也可以根据[nginx2goaccess](https://github.com/Feng-Xu/nginx2goaccess)来转换，但是注意：**转换不是很完美，还需检查**。
   - log-format 注意：在goaccess格式中，当有`%r`参数在的时候，不能有`%m`, `%U`, `%q` 和 `%H`。因为`%r`取到的是full request，会与`%m`, `%U`, `%q` 和 `%H`冲突。

3. 实时更新说明

   > 默认goaccess在开启实时real-time-html后会监听端口7890的websocket，如果服务器不允许请求7890端口，你就看不到那个页面是实时更新的——你会发现访问的页面最后更新时间始终不	变。真正更新的实时内容是从websocket过来的 

4. 在nginx中配置转发就可以使用了

   ```shell
          location /openresty_test.html {
              root /opt/xufeng/openresty/nginx/html;
          }
   ```

5. 多台nginx server日志收集，具体做法：

   1. 用syslog把日志汇聚在一台服务上，再用goaccess
   2. 用NFS把多台主机的日志目录映射在一起，再用goaccess
