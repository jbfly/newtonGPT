# chatgpt_asyncio_telnet_cli.py
import asyncio
import subprocess

async def handle_connection(reader, writer):
    addr = writer.get_extra_info('peername')

    print(f'Connection from {addr}')

    writer.write(b'Hello, Newton! Type your message and press Enter to chat with ChatGPT.\r\n')

    while True:
        data = await reader.readuntil(b'\n')
        if not data:
            break

        message = data.decode('ascii', 'replace').strip()
        print(f'Received {message!r} from {addr}')

        # Call the existing CLI utility and get the response
        chatgpt_process = subprocess.run(['chatgpt', message], capture_output=True, text=True)
        chatgpt_reply = chatgpt_process.stdout.strip()
        print(f"ChatGPT Reply: {chatgpt_reply}")

        writer.write(b'ChatGPT: ')
        writer.write(chatgpt_reply.encode('ascii', 'replace'))
        writer.write(b'\r\n')

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

