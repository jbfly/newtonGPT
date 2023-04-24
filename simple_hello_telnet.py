# simple_hello_telnet.py
import asyncio
from telnetlib3 import TelnetServer

async def hello_shell(reader, writer):
    writer.write('Hello, Newton!\r\n'.encode('ascii', 'replace'))
    writer.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    server = loop.run_until_complete(loop.create_server(lambda: TelnetServer(hello_shell), host='0.0.0.0', port=6801))
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    loop.run_forever()

