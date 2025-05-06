from dotenv import load_dotenv
import os
from fastmcp import FastMCP, Client


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


@mcp.tool(name="weather_tool")
def weather_tool(city: str = OPENWEATHER_CITY) -> str:
    '''
    도시명을 입력하면 (온도, 날씨) 정보를 반환합니다. 
    하지만 아무런 도시명을 말하지 않는다면 함수의 'city' 파라미터의 default 값을 사용합니다. 예: Seoul
    '''
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric&lang=kr"

    try:
        response = requests.get(api_url)
        city_temperature = response.json()['main']['temp']
        city_weather = response.json()['weather'][0]['description']
        city_wind_speed = response.json()['wind']['speed']

        return f'''검색한 도시: {city}, 온도: {city_temperature}도, 날씨: {city_weather}, 풍속: {city_wind_speed}m/s
        위 네가지 정보는 반드시 사용자에게 알려주고 위 정보를 바탕으로 복장을 함께 추천해주세요.'''

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


