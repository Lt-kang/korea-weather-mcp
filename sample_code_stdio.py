from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

import asyncio
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()


os.environ["OPENWEATHER_API_KEY"] = os.getenv("OPENWEATHER_API_KEY")
model = ChatOpenAI(model="gpt-4o")

weather_server_script_path = str(Path(__file__).parent / "mcp_server" / "weather_mcp_stdio.py")

async def call_stdio_mcp():
    server_params = StdioServerParameters(
        command="python", # 실행할 명령
        args=[weather_server_script_path], # 인자(스크립트 경로)
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await load_mcp_tools(session)

            agent = create_react_agent(model, tools)

            '''
            국내
            '''
            user_input = "오늘 강남구 날씨 알려줘"
            inputs = {"messages": [("human", user_input)]}

            result = await agent.ainvoke(inputs)
            print("========================================")
            print(f"human: {user_input}")
            print(f"Ai: \n\n{result['messages'][-1].content}")
            print("========================================")

            '''
            중국국
            '''
            user_input = "오늘 베이징 날씨 알려줘"
            inputs = {"messages": [("human", user_input)]}

            result = await agent.ainvoke(inputs)
            print("========================================")
            print(f"human: {user_input}")
            print(f"Ai: \n\n{result['messages'][-1].content}")
            print("========================================")

            '''
            일본
            '''
            user_input = "오늘 도쿄 날씨 알려줘"
            inputs = {"messages": [("human", user_input)]}

            result = await agent.ainvoke(inputs)
            print("========================================")
            print(f"human: {user_input}")
            print(f"Ai: \n\n{result['messages'][-1].content}")
            print("========================================")

if __name__ == "__main__":
    asyncio.run(call_stdio_mcp())

