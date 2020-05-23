#!/bin/bash

if [[ -d DeLight ]]
then
    echo "Delight exists on your filesystem."

else
 VERSION=$(curl -s "https://github.com/devaultcrypto/DeLight/releases/latest" | grep -o 'tag/[v.0-9]*' | awk -F/ '{print $2}')
 VERSION="${VERSION:1}"
 wget https://github.com/devaultcrypto/DeLight/releases/download/v$VERSION/DeLight-$VERSION.tar.gz
 tar -xvf ./DeLight-$VERSION.tar.gz
 mv ./DeLight-$VERSION DeLight
 rm DeLight-4.0.12.tar.gz
fi


python3 app.py
