# 1.16.1 - 2018-08-15
## Feature
-fixed bugs
## Bug

## Config

# 1.16.0 - 2018-08-13
## Feature
-新增5J
## Bug

## Config

# 1.15.0 - 2018-08-02
## Feature
-新增PAM
## Bug

## Config

# 1.14.1 - 2018-07-27
## Feature

## Bug
-9c修复存在爬取商务舱的问题
## Config

# 1.14.0 - 2018-07-27
## Feature
-9c切换爬虫渠道到小程序爬取
## Bug

## Config

# 1.13.2 - 2018-07-24
## Feature

## Bug
- 修复儿童价提取错误
## Config

# 1.13.1 - 2018-07-23
## Feature

## Bug
- 移出pyv8
## Config

# 1.13.0 - 2018-07-23
## Feature
- 新增对ipcc:LCJC_F的支持
## Bug

## Config

# 1.12.1 - 2018-06-29
## Feature

## Bug

- 修复9C存在的oneTrip问题

## Config

# 1.12.0 - 2018-06-28
## Feature
- 兼容lcc_shopping2.0
## Bug

## Config

# 1.11.3 - 2018-06-20
## Feature

## Bug

- 兼容虎航新版请求问题
- 修复格式话往返处理错误问题

## Config

# 1.11.2 - 2018-06-20
## Feature

## Bug

- 修改时间格式化Bug

## Config

# 1.11.1 - 2018-06-12
## Feature

## Bug

- 时间由北京时间改为当地时间
- 修改增加儿童价格判断

## Config

# 1.11.0 - 2018-06-12
## Feature

- 增加9C抓数

## Bug

## Config

# 1.10.0 - 2018-04-26
## Feature

- 移出切换代理定时器

## Bug

## Config

# 1.9.0 - 2018-04-24
## Feature

- 添加切换代理定时器

## Bug

## Config
- 修改 [proxy1] 的代理配置：
```
dynamicProxy=duoipmrvnmtwl:AwijmbH5BovCw@222.184.35.215:41369
switchTime=300
switchProxy=http://ip4.hahado.cn/simple/switch-ip?username=duoipmrvnmtwl&password=AwijmbH5BovCw
```

# 1.8.5 - 2018-04-20
## Feature

## Bug

- 修复启动时错误导入模块bug

## Config

# 1.8.4 - 2018-04-20
## Feature

## Bug

- 解决TGAU被封时的处理
- 解决缓存代理存在的bug

## Config


# 1.8.3 - 2018-04-17
## Feature

## Bug

- 修复TGAU表单时候颠倒

## Config

# 1.8.2 - 2018-04-17
## Feature

## Bug

- 修复往返机场颠倒bug

## Config


# 1.8.1 - 2018-04-16
## Feature

## Bug

- 修护TGAU可能存机型为空
- 修护缓存代理存在的bug

## Config

- 修改 [proxy1] 的代理配置：
```
[proxy1]
dynamicProxy=duoipsnukthiy:l7MtH3xk3Or7s@222.184.35.215:37882
switchTime=1800
switchProxy=http://ip4.hahado.cn/simple/switch-ip?username=duoipsnukthiy&password=l7MtH3xk3Or7s
```

# 1.8.0 - 2018-04-10
## Feature

- 移除webdriver逻辑,改为HTTP请求爬虫

## Bug

## Config

- 修改和新增代理配置
```
[proxyconf]
type=2
switch=1
[proxy1]
dynamicProxy=duoipcnecxnjgbb:DrEYcAucoGPK5@222.184.35.215:35779
switchTime=1800
switchProxy=http://ip4.hahado.cn/simple/switch-ip?username=duoipcnecxnjgbb&password=DrEYcAucoGPK5
[proxy2]
targetSiteName=TT
dynamicProxy=http://61.160.207.39:4208/comm/getHttpProxyRaw.do
```

# 1.7.0 - 2018-04-02
## Feature

- 增加是否使用代理配置

## Bug

## Config

- config file :`/data/config/lcc-spider/config.properties` 添加代理开关
```
[proxy]
switch=0
```


# 1.6.0 - 2018-03-30
## Feature

- 移出定时器修改代理IP

## Bug

## Config

# 1.5.0 - 2018-03-28
## Feature

- Chrome集成动态代理

## Bug

## Config

- 增加动态代理配置

```
[proxy]
dynamicProxy=duoipcnfpbzolzf:C0TWvAaIJyXwD@222.184.35.215:35686
switchTime=1800
switchProxy=http://ip4.hahado.cn/simple/switch-ip?username=duoipcnfpbzolzf&password=C0TWvAaIJyXwD

```

# 1.4.4 - 2018-03-22
## Feature

## Bug

- 虎航修改为en环境下爬取

## Config

# 1.4.3 - 2018-03-22
## Feature

## Bug

- 修复虎航childNumber默认不为0

## Config

# 1.4.2 - 2018-03-21
## Feature

## Bug

- 修复澳洲虎航座位数截取错误

## Config

# 1.4.1 - 2018-03-20
## Feature

## Bug

- 修复tiger不加载jquery

## Config

# 1.4.0 - 2018-03-20
## Feature

- 增加澳洲虎航爬虫

## Bug

## Config

# 1.3.0 - 2018-03-12
## Feature

- 不再处理机场三字码转城市三字码

## Bug

## Config

# 1.2.0 - 2018-03-12
## Feature

- 修改stopCity字段问题，现在都把此字段置为空
- 机型信息字段置为空

## Bug

## Config

# 1.1.1 - 2018-03-05
## Feature

## Bug

- 修复en_US下座位匹配不正确

## Config

# 1.1.0 - 2018-02-22
## Feature
- Increase support for discounts

## Bug

## Config

# 1.0.0 - 2018-02-08
## Feature
- support Asia

## Bug

## Config
- config file :`/data/config/lcc-spider/config.properties`  
- config value

```
[server]
port=9000

[browser]
chromedriver=/data/opt/python/chromedriver

[spider]
timeout=40
maxThread=10

```

# Precondition
## create a none-root

```
user:lcc
passwd:spider

useradd lcc && echo spider | passwd --stdin lcc
```

## install related package

```
# Xvfb
yum -y install Xvfb libXfont xorg-x11-fonts* unzip

# chrome
/etc/yum.repos.d/google-chrome.repo
cat >> /etc/yum.repos.d/google-chrome.repo << END
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
END

yum -y install google-chrome-stable --nogpgcheck

# chromedriver
wget --http-user=***  --http-passwd=***#1T http://svn.worthytrip.net:60081/svn/lcc/bin/chromedriver_linux64.zip -P  /data/source/
unzip /data/source/chromedriver_linux64.zip -d /data/opt/python/
# add chromedriver to the PTAH, /data/opt/python/

```

## create related folder

```
user:lcc
passwd:spider

useradd lcc && echo spider | passwd --stdin lcc

yum -y install Xvfb libXfont xorg-x11-fonts* unzip

mkdir /data/opt/python
mkdir -p /data/config/lcc-spider/
mkdir -p /data/log/python/lcc_spider/
chown -R lcc.lcc /data/log/python/lcc_spider/
```

# deploy
```
# su none-root
su lcc

# start Xvfb
nohup Xvfb -ac :7 -screen 0 1280x1024x8 > /dev/null 2>&1 &
export DISPLAY=:7

# download package and install depends pacakge
wget --http-user=***  --http-passwd=***#1T http://svn.worthytrip.net:60081/svn/lcc/1.0.0/lcc_spider-1.0.0.tar.gz -P /data/source/

tar -zvxf /data/source/lcc_spider-1.0.0.tar.gz -C /data/opt/python/
cd /data/opt/python/lcc_spider && pip install -r requirements.log

# start pacakge
nohup   gunicorn -w 1 -k gthread --threads 10  -b 0.0.0.0:9000 lcc_spider:app    >/dev/null 2>&1 &

```