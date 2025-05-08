from dotenv import load_dotenv
import os
from fastmcp import FastMCP, Client
import datetime


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



@mcp.tool(name="global_weather_tool")
def global_weather_tool(city: str = 'Seoul') -> str:
    f'''
    도시의 날씨를 조회하는 도구 입니다.
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
    stdio로 실행을 원한다면
    transfport 파라미터를 삭제하거나 (default가 stdio)
    mcp.run(transport="stdio")
    으로 입력하면 됩니다.
    '''

    '''
    test code
    '''
    # client = Client(mcp)

    # async def call_tool(city: str):
    #     async with client:
    #         result = await client.call_tool("weather_tool", {"city": city})
    #         print(result)

    # asyncio.run(call_tool("Seoul"))




