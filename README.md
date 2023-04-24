# NewtonGPT

NewtonGPT is a project that allows users to interact with OpenAI's ChatGPT via a Telnet interface. It utilizes the Python `asyncio` library to handle concurrent connections and `aiohttp` for asynchronous API calls.

## Directory Structure

'''
newtonGPT
│
├── chatgpt_asyncio_telnet_api.py # Main script for ChatGPT Telnet server
├── chatgpt_asyncio_telnet_cli.py # Client script for connecting to the Telnet server
├── pt100_serial.py # Serial number generator for PT100
├── telnet_chatgpt.py # (Deprecated) Initial version of the Telnet server
│
└── testing # Directory containing test scripts
├── echo_telnet.py # Test script for echoing messages via Telnet
├── openai_test.py # Test script for basic interaction with OpenAI API
├── simple_hello_telnet.py # Simple Telnet server example
├── minimal_telnet.py # Minimalistic Telnet server example
└── simple_asyncio_hello_telnet.py # Asyncio-based Telnet server example
'''

## How It Works

1. The `chatgpt_asyncio_telnet_api.py` script is the main server application. It listens for incoming Telnet connections and establishes asynchronous communication with the connected clients. 

2. For each connected client, it maintains a conversation history with ChatGPT, allowing contextual responses.

3. The `chatgpt_asyncio_telnet_cli.py` script is a simple Telnet client that connects to the server, allowing users to send messages and receive replies from ChatGPT.

4. The `pt100_serial.py` script is a standalone serial number generator for PT100 devices. It is not directly related to the ChatGPT Telnet functionality but is included as a utility in the project.

## Usage

1. First, set up the required environment variables, such as the OpenAI API key:

```bash
export OPENAI_API_KEY=your_openai_api_key
''

2. Run the main server script in one terminal:

```bash
python chatgpt_asyncio_telnet_api.py
''

3. In another terminal, run the client script to connect to the server:

python chatgpt_asyncio_telnet_cli.py

4. You can now interact with ChatGPT via the Telnet interface by typing messages and pressing Enter.

##Note
The telnet_chatgpt.py script is a deprecated initial version of the Telnet server and is kept for reference purposes. The newer chatgpt_asyncio_telnet_api.py script should be used for the primary functionality.
