## Slot公共模块UI自动化测试 - Web

* 使用 `flask` 实现服务端口，通过页面调用端口运行测试
* 使用 `python3 Unittest` 、 `selenium3` 、 `JavaScript` 实现slot游戏公共模块UI自动化测试
* 测试过程若抛出异常会自动截图保存，并借助 `HTMLTestReportCN` 生成测试报告
* 生成报告的插件：https://github.com/Gelomen/HTMLTestReportCN-ScreenShot

## 目录结构

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


## 使用说明

### 1. 浏览器

selenium UI自动化测试用的浏览器一般有 chrome、Firefox、IE、Opera 和 Safari，本项目使用的是 chrome 浏览器，所以建议安装 chrome。

### 2. 启动服务

#### 开发模式

打开 `app\RunApp.py` 启动服务

#### 正式环境

参考：[使用 IIS 在 Windows 部署 Flask 网站](https://gelomen.github.io/Flask/%E4%BD%BF%E7%94%A8-IIS-%E5%9C%A8-Windows-%E9%83%A8%E7%BD%B2-Flask-%E7%BD%91%E7%AB%99.html)

### 3. 相关接口

服务器端口：http://server-ip:5000/

#### 运行所有用例

API：~/slot/RunAllTests
类型：POST
参数：lobby,tester,username,password,gameId,gameName,fullLine,fullLineMulitiplier,lineNumMin,lineNumMax,lineCost,autoGameTimes
示例：http://server-ip:5000/slot/RunAllTests

#### 运行自定义用例

API：~/slot/RunCustomTests
类型：POST
参数：lobby,tester,username,password,gameId,gameName,fullLine,fullLineMulitiplier,lineNumMin,lineNumMax,lineCost,autoGameTimes，以及测试的类名和测试用例名字
参数格式：

```json
[{"game_attr": {
            "lobby": "https://lobby.fg.blizzmi.cn",
            "tester": "Gelomen",
            "username": "automatedTest1",
            "password": "123456",
            "gameId": "3303",
            "gameName": "众神之王",
            "fullLine": "True",
            "fullLineMulitiplier": "50",
            "lineNumMin": "1",
            "lineNumMax": "25",
            "lineCost": "1, 2, 5, 10, 50, 100, 500, 1000",
            "autoGameTimes": "25, 50, 100, 200, 500, -1"
        },
        "test_case": [
            {"key": "TestReward", "value": "test_reward"}
        ]
    }
]
```

示例：http://server-ip:5000/slot/RunAllTests

#### 停止测试运行

API:~/StopAllTests/<pid>
类型：GET
测试：<pid>
示例：http://server-ip:5000/StopAllTests/5566

#### 获取所有用例的名字和描述

API：~/slot/allTestDoc
类型：GET
参数：无
示例：http://server-ip:5000/slot/allTestDoc

#### 获取所有报告名字和链接

API：~/slot/allReports
类型：GET
参数：无
示例：http://server-ip:5000/slot/allReports

#### 打开报告页面

API：~/slot/report/<report_name>
类型：GET
参数：<report_name>
示例：http://server-ip:5000/slot/report/[3303]CommonTestReport

#### 删除报告

API：~/slot/delete_report/<report_name>
类型：GET
参数：<report_name>
示例：http://server-ip:5000/slot/delete_report/report/[3303]CommonTestReport 
