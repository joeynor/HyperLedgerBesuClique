
## Clique private permissioned network

### Requirements - Software
1. Docker, go to docker webpage and read the installation instructions, and post installation
2. Docker-compose, need to build image
3. python >= 3.10, also need to install pip3
4. hyperledger/besu (make sure besu executable is in your path)
5. need to install jdk

### Requirements - System
1. Enable ivp6 for docker
2. Os (Linux >= 6.0.0)
3. 16gb ram
4. 2vcpu (more is always better)

### Installation

1. Clone the repo and switch to v2 branch.

```bash
git clone --recurse-submodules -j8 https://github.com/joeynor/HyperLedgerBesuClique clique
cd clique
```
~~git checkout v2 # this is required to use clique with availability option~~

2. Generate new keys for initial signer, bootnodes and genesis node.

```bash
bash runner --init true
```

3. Allocate  `x` eth for `x` testing accounts.
```
bash runner --alloc 10 --balance 90000000000000000000000
```
4. Run the network

```bash
bash runner --action start --explorer true --port 80
```

5. Wait for atleast 5-10mins for all services to be up, then neviagate to <http://localhost> to view explorer `(if --explorer true)` is suplied. 


### Testing
there's a python script under `connect` that can perform the following tasks

1. view all accounts in the network
2. send transaction
3. account history



## Cloud Deployment

1. Open port 8545 for RPC
2. Open port 80 for web-explorer


## Maintenance

One can manage and maintain the network with the help of `docs/` folder. and a detailed explanation on how can be explored, located under `docs/`
