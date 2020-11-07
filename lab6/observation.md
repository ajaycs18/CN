# Configure RIP Routing Protocol in Routers

## Observations/Learnings
- Created a topology as shown using 3 routers and 2 pcs
- Connected the routers using _serial ports_ through _DCE_ cables 
- Configured router ip addresses using `ip address <address> <subnet_mask>`
- `encapsulation ppp` and `clock rate 64000` used to specify ppp protocol and clock rate in routers 0 and 1 for the serial ports
- Configured RIP routing using `router rip` then `network <address>` commands

## Topology
![topology](Topology.png)

## Router 0 Config (_10.0.0.10_)
![router0config](router0config.png)
![router0iproute](router0iproute.png)

## Router 1 Config
![router1config1](router1config1.png)
![router1config2](router1config2.png)

## Router 2 Config (_40.0.0.10_)
![router2config](router2config.png)
![router2iproute](router2iproute.png)

## PC0-PC1 Ping (_10.0.0.1_ -> _40.0.0.1_)
![pc0pc1ping](pc0pc1ping.png)
