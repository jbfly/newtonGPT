# telnet_chatgpt.py
import asyncio
import subprocess
import shlex
from telnetlib3 import TelnetServer, TelnetWriter

CHATGPT_COMMAND = 'chatgpt'

async def shell(reader, writer):
    welcome_message = 'Welcome to ChatGPT Telnet Server! Enter your message and press Enter to chat with ChatGPT.\r\n'
    writer.write(welcome_message.encode('ascii', 'replace'))

    while True:
        writer.write(b'> ')
        message = (await reader.readuntil(b'\n')).decode('ascii', 'replace').strip()
        if message.lower() in ('quit', 'exit'):
            writer.write(b'Goodbye!\r\n')
            await writer.drain()
            writer.close()
            break

        chatgpt_command = f'{CHATGPT_COMMAND} "{shlex.quote(message)}"'
        process = subprocess.run(chatgpt_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output = process.stdout.decode('utf-8')

        output_ascii = output.encode('ascii', 'replace')
        writer.write(output_ascii + b'\r\n')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    server = loop.run_until_complete(loop.create_server(lambda: TelnetServer(shell), host='0.0.0.0', port=6801))
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    loop.run_forever()

