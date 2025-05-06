from dotenv import load_dotenv
import os
from fastmcp import FastMCP, Client
import datetime

sys_date = datetime.now().strftime("%Y%m%d")

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
OPENWEATHER_CITY = os.getenv("OPENWEATHER_CITY")


import requests
import asyncio



mcp = FastMCP(
    name="weather_mcp",
    instructions="국내/해외 날씨를 조회하는 mcp server",
    port=7000
)


global_weather_tool_description = '''
해외 도시의 날씨를 조회하는 도구 입니다.
조회 가능한 국가의 목록은 아래와 같습니다.

'sq': 'Albanian'
'af': 'Afrikaans'
'ar': 'Arabic'
'az': 'Azerbaijani'
'eu': 'Basque'
'be': 'Belarusian'
'bg': 'Bulgarian'
'ca': 'Catalan'
'zh_cn': 'Chinese Simplified'
'zh_tw': 'Chinese Traditional'
'hr': 'Croatian'
'cz': 'Czech'
'da': 'Danish'
'nl': 'Dutch'
'en': 'English'
'fi': 'Finnish'
'fr': 'French'
'gl': 'Galician'
'de': 'German'
'el': 'Greek'
'he': 'Hebrew'
'hi': 'Hindi'
'hu': 'Hungarian'
'is': 'Icelandic'
'id': 'Indonesian'
'it': 'Italian'
'ja': 'Japanese'
'kr': 'Korean'
'ku': 'Kurmanji (Kurdish)'
'la': 'Latvian'
'lt': 'Lithuanian'
'mk': 'Macedonian'
'no': 'Norwegian'
'fa': 'Persian (Farsi)'
'pl': 'Polish'
'pt': 'Portuguese'
'pt_br': 'Português Brasil'
'ro': 'Romanian'
'ru': 'Russian'
'sr': 'Serbian'
'sk': 'Slovak'
'sl': 'Slovenian'
'sp': 'Spanish'
'es': 'Spanish'
'sv': 'Swedish'
'se': 'Swedish'
'th': 'Thai'
'tr': 'Turkish'
'ua': 'Ukrainian'
'uk': 'Ukrainian'
'vi': 'Vietnamese'
'zu': 'Zulu'

위 목록 구조는 key: value 입니다.

value는 해당 국가의 언어를 의미합니다.
key는 실제 해당 함수에 전달할 파라미터 값입니다.

예를 들어, 'kr' 키는 한국을 의미하며, 이 키를 사용하면 한국의 날씨를 조회할 수 있습니다.
ex)
1.
user_input: 오늘 서울의 날씨는 어때?
parameter: kr

2. 
user_input: 오늘 미국 뉴욕의 날씨는 어때?
parameter: us

3. 
user_input: 오늘 일본 도쿄의 날씨는 어때?
parameter: jp

위와 같이 사용자의 입력에 따라 적절한 파라미터를 전달해야 합니다.
'''.replace("'", "")




@mcp.tool(name="global_weather_tool")
def global_weather_tool(city: str = 'us') -> str:
    f'''
    {global_weather_tool_description}    
    '''
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric&lang=kr"

    try:
        response = requests.get(api_url).json()
        city_temperature = response['main']['temp']
        city_weather = response['weather'][0]['description']
        city_wind_speed = response['wind']['speed']
        city_name = response['name']
        sys_date = datetime.datetime.fromtimestamp(response['dt']).strftime('%H:%M')

        return f'''
        검색한 도시: {city_name}
        기준 시간: {sys_date}
        온도: {city_temperature}도 
        날씨: {city_weather} 
        풍속: {city_wind_speed}m/s 
        
        위 정보는 반드시 사용자에게 알려주고 위 정보를 바탕으로 복장을 함께 추천해주세요.'''

    except Exception as e:
        return "날씨 조회 실패"




if __name__ == "__main__":
    mcp.run(transport="sse")

    '''
    test code
    '''
    # client = Client(mcp)

    # async def call_tool(city: str):
    #     async with client:
    #         result = await client.call_tool("weather_tool", {"city": city})
    #         print(result)

    # asyncio.run(call_tool("Seoul"))




