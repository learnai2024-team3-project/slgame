#!/bin/bash

# 檢查 gdown 是否已安裝
if ! pip show gdown > /dev/null 2>&1; then
    echo "gdown is not installed. Installing gdown..."
    pip install gdown
else
    echo "gdown is already installed."
fi


gdown 'https://docs.google.com/uc?id=10A6zKDeXzp65F4-oi4ZAD4bG9VxAojJy' -O ~/slgame/models/best.pt


