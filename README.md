# custom-data-llama

This is a demo of how you can use langchain with python-llama-cpp, upload your custom inputs in TXT or PDF
and query any model about the information from the input. I'm using this on CPU - it's slow but seems to work.

This is using gradio as a webUI, so once started you need to connect to port 8080 with a browser.

Things to remember:
- llama-cpp quite recently moved to GGUF model from GGML, so make sure you have the right model downloaded.
- installing needed libraries should be done via: ```pip install langchain llama-cpp-python pypdf gradio``` (please note some more may be needed)
- paths and parameters may be tweaked
