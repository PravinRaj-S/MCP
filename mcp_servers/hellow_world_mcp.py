from fastmcp import FastMCP

# Create MCP server instance
mcp = FastMCP("hello-server")

# Define a tool
@mcp.tool()
def say_hello(name: str) -> str:
    """Greets the user by name."""
    return f"Hello, {name}! 👋"

# Run the server (auto handles stdio for Claude)
if __name__ == "__main__":
    mcp.run()
