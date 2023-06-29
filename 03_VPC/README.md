## VPC - Virtual Private Cloud

When an organization wants to use the AWS services but within their own private space, or network in short. This can be achieved using VPC. The VPCs are defined within the scope of an AWS region and can spread all over the availability zones.

## Subnets

VPCs network are very large, to maintain them, they are divided into *Subnets*. These subnets can be private as well as public subnets.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/f347414d-ae71-4855-8a56-18faad40b3b6)


![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/48c77cfd-ee7a-451d-988e-f0654cb9800c)


## Why VPC is required?
  
One of the main reasons VPC is in use is privacy and Security concerns. Being on a public network, an organization's data is at risk. This is where VPC comes in help. Using VPC, an organization can create its private network where it can define and access resources as per the requirements and use.

During the creation of an AWS account, a VPC network is already assigned. However, customization is point possible. This allows the explicit creation of Subnets, Security Groups, and Internet Gateways.

## Terminologies

### IP Address

Stands for Internet Protocol, an IP address is an address using which the Internet knows where to send digital data, pictures, or almost everything online. Just like someone needs our home address to reach us, a server needs an IP address to receive data over the Internet.

### IPv4 vs IPv6

+ IPv4
![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/d04643ab-1210-4140-8559-dad337049ffa)

IPv4 is a group of 4 numbers, ranging from 0-255, and each separated by ( . ). This unique address is used to let everyone around the globe send and receive data over the internet.

+ IPv6
+ 
Due to excessive growth in the internet boom, we almost ran out of unique IP addresses. For this, a newer version of IPv6 was in the queue to launch. It ensures we will never run out of IP addresses.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/c3279e21-fce1-4797-b54c-f5db5d663ddd)

### Subnets
A 32-bit IPv4 address is assigned to the network as well as the hosts. With this, there are 5 classes as well named from Class A to Class E

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/e3934e19-e8e2-43fd-bbba-2cea3d296c3a)


![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/f807ac98-ed06-498c-a77e-1f23ef63f79f)


![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/25574e8a-e339-4271-8f0a-c7d81ec4fcd6)

For example, on a train, there are 4 compartments, names from CA to CD, and each has a ca[capacity of 100 passengers, So while booking tickets, several bookings for each compartment are 100, 100, 150, and 20. Here we can see that the numbers of passengers in CC exceed the limits, whereas CD still has some seats left. 
So what one can do is to shift the extra 50 passengers in CC to CD and by this, we can utilize most of the resources available avoiding any overload.
In the same way, VPC helps and works, it allows us to utilize make robust use of the resources we have.



### Subnetting Mask
It is used to identify which class the IP address belongs to and take further actions.

### Inner Domain Routing
![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/f119ea68-0ce1-4a2c-814b-6bba2daa9913)

The `27` here is known as CIDR (Classless Inner Domain Routing) Notation. As we can see `202.201.150.10` belongs to class C, but after providing an inner routing of `/27` it now no more belongs to class C.


### Network ID
Network ID is the beginning of an IP address, which must match the mask in binary form. This ID will link the subnet to the large networks.

### Broadcast Address
To send data from a host network, a router uses a broadcast address. This address comes after all the addresses. It has a range of addresses using the subnet mask.
![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/9f191ac4-1230-4af4-b810-a9ed1ef0b012)

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/74ca243a-b20a-4ab9-a462-4907576eec1e)

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/c49a653b-6657-45b0-9744-1fc2e5847f37)


## Calculating the Possible number of Hosts and Subnets
![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/7982b20b-83b3-47d3-88db-ca663a462682)

In this picture, the possible number of hosts is 65. Hence after the mask, the `63` will be the broadcasting address. In summary
Host address - `205.150.65.62`
Broadcast address - `205.150.65.63`

## Components of VPC
+ Internet Gateway - This enables routing to the traffic in the public network.
+ DNS - It is just a name mapped over an IP address.
+ Elastic IP - These are the reserved IP addresses that one can use to assign any EC2 instances.
+ Endpoints - Used for horizontal scaling that allows communication between EC2 instances.
+ Network Interface - Point of connection between a public and private network.
+ Egress-only IP - It allows communication of EC2 over IPv6
+ Route Tables - Defines how traffic is routed between each subnet,
+ VPC Peering - It is a connection between VPC and instances.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/775e9e56-d6e3-4ccf-bc76-9e7574e032d4)

## Launch Instances into VPC
AWS computing services like EC2, are like virtual hardware to run applications and it takes care of the hardware. Any instances when launched must have a VPC, if not provided, AWS will choose one from the default 4096 addresses. Also, each instance is assigned a host DNS.


![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/9e8ab4d4-1f20-411a-9d6c-f32a8f348740)












