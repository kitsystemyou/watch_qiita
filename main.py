import requests

headers = {"Authorization": "Bearer 85675154253e23be371435a1db86cc7df3c6dba1"}
res = requests.get("https://qiita.com/api/v2/items/5be1ed392c12cde150e4", headers=headers)
print(res.status_code)
if res.status_code != 200:
    print(res.status_code, res.json())

res_data = res.json()
print(res_data["id"])
print(res_data["page_views_count"])
print(res_data["url"])

