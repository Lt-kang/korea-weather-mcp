from dotenv import load_dotenv
import os
from fastmcp import FastMCP 
import datetime
from pathlib import Path

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

korea_city_list = open(Path(__file__).parent / 'korea_city.txt', 'r', encoding='utf-8').read().splitlines()

'''
openweathermap에서 제공하는 도시 리스트
https://bulk.openweathermap.org/sample/city.list.json.gz
'''
@mcp.tool()
def kor_weather_tool(city: str = 'Seoul') -> str:
    f'''
    도시의 날씨를 조회하는 도구 입니다.
    이때 city parameter로 입력 가능한 도시 list는 아래와 같습니다.

    {'\n'.join(korea_city_list)}

    만약 "OO구" 이런 입력이 들어온다면 이는 서울 시내의 구를 의미합니다.
    '''
    print(city)
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric&lang=kr"

    try:
        response = requests.get(api_url)
        print(response.status_code)
        response = response.json()

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
    # mcp.run(transport="sse")
    mcp.run(transport="sse")
    '''
    stdio로 실행을 원한다면
    transfport 파라미터를 삭제하거나 (default가 stdio)
    mcp.run(transport="stdio")
    으로 입력하면 됩니다.
    '''

    '''
    test code
    '''
    # from fastmcp import Client

    # client = Client(mcp)

    # async def call_tool(city: str):
    #     async with client:
    #         result = await client.call_tool("weather_tool", {"city": city})
    #         print(result)

    # asyncio.run(call_tool("Seoul"))




