#!/bin/bash

if [[ -d DeLight ]]
then
    echo "Delight exists on your filesystem."

else
 wget https://github.com/devaultcrypto/DeLight/releases/download/v4.0.12/DeLight-4.0.12.tar.gz
 echo 'sdsd'
 tar -xvf DeLight-4.0.12.tar.gz
 mv DeLight-4.0.12 DeLight
fi
