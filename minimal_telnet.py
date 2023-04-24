# minimal_telnet.py
import asyncio
from telnetlib3 import TelnetServer

async def minimal_shell(reader, writer):
    writer.write('Welcome to Minimal Telnet Server\r\n'.encode('ascii', 'replace'))
    writer.write('Enter some text and press Enter\r\n'.encode('ascii', 'replace'))

    while True:
        message = await reader.readuntil(b'\n')
        writer.write(b'You typed: ')
        writer.write(message)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    server = loop.run_until_complete(loop.create_server(lambda: TelnetServer(minimal_shell), host='0.0.0.0', port=6801))
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    loop.run_forever()

