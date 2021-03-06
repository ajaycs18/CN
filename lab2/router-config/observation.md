# Router

## Aim

To configure a router, connect end devices, and ping the network devices 

## Observations/Learning

- Creating a topology and connecting 2 PCs to it on 2 different ports
- Configuring a router's interfaces using `enable`(privileged mode), `configure terminal`, `interface (fa0/0, fa1/1)`, `ip address` commands. `no shutdown` to prevent the link from shutting down
- Configuring default gateways for the PCs and setting the same in the router interfaces using the CLI with the above commands
- Viewing PC ip configuration using `ipconfig` and pinging the gateway & other PC using `ping` command

## Images/Videos

### Connection

![Connection](connection.png)

### Router Config

![Router Config1](routerconfig1.png)
![Router Config2](routerconfig2.png)

### PC6 Config

![PC6 Config](pc6.png)

### PC6-Gateway Ping

![PC6-Gateway Ping](pc6ping.png)

### PC7 Config

![PC7 Config](pc7.png)

### PC7-Gateway Ping

![PC7-Gateway Ping](pc7ping.png)

### PC6-PC7 Ping

![PC6-PC7 Ping](pc6pc7ping.png)

### Ping GIF

![Ping](routerping.gif)
