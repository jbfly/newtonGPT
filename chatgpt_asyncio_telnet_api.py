# Import necessary libraries
import asyncio
import openai
import os
import aiohttp

# Define an asynchronous function to call the ChatGPT API with the conversation history
async def call_chatgpt_api(conversation_history):
    # Set the headers for the API request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}",
    }

    # Set the API URL
    url = "https://api.openai.com/v1/chat/completions"

    # Prepare the payload for the API request
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": conversation_history,
    }

    # Make an asynchronous POST request to the API
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            response_data = await response.json()

    # Extract the ChatGPT reply from the response data
    chatgpt_reply = response_data['choices'][0]['message']['content']
    return chatgpt_reply

# Define an asynchronous function to handle incoming Telnet connections
async def handle_connection(reader, writer):
    # Get the address of the connected client
    addr = writer.get_extra_info('peername')

    print(f'Connection from {addr}')

    # Send a welcome message to the connected client
    writer.write(b'Hello, Newton! Type your message and press Enter to chat with ChatGPT.\r\n')

    # Initialize the conversation history
    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    # Main loop to handle incoming messages from the client
    while True:
        # Read data from the client until a newline character is encountered
        data = await reader.readuntil(b'\n')
        if not data:
            break

        # Decode the received message and print it
        message = data.decode('ascii', 'replace').strip()
        print(f'Received {message!r} from {addr}')

        # Add the user message to the conversation history
        conversation_history.append({"role": "user", "content": message})

        # Call the ChatGPT API with the updated conversation history and get the response
        chatgpt_reply = await call_chatgpt_api(conversation_history)
        print(f"ChatGPT Reply: {chatgpt_reply}")

        # Add ChatGPT's reply to the conversation history
        conversation_history.append({"role": "assistant", "content": chatgpt_reply})

        # Split the reply into lines and send it to the client
        reply_lines = chatgpt_reply.split('\n')
        
        # Print "ChatGPT: " only once at the beginning of the message
        writer.write(b'ChatGPT: \n')
        
        for i, line in enumerate(reply_lines):
            if i != 0:  # Add a newline before every line except the first one
                writer.write(b'\r\n')
            writer.write(line.encode('ascii', 'replace'))

        # Add a newline after the response
        writer.write(b'\r\n')

    # Close the connection with the client
    print(f'Closing the connection with {addr}')
    writer.close()

# Define the main asynchronous function
async def main():
    # Start an asyncio server to handle incoming Telnet connections
    server = await asyncio.start_server(handle_connection, '0.0.0.0', 6801)

    # Get the server address and print it
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    # Run the server in the context of an asynchronous context manager
    async with server:
        await server.serve_forever()

# Run the main function when the script is executed
if __name__ == '__main__':
    asyncio.run(main())
