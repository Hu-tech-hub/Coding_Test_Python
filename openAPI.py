import requests
import os
import re

def safe_filename(text, max_length=100):
    text = re.sub(r'[\\/*?:"<>|]', '_', text)
    text = text.replace('(', '').replace(')', '')
    return text[:max_length].strip()

# API 기본 설정
url = "https://apis.data.go.kr/B410001/cmmrcFraudCase/cmmrcFraudCase"
service_key = "ZFx8F0sm0Qgs06Solg4q98FfxzCQYhiPlzs6Xp8hjbC8ZyHuuiZoDbJmBos8nGSWkxHpcB7U1uYE6jqmMRMFfQ=="

# 저장 폴더 생성
os.makedirs("fraud_cases_html", exist_ok=True)

# ✅ 1. 전체 건수 확인
params = {
    'serviceKey': service_key,
    'type': 'json',
    'numOfRows': 1,
    'pageNo': 1
}
res = requests.get(url, params=params)
data = res.json()
total_cnt = int(data['response']['body']['totalCnt'])

# ✅ 2. 페이지 수 계산
num_per_page = 10
total_pages = (total_cnt + num_per_page - 1) // num_per_page

print(f"🔍 전체 사례 수: {total_cnt}건 → {total_pages} 페이지 처리 예정")

# ✅ 3. 페이지별 요청 및 저장
for page in range(1, total_pages + 1):
    params = {
        'serviceKey': service_key,
        'type': 'json',
        'numOfRows': num_per_page,
        'pageNo': page
    }

    res = requests.get(url, params=params)
    data = res.json()
    items = data['response']['body']['itemList']['item']

    for i, item in enumerate(items):
        try:
            # 파일 저장 시:
            title_raw = item['titl']
            title_clean = safe_filename(title_raw)
            filename = f"fraud_cases_html/{(page-1)*num_per_page + i + 1:03d}_{title_clean}.html"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(item['bdtCntnt'])
        except Exception as e:
            print(f"❌ 저장 실패 (페이지 {page}, 항목 {i}): {e}")

print("✅ 전체 HTML 저장 완료!")
