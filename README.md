#### Slot公共模块UI自动化测试 - Online
* 使用 `flask` 实现服务端口，通过页面调用端口运行测试
* 使用 `python3 Unittest` 、 `selenium3` 、 `JavaScript` 实现slot游戏公共模块UI自动化测试
* 测试过程若抛出异常会自动截图保存，并借助 `HTMLTestReportCN` 生成测试报告
* 生成报告的插件：https://github.com/Gelomen/HTMLTestReportCN-ScreenShot

#### 目录结构
```
SlotCommonTest
    |
    +-- server
    |    |
    |    +-- automaticTest
    |    |    |
    |    |    +-- assets                                // 数据目录
    |    |    |     |
    |    |    |     +-- config.ini
    |    |    +-- lib                                   // 插件目录
    |    |    |     |
    |    |    |     +-- chromedriver.exe
    |    |    |     +-- HTMLTestReportCN.py
    |    |    +-- result                                / 测试报告目录
    |    |    |     |
    |    |    |     +-- sample                          // 测试报告例子
    |    |    |     +-- README.md
    |    |    +-- source                                // 源码目录
    |    |    |     |
    |    |    |     +-- common                          // 公共类目录
    |    |    |     |     |
    |    |    |     |     +-- Common.py
    |    |    |     |     +-- RunAllTests.py            // 执行这个可以跑所有用例并生成测试报告
    |    |    |     +-- testcases                       // 测试用例目录
    |    |    |     |     |
    |    |    |     |     +-- TestLoadingView.py
    |    |    |     |     +-- TestMainAndComView.py
    |    |    |     |     +-- ...
    |    +-- AllReportsName.py
    |    +-- SlotTestServer.py                          // 自动化测试服务文件
    |    +-- TestCaseDoc.py
    +-- venv                                            // 虚拟环境目录
    +-- .gitignore
    +-- README.md
    +-- requirements.txt
```


#### 使用说明
##### 1. 配置
进入数据目录，打开 `config.ini`，修改 *`lobby`* 和 *`game`* 等测试目标游戏属性
```ini
[config]
lobby = https://lobby.fg.blizzmi.cn
tester = Gelomen
username = automatedTest1
password = 123456
gameId = 3303
gameName = 众神之王
fullLine = True
fullLineMulitiplier = 50
lineNumMin = 1
lineNumMax = 25
lineCost = 1, 2, 5, 10, 50, 100, 500, 1000
autoGameTimes = 25, 50, 100, 200, 500, -1
```

##### 2. 浏览器
selenium UI自动化测试用的浏览器一般有 chrome、Firefox、IE、Opera 和 Safari，本项目使用的是 chrome 浏览器，所以建议安装 chrome。

##### 3. 启动服务
打开 `server\SlotTestServer.py` 启动服务

##### 4. 相关接口
服务器端口：http://server-ip:5000/

|接口|描述|类型|参数|示例|
|:--|:--|:--|:--|:--|
|~/RunAllTests|运行所有用例|POST|lobby,tester,username,password<br/>gameId,gameName,fullLine<br/>fullLineMulitiplier,lineNumMin,lineNumMax<br/>lineCost,autoGameTimes|http://server-ip:5000/RunAllTests|
|~/allTestDoc|获取所有用例的名字和描述|GET|无|http://server-ip:5000/allTestDoc|
|~/allReports|获取所有报告名字和链接|GET|无|http://server-ip:5000/allReports|
|~/report/:reportname|打开报告页面|GET|reportname|http://server-ip:5000/report/【希腊传说】公共模块测试报告V1.1|

##### 5. 详情
具体安装配置请查看 [WIKI](https://github.com/Gelomen/SlotCommonTest/wiki)