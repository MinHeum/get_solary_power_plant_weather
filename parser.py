import requests, json, csv
from urllib.request import urlopen

url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
req_service_key = '?serviceKey=44aQB7sVFWrqaxR74AML73ldow%2BVsbLvf9roE3Hg5arKLW5TMAU92AkTwum9sG0TTWkT%2ByeME6fjl7xYw5CjXQ%3D%3D'
req_type = '&dataType=JSON'
req_datatype = '&dataCd=ASOS'
req_datetype = '&dateCd=DAY'
req_start_date = '&startDt='
req_end_date = '&endDt='
req_observatroy_no = '&stnIds='
num_of_rows = '&numOfRows=365'

year = int(input("조회할 년도: "))

# 윤년 처리
leaf_year = False
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): leaf_year = True


month = input("조회할 월: ")
if len(month) == 1: month = '0'+ month

day = '31'
_30 = ['04','06','09','11']
if month in _30:
    day = '30'
if month == '02':
    if leaf_year: day = '28'
    else: day = '29'

obs_lst = """
 1) 경상대태양광
 2) 광양항세방태양광
 3) 구미태양광
 4) 두산태양광
 5) 삼천포태양광
 6) 여수태양광
 7) 영동태양광
 8) 영흥태양광
 9) 예천태양광
10) 탑선태양광
"""

print(obs_lst)

obs_no = input("조회할 관측소: ")
obs_dt = {"1":192,"2":266,"3":279,"4":155,"5":295,"6":168,"7":105,"8":112,"9":273,"10":156}

req_start_date = req_start_date + str(year) + month + '01'
req_end_date = req_end_date + str(year) + month + day
req_observatroy_no = req_observatroy_no + str(obs_dt[obs_no])

# url 완성
req_url = url + req_service_key + req_type + req_datatype + req_datetype + req_start_date + req_end_date + req_observatroy_no + num_of_rows

resp = requests.get(req_url)
dt = json.loads(resp.text)
data = dt['response']['body']["items"]["item"]
days = len(data)

arr = [0.0] * 5
for i in data:
    print(i["tm"]+"\t"+i["stnNm"]+'\t평균 기온: '+i["avgTa"]+'\t합계 일조시간: '+i["sumSsHr"]+'\t평균 상대습도: '+i["avgRhm"]+"\t평균 전운량: "+i["avgTca"]+"\t평균 중하층운량: "+i["avgLmac"])
    arr[0] += float(i["avgTa"])
    arr[1] += float(i["sumSsHr"])
    arr[2] += float(i["avgRhm"])
    arr[3] += float(i["avgTca"])
    arr[4] += float(i["avgLmac"])

print("=======================================================================================================================================================")
print('"월 평균 기온: %.2f\t월 평균 일조시간: %.2f시간\t월 평균 상대습도: %.2f%%\t월 평균 전운량: %.2f(10분위)\t월 평균 중하층운량: %.2f(10분위)'%(arr[0]/days,arr[1]/days,arr[2]/days,arr[3]/days,arr[4]/days))
    


