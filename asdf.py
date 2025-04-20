import requests

url = "https://apis.data.go.kr/B410001/cmmrcFraudCase/cmmrcFraudCase"
service_key = "ZFx8F0sm0Qgs06Solg4q98FfxzCQYhiPlzs6Xp8hjbC8ZyHuuiZoDbJmBos8nGSWkxHpcB7U1uYE6jqmMRMFfQ=="

params = {
    'serviceKey': service_key,
    'type': 'json',
    'numOfRows': 1,   # 1개만 요청해도 totalCnt는 포함됨
    'pageNo': 1
}

response = requests.get(url, params=params)
data = response.json()

total_cnt = int(data['response']['body']['totalCnt'])
print(f"✅ 전체 무역사기 사례 개수: {total_cnt}건")
