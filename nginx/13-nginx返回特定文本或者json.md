### nginx返回特定文本或者json
#### 固定文本
```nginx
location ~ ^/get_text {
		default_type text/html;
		return 200 'This is text!';
}
```
#### 固定json
```nginx
location ~ ^/get_json {
    default_type application/json;
    return 200 '{"status":"success","result":"nginx json"}';
}
```
#### 根据不同请求返回不同字符串
```nginx
location ~ ^/get_text/article/(.*)_(\d+).html$ {
    default_type text/html;
    set $s $1;
    set $d $2;
    return 200 str:$s$d;
}
# curl https://www.xxxxx.com.cn/get_text/article/asda_123.html
str:asda123
```
**注意：default_type必须要添加，否则浏览器会当成不识别的文件进行下载**  
  
另外补充一下中文显示的问题，因为Linux下采用的是utf-8的字符编码，默认情况下我们的浏览器在服务器没有指定编码或者静态页面没有声明编码的情况下会以GBK的编码去渲染页面，这样默认情况下返回中文的话浏览器用gbk来解析utf-8编码，显然会出现乱码，这时要在nginx location块中主动添加header来输出正确编码，添加内容为：add_header Content-Type ‘text/html; charset=utf-8’;这样浏览器就知道我们使用的是哪种编码了，或者把add_header这行换成charset utf-;也是可以的
```nginx
location ~ ^/get_text/article/(.*)_(\d+).html$ {
    default_type text/html;
    set $s $1;
    set $d $2;
    add_header Content-Type ‘text/html; charset utf-8’;
    #charset utf-8;
    return 200 '字符串:$s$d';
}
```