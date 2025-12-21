from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-mcp")

@mcp.tool()
def hello(name: str) -> str:
    """
    Say hello to a user
    """
    return f"Hello {name} from MCP server!"

if __name__ == "__main__":
    mcp.run(transport="stdio")