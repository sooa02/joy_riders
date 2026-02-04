from API_Side.APICaller_Sample import APICaller_Sample as SMP

c = SMP()

res = c.getdata(
    "https://openapi.naver.com/v1/search/news.json",
    "",
    "",
    "인공지능"
)

for l in res:
    print("==========================")
    print(l)
