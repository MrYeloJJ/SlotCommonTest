@echo off
echo ================================================
echo =              启动自动化测试服务              =
echo ================================================
call E:\Gelomen\PycharmProjects\SlotCommonTest\venv\Scripts\activate
call cd E:\Gelomen\PycharmProjects\SlotCommonTest\app\
call e: 
call python RunApp.py
@echo