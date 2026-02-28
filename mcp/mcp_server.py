from mcp.server.fastmcp import FastMCP
import datetime
from langsmth_tracer import tracer

tracer()

mcp = FastMCP("MCP_Server")

@mcp.tool()
async def Fahrenheit_to_celsius(Fahrenheit:float):
    """Converts temperature given in Fahrenheit degrees to Celsius degrees"""
    celsius = (Fahrenheit - 32) * (5/9)
    return f"{Fahrenheit}°F is {celsius:.2f}°C"

@mcp.tool()
async def Celsius_to_fahrenheit(Celsius:float):
    """Converts temperature given in Celsius degrees to Fahrenheit degrees"""
    Fahrenheit = ((Celsius*9)/5) + 32
    return f"{Celsius}°C is {Fahrenheit:.2f}°F"

@mcp.tool()
async def message_sentiment_analysis(message: str):
    """Analyzes the sentiment of a message and returns whether it is positive, negative, or neutral."""
    positive_words = {"good", "love", "great", "awesome", "excellent", "fantastic", "happy", "wonderful"}
    negative_words = {"bad", "hate", "terrible", "awful", "horrible", "sad", "worst", "disgusting"}
    
    words = set(message.lower().split())
    if words & positive_words:
        return f"The sentiment of the message '{message}' is positive."
    elif words & negative_words:
        return f"The sentiment of the message '{message}' is negative."
    else:
        return f"The sentiment of the message '{message}' is neutral."
    
@mcp.tool()
async def calculate_years_since(year: int):
    """Calculates the number of years since the given year."""
    current_year = datetime.datetime.now().year
    if year > current_year:
        return f"{year} is a future year, not a past one."
    if year < 1:
        return f"{year} is not a valid year."
    diff = current_year - year
    return f"It has been {diff} years since {year}."

if __name__ == "__main__":
    mcp.run(transport="stdio")
    









