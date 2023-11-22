# legacy-wznn-snapshot

The legacy wZNN token on BSC has been abandoned, leaving ~87k wZNN out of the circulating supply.

In order to solve this problem, we can:
- take a snapshot of the holder count at a certain height
- distribute equivalent, valid ZNN to these holders

--------------

The snapshot data was collected using the [ERC20-snapshot tool](https://github.com/gweidart/ERC20-snapshot).  
Snapshot parameters are included here:
- [wZNN](./wZNN/snapshot.config.json)
- [Cake LP](./Cake-LP/snapshot.config.json)

Additional context is available [here](./notes.txt).

Clean snapshots without empty balances:
- [wZNN](./wZNN_data.json)
- [Cake LP](./Cake-LP_data.json)
