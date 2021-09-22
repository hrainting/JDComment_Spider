# -*- encoding: utf-8 -*-
from enum import Flag
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import numpy as np
import requests
import json
import csv
import io

# 保存评论数据
def commentSave(list_comment):
    '''
    list_comment: 二维list,包含了多条用户评论信息
    '''
    file = io.open('JDComment_data.csv','w',encoding="utf-8",newline = '')
    writer = csv.writer(file)
    writer.writerow(['用户ID','评论内容','购买时间','点赞数','回复数','得分','评价时间','手机型号'])
    for i in range(len(list_comment)):
        writer.writerow(list_comment[i])
    file.close()
    print('存入成功')

def getCommentData(format_url,proc,i,maxPage):
    '''
    format_url: 格式化的字符串架子，在循环中给它添上参数
    proc: 商品的productID，标识唯一的商品号
    i: 商品的排序方式，例如全部商品、晒图、追评、好评等
    maxPage: 商品的评论最大页数
    '''
    sig_comment = []
    global list_comment
    cur_page = 0
    while cur_page < maxPage:
        cur_page += 1
        # url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv%s&score=%s&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1'%(proc,i,cur_page)
        url = format_url.format(proc,i,cur_page) # 给字符串添上参数
        try:
            response = requests.get(url=url, headers=headers, verify=False)
            time.sleep(np.random.rand()*2)
            jsonData = response.text
            startLoc = jsonData.find('{')
            #print(jsonData[::-1])//字符串逆序
            jsonData = jsonData[startLoc:-2]
            jsonData = json.loads(jsonData)
            pageLen = len(jsonData['comments'])
            print("当前第%s页"%cur_page)
            for j in range(0,pageLen):
                userId = jsonData['comments'][j]['id']#用户ID
                content = jsonData['comments'][j]['content']#评论内容
                boughtTime = jsonData['comments'][j]['referenceTime']#购买时间
                voteCount = jsonData['comments'][j]['usefulVoteCount']#点赞数
                replyCount = jsonData['comments'][j]['replyCount']#回复数目
                starStep = jsonData['comments'][j]['score']#得分
                creationTime = jsonData['comments'][j]['creationTime']#评价时间
                referenceName = jsonData['comments'][j]['referenceName']#手机型号
                sig_comment.append(userId)#每一行数据
                sig_comment.append(content)
                sig_comment.append(boughtTime)
                sig_comment.append(voteCount)
                sig_comment.append(replyCount)
                sig_comment.append(starStep)
                sig_comment.append(creationTime)
                sig_comment.append(referenceName)
                list_comment.append(sig_comment)
                print(sig_comment)
                sig_comment = []
        except:
            time.sleep(5)
            cur_page -= 1
            print('网络故障或者是网页出现了问题，五秒后重新连接')
            

if __name__ == "__main__":
    global list_comment
    ua=UserAgent()
    format_url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&{0}&score={1}&sortType=5&page={2}&pageSize=10&isShadowSku=0&fold=1'
    # 设置访问请求头
    headers = {
    'Accept': '*/*',
    'Host':"club.jd.com",
    "User-Agent":ua.random,
    'Referer':"https://item.jd.com/",
    'sec-ch-ua':"\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode':'no-cors',
    'Sec-Fetch-Site':'same-site',
    'cookie':'shshshfpa=d7652284-2677-e442-f65b-a18ed2e089b7-1611056071; shshshfpb=eOUYl%2FyuXFYLwv7eDtH4YLQ%3D%3D; TrackID=1hKarizYZ57NdV7srtnM1enex0Jh0YC4lJzRM1MkwReFRx-4w3xU-pLqDgyLLN0QL6ZjmgfchOqm3Gaiei6xQMr4vnf6in90SyUxGti7Nj3KkfUhWNHsVlHkoh_PX5Xy_; pinId=O67PJVPQj-o0uoFFSsfdKbV9-x-f3wj7; __jdu=16110560689641627630371; areaId=17; ipLoc-djd=17-1381-50713-0; PCSYCityID=CN_420000_420100_0; jwotest_product=99; unpl=V2_ZzNtbUIDEBV3CxRVLhBVVWIAEA9KVxdFIA9FUywdXwJmABdbclRCFnUUR1xnGl8UZgsZXEtcQRNFCEdkeRtdAGcAElVCZ3Mldgh2VUsZWwVnAhZaQ1BKHXINRlN4H1sHZgEUXXJnRBV8OHZkfhldBGUCFFlKU3MURQpHVXkfWQxmARJtCTlCWHUPRlR6HVsEYAoaWkdXRBZzD0RVeR9cNWYzEQ%3d%3d; __jdv=76161171|so.lenovo.com.cn|t_330412191_|tuiguang|1eb132c0d88a423c91ead626f5260247|1632272918632; __jda=122270672.16110560689641627630371.1611056068.1632243773.1632272919.12; __jdc=122270672; shshshfp=584a61554b96a42cfd5822b0ec3ee825; token=b3ac5da7d1c549943edd123efec3012c,2,906818; __tk=1YG51YTt2crXrAs41Y1AKcrurYq3KwsE1wG41YbXrcx,2,906818; shshshsID=b8c17506eb627f5ecff334470524ef9e_5_1632272955907; __jdb=122270672.5.16110560689641627630371|12.1632272919; 3AB9D23F7A4B3C9B=S5CLGPTR2H6IRDRTAFWABV3CMBJFK3PVUEUK2DO6D6I645RWP5BFUQ4LATFKJXPLQHQVCDXNFTWOSBS54ZHSVFYX64'
    }
    #手机四种颜色对应的产品id参数
    productid = ['productId=100010594803','productId=100019141912','productId=100019141872','productId=100018886680']
    list_comment = [[]]
    sig_comment = []
    for proc in productid:#遍历产品颜色
        i = -1
        while i < 7:#遍历排序方式
            i += 1
            if(i == 6):
                continue
             #先访问第0页获取最大页数，再进行循环遍历
            url = format_url.format(proc,i,0)
            print(url)
            try:
                response = requests.get(url=url, headers=headers, verify=False)
                jsonData = response.text
                startLoc = jsonData.find('{')
                jsonData = jsonData[startLoc:-2]
                jsonData = json.loads(jsonData)
                print("最大页数%s"%jsonData['maxPage'])
                getCommentData(format_url,proc,i,jsonData['maxPage'])#遍历每一页
            except Exception as e:
                i -= 1
                print("the error is ",e)
                print("wating---")
                time.sleep(5)
                #commentSave(list_comment)
    print("爬取结束，开始存储-------")
    commentSave(list_comment)
