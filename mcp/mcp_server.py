from mcp.server.fastmcp import FastMCP
import datetime
from langsmth_tracer import tracer

tracer()

mcp = FastMCP("MCP_Server")

@mcp.tool()
async def get_current_time():
    """Returns the current system time."""
    return f"The current time is {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

@mcp.tool()
async def message_sentiment_analysis(message: str):
    """Analyzes the sentiment of a message and returns whether it is positive, negative, or neutral."""
    if "good" in message.lower():
        return f"The sentiment of the message '{message}' is positive."
    elif "bad" in message.lower():
        return f"The sentiment of the message '{message}' is negative."
    else:
        return f"The sentiment of the message '{message}' is neutral."
    
@mcp.tool()
async def calculate_years_since(year: int):
    """Calculates the number of years since the given year."""
    diff = datetime.datetime.now().year - year
    return f"It has been {diff} years since {year}."

if __name__ == "__main__":
    mcp.run(transport="stdio")
    

