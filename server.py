from mcp.server.fastmcp import FastMCP

#Create an MCP Server
mcp = FastMCP("Weathe Service")

@mcp.tool()
def get_weather(location: str) -> str:
    """Get The current weather for a specified location"""
    return f"Weather in {location}: Sunny, 72F"

@mcp.resource("weather://{location}")
def weather_resourcee(location: str) -> str:
    """Provide weathe data as a resource"""
    return f"Weather data for {location}: Sunny, 72F"

@mcp.prompt()
def weather_report(location: str) -> str:
    """Create a Weather Report Prompt"""
    return f"you are a weather reporter. Weather report for {location}?"


#Run the server

if __name__=="__main__":
    mcp.run(transport="sse",port=3001)
    