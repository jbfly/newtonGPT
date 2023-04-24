# simple_asyncio_hello_telnet.py
import asyncio

async def handle_connection(reader, writer):
    addr = writer.get_extra_info('peername')

    print(f'Connection from {addr}')

    writer.write(b'Hello, Newton!\r\n')

    while True:
        data = await reader.read(100)
        if not data:
            break

        print(f'Received {data!r} from {addr}')
        writer.write(b'Echo: ')
        writer.write(data)

    print(f'Closing the connection with {addr}')
    writer.close()

async def main():
    server = await asyncio.start_server(handle_connection, '0.0.0.0', 6801)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
