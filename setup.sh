#!/bin/bash
CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install llama-cpp-python
pip install --upgrade pip
pip install -r requirements.txt