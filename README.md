# 京东爬虫

感谢大佬的代码，原链接：https://blog.csdn.net/weixin_42474261/article/details/88354134?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522163227861116780261938679%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=163227861116780261938679&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-88354134.first_rank_v2_pc_rank_v29&utm_term=%E4%BA%AC%E4%B8%9C%E8%AF%84%E8%AE%BA%E7%88%AC%E8%99%AB&spm=1018.2226.3001.4187

## 抓取评论的关键字

* 用户ID
* 评论内容
* 会员级别
* 点赞数
* 回复数
* 评价星级
* 购买时间
* 手机型号

## 抓取原理

* 分析京东评论界面数据来源及url规律

* 利用requests库访问json格式评论信息

## 运行环境

* Chrome 版本 72.0.3626.109（正式版本） （64 位）
* Python 3.5.2 :: Anaconda 4.2.0 (64-bit)

## 前置库

核心库如下

* requests
* fake_useragent
* BeautifulSoup

在当前目录下的控制台使用以下命令，批量安装上述相关的程序包

```
pip install -r requirements.txt
```

## 使用方法

### Cookie配置

以下图为例，复制控制台中Header请求中的Cookies字段内容，将其替换代码中`'your cookies'`部分，即可批量访问评论信息，有问题请留言。

![image-20210819134514961](picture/image-20210819134514961.png)



### 爬取脚本SpiderScript.py

将文件下载到本地，cmd进入该文件夹，在配置好Cookie和自己想爬取的商品id后运行

`python SpiderScript.py`

即可执行爬虫脚本，当然也可以通过Pycharm、VS Code等环境直接运行该脚本。

![1551882088853](picture/Snipaste_2019-03-06_22-22-48.PNG) 
(注意：在爬取数据之前，尽量确保网络的稳定，这能提高爬虫的效率，爬完所有数据，会存到data目录下的csv文件中)

(_我在爬取过程中遇到了一个问题_：fake_useragent.errors.FakeUserAgentError: Maximum amount of retries reached

再次感谢另一位大佬，原链接：https://blog.csdn.net/xc_zhou/article/details/106412377

可能是缓存fake_useragent_0.1.11.json的问题(最新的版本），但是这个json文件我无法用wget方法或者浏览器下载下来，

只需要将这个缓存文件放在windows或者linux的缓存目录下：

1.获取临时目录：2.将 fake_useragent_0.1.11.json 放入上述linux 或者 windows的临时目录（这里**大佬**将自己成功运行的json文件提供链接:https://pan.baidu.com/s/1_Qv1LGBSjO2bnF4ocMqhwQ 提取码: 2hpu ）

### 数据处理脚本JDComment_Processing.ipynb
使用Jupyter notebook/lab打开ipynb文件，随后shift+enter逐步执行，即可看到数据处理过程(每个单元格的执行情况)

## 数据处理

在JDComment_Processing中包含了数据清洗、数据分析的整个过程（附注释与分析），使用的IDE是jupyter。数据规模有限，分析过程仅供参考。
