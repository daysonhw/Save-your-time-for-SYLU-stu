# Save your time for SYLU students
### An automatic tool to save your time everyday!  (自动化工具节约您的宝贵时光)  
  
> Once set, works forever (theoredically) --一劳永逸  
> Integrate vaildation units, make sure it's all set --集成验证功能，确保不漏报  
> Integrate mail service for RESULT or ERROR report --集成邮件提醒功能  
> Using mac? You lucky dog, you won't need to worried about configuration, it's open box.  

### How to use it? (如何使用)
---
Initially, you need to grab the request in daily imforme section, transform into base64 form, then insert it to variable 'rawBase64', run the script with python FILENAME. If it's first time you need to input some data, like username and password, it will save the cookie for further purpose.
Using crontab or something else to run it daily.  
首先需要进行一次提交 抓包 获取提交的表单，将其编码为Base64 放入变量’rawBase64‘中，运行脚本在终端中按照说明输入必要的参数，当输出success后即运行成功，之后可以使用crontab 之类的工具定时执行一次即可。

### Step Further
---
If you are using Darwin, it will imform you progress by using system notification. If you are using other operating system, there're another feature for you, but it take a bit of time. Just go to IFTTT create an API and fill these variables.
