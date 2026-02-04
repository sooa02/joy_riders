import xml.etree.ElementTree as ET
import urllib.request

class ApiOil:
    def getdata(self, oil_type: str) -> float:
        url = "https://www.opinet.co.kr/api/avgAllPrice.do?out=xml&code=F260204142"

        # 1. 오피넷 API 호출
        with urllib.request.urlopen(url) as response:
            xml_data = response.read().decode("utf-8")

        # 2. XML 데이터 파싱
        root = ET.fromstring(xml_data)

        # 3. 유종 이름으로 가격 찾기
        for oil in root.findall("OIL"):
            prod_name = oil.find("PRODNM").text
            price = oil.find("PRICE").text

            if prod_name == oil_type:
                return float(price)  # 정수 가격 반환

        # 4. 해당 유종이 없을 경우
        return -1.0


apioil = ApiOil()
