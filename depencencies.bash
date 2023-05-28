#!/bin/bash

echo [+] Installing proto
choco install protoc

echo [+] Installing protobuf
pip install protobuf

echo [+] Installing deps
pip install -r googleplay-api/requirements.txt
