#!/bin/bash

echo [+] Installing proto
choco install protoc

echo [+] Installing deps
pip install -r googleplay-api/requirements.txt

echo [+] Updating protobuf
pip install --upgrade protobuf
