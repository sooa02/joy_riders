from API_Side.APICaller import APICaller

class APICaller_Sample(APICaller):
    def getdata(self, *args):
        """
        :param args: [url, Client-ID, Client-Secret, search_input]
        :return:
        """

        headers = {
            "X-Naver-Client-Id": args[1],
            "X-Naver-Client-Secret": args[2]
        }

        params = {
            "query": args[3],
            "display": 20,
            "start": 1,
            "sort": "date"
        }

        dapi = self.downloadapi(args[0], headers, params)

        res = []
        for i in dapi.json()['items']:
            res.append(i['description'])

        return res