#!/bin/bash

echo [+] Installing proto
# Installation from https://grpc.io/docs/protoc-installation/
PB_REL="https://github.com/protocolbuffers/protobuf/releases"
curl -LO $PB_REL/download/v3.15.8/protoc-3.15.8-linux-x86_64.zip
unzip protoc-3.15.8-linux-x86_64.zip -d $HOME/.local
export PATH="$PATH:$HOME/.local/bin"
rm protoc-3.15.8-linux-x86_64.zip

echo [+] Installing protobuf
pip install protobuf

ls googleplay-api


echo [+] Installing deps
pip install -r googleplay-api/requirements.txt
