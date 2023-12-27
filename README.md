
## How to

### Requirements
1. Docker
2. Docker-compose
3. hyperledger/besu (make sure besu executable is in your path)

#### How to you

1. run the following commands
 
```bash
git clone --recurse-submodules -j8 https://github.com/abuyusif01/clique clique
cd clique
git checkout v2


# --init == install python dependencies, and generate besu keypairs. therefore run this only once
# --explorer == determine weither to enable explorer or not
# --action == what todo, either start or stop
# --port == which port to run chainlens (default 9600)
bash runner --action start --port 80 --init true --explorer true
```

2. Wait for atleast 5-10mins for all services to be up, then neviagate to <http://localhost> to view explorer `(if --explorer true)` is suplied. 


## Cloud Deployment

1. Open port 8545 for RPC
2. Open port 80 for web-explorer