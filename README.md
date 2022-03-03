
# Shortest Path Multi-Source Multi-Destination

The proposed algorithm tries to find the shortest distance between a set of origins and destination for a single transporter given that there is proiority in delivering the packages. You can not go to a destination unless you have picked up the package from it origin.


edit: the code base is an algorithm proposed for a startup based on the idea of finding the optimal path for a delivery-sharing-based app in which a user would pick up and deliver packages along his/her route from A to B.

## Format

the data is in a dictionary in such way that every "key" in dictionary corrospands to an origin and every "value" is the destination.

Ex: {1:4, 2:5, 3:6}

```
- Origins
    - 1
    - 2
    - 3
- Destinations
    - 4
    - 5
    - 6
```

