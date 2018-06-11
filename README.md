#### Slot公共模块UI自动化测试 - Web
* 使用 `flask` 实现服务端口，通过页面调用端口运行测试
* 使用 `python3 Unittest` 、 `selenium3` 、 `JavaScript` 实现slot游戏公共模块UI自动化测试
* 测试过程若抛出异常会自动截图保存，并借助 `HTMLTestReportCN` 生成测试报告
* 生成报告的插件：https://github.com/Gelomen/HTMLTestReportCN-ScreenShot

#### 目录结构
```
SlotCommonTest
    |
    +-- app                                               # Flask app 目录
    |    |
    |    +-- automatedTest                                # 自动化测试目录
    |    |         |
    |    |         +-- slot                               # slot类，以后可能会有mchat
    |    |         |     |
    |    |         |     +-- assets                       # 资源目录
    |    |         |     |     |
    |    |         |     |     +-- config.ini             # 本地版本的游戏配置文件，在web版没用到
    |    |         |     |     +-- GMAndOdds.xlsx         # 测试赔付用例用到的配置表
    |    |         |     |
    |    |         |     +-- lib                          # 外部插件目录
    |    |         |     |    |
    |    |         |     |    +-- chromedriver.exe        # webdriver 插件
    |    |         |     |    +-- HTMLTestReportCN.py     # unittest测试报告插件，为web版改写过
    |    |         |     |
    |    |         |     +-- source                       # slot 测试的源码
    |    |         |     |     |
    |    |         |     |     +-- common                 # 公共文件夹
    |    |         |     |     |      |
    |    |         |     |     |      +-- Browser.py      # 初始化webdriver
    |    |         |     |     |      +-- Common          # 自动化测试用到的各种操作都写在里面
    |    |         |     |     |      +-- CustomRun       # 运行自定义用例
    |    |         |     |     |      +-- ReadGM.py       # 读取测试赔付用的GM
    |    |         |     |     |      +-- RunAllTests.py  # 运行所有用例
    |    |         |     |     |
    |    |         |     |     +-- testcase               # 测试用例目录
    |    |         |     |     |      |
    |    |         |     |     |      +-- TestGameAttr.py
    |    |         |     |     |      +-- ..
    |    |
    |    +-- main                                         # Flask web 相关文件夹
    |    |    |
    |    |    +-- AnalyzeSlotCustomJson.py                # 运行自定义用例时，需要将 json 解析出现游戏属性和用例
    |    |    +-- GameAttr.py                             # 用于保存从 web 获得的游戏属性
    |    |    +-- HostIp.py                               # 获取当前主机 ip，用于拼接报告链接使用
    |    |    +-- SlotReport.py                           # 获取所有报告，同时可以打开报告和删除报告
    |    |    +-- SlotTestDoc.py                          # 获取所有测试用例的类名、用例名，以及他们的中文描述
    |    |
    |    +-- static                                       # Flask 静态文件夹
    |    |     |
    |    |     +-- slot                                   # slot 分类的报告文件夹，以后可能有 mchat 的
    |    |     |    |
    |    |     |    +-- [3303]CommonTestReport..          # slot 测试报告，需为英文名字，否则 IIS 不能正常读取
    |    |
    |    +-- RunApp.py                                    # 启动 Flask app，web 的接口都在这里
    |    +-- web.config                                   # IIS 配置文件
    |
    +-- venv                                              # 虚拟环境目录
    +-- .gitignore
    +-- README.md
    +-- requirements.txt                                  # 项目所需依赖及版本记录文件
    +-- web.log                                           # IIS 服务的log
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
|~/RunAllTests|运行所有用例|POST|lobby,tester,username,password,<br/>gameId,gameName,fullLine,<br/>fullLineMulitiplier,lineNumMin,lineNumMax,<br/>lineCost,autoGameTimes|http://server-ip:5000/RunAllTests|
|~/allTestDoc|获取所有用例的名字和描述|GET|无|http://server-ip:5000/allTestDoc|
|~/allReports|获取所有报告名字和链接|GET|无|http://server-ip:5000/allReports|
|~/report/:reportname|打开报告页面|GET|reportname|http://server-ip:5000/report/【希腊传说】公共模块测试报告V1.1|

##### 5. 详情
具体安装配置请查看 [WIKI](https://github.com/Gelomen/SlotCommonTest/wiki)