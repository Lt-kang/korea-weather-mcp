# Korea Weather MCP (한국 날씨 MCP)

## 프로젝트 소개
이 프로젝트는 국내/해외 도시의 날씨 정보를 조회하여 알려주는 MCP(Model Context Provider) 서버를 제공합니다.   
OpenWeatherMap API를 활용하여 실시간 날씨 데이터를 가져와 사용자에게 제공합니다.

## 기능
- 도시 이름을 입력하면 해당 도시의 현재 온도, 날씨 상태, 풍속 정보 제공
- 날씨 정보를 바탕으로 적절한 복장 추천

## 설치 방법
```bash
# 저장소 복제
git clone https://github.com/Lt-kang/korea-weatehr-mcp.git
cd korea-weather-mcp

# 가상 환경 생성 및 활성화
python -m venv venv
venv\Scripts\activate  # Windows

# 필요한 패키지 설치
pip install -r requirements.txt
```

## 환경 설정
`.env` 파일을 프로젝트 루트 디렉토리에 생성하고 다음 정보를 입력합니다:

```
OPENAI_API_KEY=your_api_key_here

OPENWEATHER_API_KEY=your_api_key_here
OPENWEATHER_CITY=Seoul  # 기본 도시 설정
```

OpenAI API 키는 [여기](https://platform.openai.com/settings/profile/api-keys)에서 발급받을 수 있습니다.  
OpenWeatherMap API 키는 [여기](https://openweathermap.org/api)에서 발급받을 수 있습니다.

## 사용 방법
1. MCP 서버 실행:
```bash
python mcp_server/weather_mcp.py
```

2. Jupyter Notebook에서 `main.ipynb`를 실행하여 인터랙티브하게 날씨 정보를 조회할 수 있습니다.

## 주요 파일 설명
- `weather_mcp.py`: 날씨 정보를 제공하는 MCP 서버 구현
- `main.ipynb`: LangChain과 LangGraph를 활용한 날씨 정보 조회 예제 및 테스트
- `requirements.txt`: 필요한 패키지 목록

## 의존성
- FastMCP: MCP 서버 구현을 위한 라이브러리
- LangChain: LLM 애플리케이션 개발 프레임워크
- LangGraph: LLM 기반 워크플로우 구성을 위한 라이브러리
- OpenAI: GPT-4o 모델 사용을 위한 API 클라이언트
