#!/bin/bash

if [[ -d ./DeLight ]]
then
    echo "/etc exists on your filesystem."

else
  wget https://github.com/devaultcrypto/DeLight/releases/download/v4.0.12/DeLight-4.0.12.tar.gz
fi

tar -xvf DeLight-4.0.12.tar.gz
mv DeLight-4.0.12 DeLight
