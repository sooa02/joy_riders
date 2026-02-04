class ApiOil:
    def getdata(self, oil_type: str) -> int:
        import xml.etree.ElementTree as ET

        xml_data = """
        <RESULT>
            <OIL>
                <TRADE_DT>20260204</TRADE_DT>
                <PRODNM>고급휘발유</PRODNM>
                <PRICE>1929.12</PRICE>
            </OIL>
            <OIL>
                <TRADE_DT>20260204</TRADE_DT>
                <PRODNM>휘발유</PRODNM>
                <PRICE>1687.54</PRICE>
            </OIL>
            <OIL>
                <TRADE_DT>20260204</TRADE_DT>
                <PRODNM>자동차용경유</PRODNM>
                <PRICE>1581.53</PRICE>
            </OIL>
        </RESULT>
        """

        root = ET.fromstring(xml_data)

        for oil in root.findall('OIL'):
            prod_name = oil.find('PRODNM').text
            price = oil.find('PRICE').text

            if prod_name == oil_type:
                return int(float(price))

        return -1


if __name__ == "__main__":
    api = ApiOil()
    print(api.getdata("휘발유"))
    print(api.getdata("자동차용경유"))
