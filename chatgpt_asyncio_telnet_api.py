# chatgpt_asyncio_telnet.py
import asyncio
import openai
import os
import aiohttp

async def call_chatgpt_api(conversation_history):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}",
    }

    url = "https://api.openai.com/v1/chat/completions"

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": conversation_history,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            response_data = await response.json()

    chatgpt_reply = response_data['choices'][0]['message']['content']
    return chatgpt_reply

async def handle_connection(reader, writer):
    addr = writer.get_extra_info('peername')

    print(f'Connection from {addr}')

    writer.write(b'Hello, Newton! Type your message and press Enter to chat with ChatGPT.\r\n')

    # Initialize the conversation history
    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    while True:
        data = await reader.readuntil(b'\n')
        if not data:
            break

        message = data.decode('ascii', 'replace').strip()
        print(f'Received {message!r} from {addr}')

        # Add user message to conversation history
        conversation_history.append({"role": "user", "content": message})

        # Call the ChatGPT API and get the response
        chatgpt_reply = await call_chatgpt_api(conversation_history)
        print(f"ChatGPT Reply: {chatgpt_reply}")

        # Add ChatGPT's reply to the conversation history
        conversation_history.append({"role": "assistant", "content": chatgpt_reply})

        reply_lines = chatgpt_reply.split('\n')
        
        # Print "ChatGPT: " only once at the beginning of the message
        writer.write(b'ChatGPT: \n')
        
        for i, line in enumerate(reply_lines):
            if i != 0:  # Add a newline before every line except the first one
                writer.write(b'\r\n')
            writer.write(line.encode('ascii', 'replace'))

        # Add a newline after the response
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

