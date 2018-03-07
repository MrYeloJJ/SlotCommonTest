# SlotCommonTest
#### Slot公共模块UI自动化测试
* 使用 `python3 Unittest` 、 `selenium3` 、 `JavaScript` 实现slot游戏公共模块UI自动化测试
* 测试过程若抛出异常会自动截图保存，并借助 `HTMLTestReportCN` 生成测试报告
* 生成报告的插件：https://github.com/Gelomen/HTMLTestReportCN-ScreenShot

#### 目录结构
```
SlotCommonTest
    |
    +-- src
    |    +-- assets                                 // 数据目录
    |    |    +-- data.xml
    |    +-- lib                                    // 插件
    |    |    +-- chromedriver.exe
    |    |    +-- HTMLTestReportCN.PY
    |    +-- result                                 //测试报告目录
    |    |    +-- README.md
    |    +-- source                                 // 源码目录
    |    |    +-- common                            // 公共类目录
    |    |    |    +-- Common.py
    |    |    |    +-- Data.py
    |    |    |    +-- RunAllTests.py               // 执行这个可以跑所有用例并生成测试报告
    |    |    +-- testcases                         // 测试用例
    |    |    |    +-- TestLoadingView.py
    |    |    |    +-- TestMainAndComView.py
    |    |    |    +-- ...
    +-- venv                                        // 虚拟环境
    +-- .gitignore
    +-- README.md
    +-- requirements.txt
```


#### 使用说明

