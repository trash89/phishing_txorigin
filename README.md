Study case of phishing with tx origin hack, from Solidity by example site [Solidity by Example, phishing with tx origin](https://solidity-by-example.org/hacks/phishing-with-tx-origin/)

I use brownie to compile and deploy into hardhat in order to have the console.log feature.
You should start the hardhat node in another terminal and folder (`hh node`), then, in a terminal :

```
brownie compile
brownie run scripts/deploy.py
```

After deploying from brownie :
![Deployment from brownie](phishing_txorigin_deploy.png)

The result in the hardhat console :

![Hardhat console ](phishing_txorigin_console.png)

So, don't rely on tx.origin to check the sender of transaction, use msg.sender instead.
