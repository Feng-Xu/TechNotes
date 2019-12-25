### 编译nginx
1. 目录
```shell
drwxr-xr-x 6 1001 1001   4096 Sep 16 15:37 auto
-rw-r--r-- 1 1001 1001 286953 Apr 17  2018 CHANGES
-rw-r--r-- 1 1001 1001 437286 Apr 17  2018 CHANGES.ru
drwxr-xr-x 2 1001 1001   4096 Sep 16 15:37 conf
-rwxr-xr-x 1 1001 1001   2502 Apr 17  2018 configure
drwxr-xr-x 4 1001 1001   4096 Sep 16 15:37 contrib
drwxr-xr-x 2 1001 1001   4096 Sep 16 15:37 html
-rw-r--r-- 1 1001 1001   1397 Apr 17  2018 LICENSE
-rw-r--r-- 1 root root    325 Sep 17 18:28 Makefile
drwxr-xr-x 2 1001 1001   4096 Sep 16 15:37 man
drwxr-xr-x 3 root root   4096 Sep 17 18:28 objs
-rw-r--r-- 1 1001 1001     49 Apr 17  2018 README
drwxr-xr-x 9 1001 1001   4096 Sep 16 15:37 src
```
- auto：辅助configure去执行时去判定nginx支持哪些模块，当前操作系统有哪些特性可以供给nginx使用
- CHANGES：nginx每个版本中提供了哪些特性，修复了哪些bug。changes.ru是俄罗斯版的changes
- conf：实例文件，nginx安装好之后为了方便运维配置，会把conf中实例文件拷贝到安装目录
- configure：该脚本是用来生成中间文件，执行编译前的一些必备工作
- contrib：提供2个perl脚本和nginx vim语法高亮。
- html：提供两个标准html文件。一个是50x错误时会重定向这个文件。另一个是默认的nginx欢迎界面
- man：linux对nginx的帮助文件
- src：nginx源代码
- objs：编译后的文件
2. 编译configure支持的参数
```shell
  --prefix=PATH                      set installation prefix
  --sbin-path=PATH                   set nginx binary pathname
  --modules-path=PATH                set modules path
  --conf-path=PATH                   set nginx.conf pathname
  --error-log-path=PATH              set error log pathname
  --pid-path=PATH                    set nginx.pid pathname
  --lock-path=PATH                   set nginx.lock pathname
  ...
  ...
  --with-select_module               enable select module
  --without-select_module            disable select module
  --with-poll_module                 enable poll module
  --without-poll_module              disable poll module
```
    - modules-path：动态模块
    - with-xxx_module：默认编译的时候xxx模块不会编入nginx，如果编译的时候想加入xxx模块，需要使用这个with-xxx_module参数
    - without-xxx_module：默认编译的时候xxx模块会编入nginx，如果编译的时候不想加入xxx模块，则需要使用这个without-xxx_module参数

3. make 编译nginx，编译完会在objs下生成二进制文件
4. make install 首次安装时使用该命令，升级nginx只执行到make
