from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="python", # Executable
    args=["./stdio/example_server.py"], # Optional command line arguments
    env=None # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print(tools)
            
            # If you want use ps aux check the server process , remove comments from the following 2 lines:
            #import time
            #time.sleep(10)

            # Call a tool
            result = await session.call_tool("fetch", {"url": "https://example.com"})
            print(result)
            """
            Other example calls include:

            # The example server only supports prompt primitives:
            # List available prompts
            # prompts = await session.list_prompts()
            # print(prompts)

            # # Get a prompt
            # prompt = await session.get_prompt("example-prompt", arguments={"arg1": "value"})

            # print(prompt)

            # List available resources
            resources = await session.list_resources()

            # List available tools
            tools = await session.list_tools()

            # Read a resource
            resource = await session.read_resource("file://some/path")

            # Call a tool
            result = await session.call_tool("tool-name", arguments={"arg1": "value"})
            """

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())