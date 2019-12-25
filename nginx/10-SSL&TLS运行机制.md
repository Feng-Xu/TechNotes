### SSL证书

![](https://github.com/Feng-Xu/feng-xu.github.io/blob/master/my_image/SSL.png)

* 域名验证（domain validate的，DV）证书
验证域名的归属是否正确
* 组织验证（organization validate的，OV）证书
验证当时申请证书填写机构，组织名称是否正确
* 扩展验证（extended validation，EV）证书
更严格，浏览器中会显示名称


### TLS通讯过程
1. 验证身份
2. 达成安全套件共识
3. 传递秘钥
4. 加密通讯

#### 具体过程
![](https://github.com/Feng-Xu/feng-xu.github.io/blob/master/my_image/TLS.png)
1. client hello
	1. 可用的版本号
	2. 当前时间
	3. 客户端随机数
	4. 会话ID
	5. 可用的密码套件清单
	6. 可用的压缩方式清单
- - - -
1. server hello
	1. 使用的版本号
	2. 当前时间
	3. 服务器随机数
	4. 会话ID
	5. 使用的密码套件
	6. 使用的压缩方式
2. certificate 服务器证书
3. serverKeyExchange（该步主要针对DH，提供DH的公钥信息）
	1. RSA情况（公钥密码参数、散列值）
	2. Diffie-Hellman对称秘钥交换情况
4. CertificateRequest
	1. 服务器能理解的证书类型清单
	2. 服务器能理解的认证机构名称清单
5. ServerHelloDone  	
- - - -
1. Certificate 客户端证书
2. ClientKeyExchange
	1. RSA情况（经过加密的预备主密码pre-master-key：客户端再随机生成一个数，然后使用服务器的公钥进行加密）
	2. Diffie-Hellman对称秘钥交换情况
3. CertificateVerity 数字签名
4.  ChangeCipherSpec 更换加密方式
5. Finished
- - - -
1. ChangeCipherSpec 更换加密方式
2. Finished

至此，整个握手阶段全部结束。接下来，客户端与服务器进入加密通信，就完全是使用普通的HTTP协议，只不过用"会话密钥"加密内容(HTTP+SSL/TLS).
