# NewtonGPT

NewtonGPT is a project that aims to enable the Apple Newton MessagePad 2000 to connect to ChatGPT over Wi-Fi, providing users with an interactive and useful AI assistant on their Newton devices.

## Overview

The main script in this project is `newtonGPT.py`, which sets up a telnet interface for the Newton MessagePad 2000 to communicate with ChatGPT via a Wi-Fi connection. This script is based on asyncio, enabling efficient and concurrent handling of multiple connections.

Another script, `chatgpt_asyncio_telnet_cli.py`, is under development and will be designed to work with the ChatGPT CLI tool.

Additionally, the `PT100_serial.py` script is a utility that generates serial numbers for the PT100 program on the Newton MessagePad 2000.

## newtonGPT.py

This script runs an asyncio-based telnet server that listens for incoming connections from the Newton MessagePad 2000. When connected, the script processes user messages, sends them to the ChatGPT API, and returns ChatGPT's responses to the Newton device over the telnet connection.

## chatgpt_asyncio_telnet_cli.py (in progress)

This script, currently under development, will provide an alternative way to interact with ChatGPT using the ChatGPT CLI tool.

## PT100_serial.py

This utility script generates serial numbers for the PT100 program on the Newton MessagePad 2000.

## Getting Started

To run the `newtonGPT.py` script, make sure you have Python 3.7 or later installed, and the required packages (aiohttp, asyncio, and openai) are installed. Set your OpenAI API key as an environment variable or replace the placeholder in the script with your API key. Then simply run the script:

```bash
python newtonGPT.py
```

This will start the telnet server, and you can connect your Newton MessagePad 2000 over Wi-Fi to interact with ChatGPT.