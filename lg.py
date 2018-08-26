import requests
from requests.exceptions import RequestException
import time
import re
headers = {
    "Host": "www.lagou.com",
    "Origin": "https://www.lagou.com",
    "Referer": "https://www.lagou.com/jobs/list_Python?px=default&city=%E6%88%90%E9%83%BD",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": "None",
    "X-Requested-With": "XMLHttpRequest"
}
url = "https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E6%88%90%E9%83%BD&needAddtionalResult=false"
def get_page_url(page):
    data = {
    "first": "false",
    "pn": page,
    "kd": "Python"
    }
    try:
        response = requests.post(url,headers=headers,data=data)
        if response.status_code == 200 :
            content = response.text
            return content
        return None
    except RequestException:
        get_page_url(page)
    time.sleep(3)

def parse_page_html(content):
    parttern =re.compile('.*?"companyShortName":"(.*?)".*?"education":(.*?)".*?"workYear":"(.*?)".*?"salary":"(.*?)".*?"positionName":"(.*?)".*?"linestaion":"(.*?)"',re.S)
    companies = re.findall(parttern,content)
    return companies
def save_to_data(data):
    occupation = str(data)
    with open("occupation.txt",'a',encoding="utf-8") as f:
        f.write(occupation+'\n')
        f.close()
def main():
    for page in range(1,2):
        content = get_page_url(page)
        datas = parse_page_html(content)
        for data in datas:
            save_to_data(data)
            print("存储数据成功")
if __name__ == "__main__":
    main()