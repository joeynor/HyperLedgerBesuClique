
## How to

### Note: make sure you have docker, and docker-compose setup

1. run the following commands
 
```bash
git clone --recurse-submodules -j8 https://github.com/abuyusif01/clique

# --init == install python dependencies, therefore run this only once
# --network == determine weither to enable explorer or not
# --action == what todo, either start or stop
# --port == which port to run chainlens (default 9600)
cd clique && bash runner --action start --port 80 --init true --network false
```

2. Wait for atleast 5-10mins for all services to be up, then neviagate to <http://localhost> to view explorer `(if --network true)` is suplied. 