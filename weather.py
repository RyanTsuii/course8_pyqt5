import requests

def get_data(citykey):
    # 发送GET请求，获取天气数据
    req = requests.get( f'https://api.seniverse.com/v3/weather/daily.json?key=Si1I_iUWRnDMLGWqe&location={citykey}&language=zh-Hans&unit=c&start=0&days=5')
    # 指定响应的编码格式为utf-8
    req.encoding = 'utf-8'
    # 将响应的JSON格式的数据解析为Python对象并返回
    return req.json()

# 定义一个类存放某天的天气情况
class city_weather:
    def __init__(self, Datas):
        self.date = Datas['date']
        self.text_day = Datas['text_day']
        self.text_night = Datas["text_night"]
        self.high = Datas['high']
        self.low = Datas['low']
        self.wind_direction = Datas['wind_direction']
        self.wind_speed = Datas['wind_speed']
        self.rainfall = Datas['rainfall']
        self.humidity = Datas['humidity']

# 定义一个类存放某地近三天的天气情况
class city_weathers:
    city_weather_list: list[city_weather] = []
    def __init__(self, Datas, city_name):
        self.city_name = city_name
        self.city_weather_list.clear()
        for i in Datas:
            self.city_weather_list.append(city_weather(i))

# 通过城市编码得到当地近三天的天气情况，返回一个city_weathers类
def get_weathers(citykey):
    data = get_data(citykey)
    return city_weathers(data['results'][0]['daily'], citykey)