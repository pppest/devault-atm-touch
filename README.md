# A touchscreen ATM for DeVault

**tl;dr**
kivy framework based touchscreen DeVault crypto ATM for the raspberry pi with a
coin acceptor.

**KNOWN PROBLEMS: it cannot give back coins and it doesnt check it coins inserted exceed atm balance**



This is the first version of the kivy based DVT ATM, but I have plans to extend its functionality and to make different versions.
I made this little video check it out:    
![A DeVault ATM youtube](https://github.com/pppest/devault-atm-touch/blob/master/images/atm-vid-fast.gif)   

You can see it on youtube with its original soundtrack by Tropigotikas:   
https://www.youtube.com/watch?v=8jyNdE-9dDU&feature=youtu.be

A pic:   
![DeVault ATM](https://github.com/pppest/devault-atm-touch/blob/master/images/devault-atm-touch-pinnata.jpg)   
<!-- ![transactiongif](https://github.com/pppest/devault-atm-touch/blob/master/images/atm.gif)   
![transactiongif](https://github.com/pppest/devault-atm-touch/blob/master/images/transaction.gif)    -->

Big shout-out to @21isenough , the Python and Kivy community for sharing so much great information!!!  
And to the DeVault devs @jonspock and @proteanx for helping me learn.  
:beers:

If you have any questions then come find me in the DeVault [discord](https://discordapp.com/invite/JnRZ7BB) or [forum](https://devaultchat.cc/) or on [twitter](https://twitter.com/pestdesmadre).

**How to use**  
To use my code just clone/download it, install the requirements and run start_atm.sh. (maybe chmod +x it)   
The app checks for the DeLight client and downloads if not found then starts the atm.


Take a look at [@21isenough](https://github.com/21isenough/LightningATM)s or [@talenpierre](https://github.com/talentpierre/KivyLightningATM_Repo/tree/master/LightningATM_Kivy_Separate)s github if you need to learn how to build the actual thing. They have great documentation.


Note:  
I left the usb.py in case someone want to use it with a converter instead of gpios  



**About**  
I work for the DeVault community and saw @21isenough 's [LightningATM prototype](https://github.com/21isenough/LightningATM) on reddit, took a look at the code and got inspired  to learn python. Then I watched some youtube tutorials, I can recommend @CoreyMSchafer s [channel](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g),
on basic python and started. I didn't have a Raspberry Pi so I got a
usb converter and made a console based [first version](https://github.com/pppest/devault-atm).  


**Links**  
Website: http://www.devault.cc/  
Forum: https://devaultchat.cc/  
Github: https://github.com/devaultcrypto  
