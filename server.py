from cloudlink import server
from cloudlink.server.protocols import clpv4
import asyncio

if __name__ == "__main__":
    # Initialize the server
    server = server()

    # Configure logging settings
    server.logging.basicConfig(
        level=server.logging.ERROR
    )

    # Load protocols
    clpv4 = clpv4(server)

    # Start the server
    server.run(ip="0.0.0.0", port=3000)
