import pytest
from unittest.mock import patch
from mcp_server.weather_mcp import global_weather_tool

sample_json = {
    "coord": {
        "lon": 126.9778,
        "lat": 37.5683
    },
    "weather": [
        {
            "id": 800,
            "main": "Clear",
            "description": "맑음",
            "icon": "01d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 18.76,
        "feels_like": 17.94,
        "temp_min": 18.76,
        "temp_max": 18.76,
        "pressure": 1009,
        "humidity": 48,
        "sea_level": 1009,
        "grnd_level": 999
    },
    "visibility": 10000,
    "wind": {
        "speed": 3.6,
        "deg": 250
    },
    "clouds": {
        "all": 0
    },
    "dt": 1745810331,
    "sys": {
        "type": 1,
        "id": 8105,
        "country": "KR",
        "sunrise": 1745786431,
        "sunset": 1745835507
    },
    "timezone": 32400,
    "id": 1835848,
    "name": "Seoul",
    "cod": 200
}

@patch("requests.get")
def test_global_weather_tool(mock_get):
    class MockResponse:
        def json(self):
            return sample_json

    mock_get.return_value = MockResponse()
    assert global_weather_tool("Seoul") == "날씨 조회 실패"

    