#### Slot公共模块UI自动化测试 - Local
* 使用 `python3 Unittest` 、 `selenium3` 、 `JavaScript` 实现slot游戏公共模块UI自动化测试
* 测试过程若抛出异常会自动截图保存，并借助 `HTMLTestReportCN` 生成测试报告
* 生成报告的插件：https://github.com/Gelomen/HTMLTestReportCN-ScreenShot

#### 目录结构
```
SlotCommonTest
    |
    +-- src
    |    +-- assets                                 // 数据目录
    |    |    +-- config.ini
    |    +-- lib                                    // 插件目录
    |    |    +-- chromedriver.exe
    |    |    +-- HTMLTestReportCN.py
    |    +-- result                                 // 测试报告目录
    |    |    +-- sample                            // 测试报告例子
    |    |    +-- README.md
    |    +-- source                                 // 源码目录
    |    |    +-- common                            // 公共类目录
    |    |    |    +-- Common.py
    |    |    |    +-- Data.py
    |    |    |    +-- RunAllTests.py               // 执行这个可以跑所有用例并生成测试报告
    |    |    |    +-- ...
    |    |    +-- testcases                         // 测试用例目录
    |    |    |    +-- TestLoadingView.py
    |    |    |    +-- TestMainAndComView.py
    |    |    |    +-- ...
    +-- venv                                        // 虚拟环境目录
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

##### 3. 启动
打开 `src/source/common/RunAllTests.py`，执行后根据控制台提示，输入自己的名字就可以开始测试

##### 4. 测试过程
测试过程每完成一条用例，控制台会打印用例名字，用例前面的符号分别代表：
`S = Success`、`F = Failure` 和 `E = Error`

##### 5. 测试结束
所有用例跑完结束，控制台会有蓝绿色提示文字，这时打开目录：
`src/result`，根据文件夹名字（时间）打开对应的html测试报告即可

##### 6. 详情
具体安装配置请查看 [WIKI](https://github.com/Gelomen/SlotCommonTest/wiki)