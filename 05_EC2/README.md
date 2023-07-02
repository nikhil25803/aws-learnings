## EC2 - Elastic Compute Cloud

What is EC2?
To run an application, we need servers. So depending on the application, we might need hundreds of servers. So instead of physically installing hardware, AWS provides secure virtual servers, resizable compute capacity, and other perks from the cloud.

To use one, we need to create an EC2 instance, we can choose OS and their quantity of choice or can even automate using SDK and programming language of our own choice.


![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/0392e0e3-67ab-464d-98af-3a7201f421df)

-----
## Why EC2 is used?

+ We can scale our instance.
+ Pay as per the use
+ Choose the OS of choice.
+ Secured by VPC
 and more ...

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/46342348-78dd-4e79-9d73-02e0c9e7b110)

----
## Hands-on 
+ Go to the AWS management console
+ Click or chose EC2
+ Click on Launch instance
+ Give a name to the instance and select the virtual OS image.
+ Generate key-value pair
  
![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/802f8ef7-6c30-41b8-88ac-dd10f78619c1)


![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/52760053-0824-4ec1-a4e0-ace92178d800)

+ Select the instance running from the dashboard.
+ The dashboard looks like

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/0a66336e-89d2-4891-ab18-950ee10df6b3)


------------------
## AMI - Amazon Machine Image

An Amazon Machine Image (AMI) is used to create virtual servers (Amazon Elastic Compute Cloud or EC2 instances) in the Amazon Web Services (AWS) environment. Different types of instances can be launched from a single AMI to support the hardware of the host computer used for the instance.

It is a template of the EC2 instance we are about to launch.
![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/92e6fe8a-5d05-49df-abd1-14b22218f871)

In short. we can create an image of the instance we launched and can use it in the same or different regions

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/236e1ffd-178c-4c26-ac8a-5488734687f9)

------------

## EBS - Elastic Block Storage
+ EBS Volume can be used as a phycial hardrive. It can be attached to an instance and can be a dynamic increase-size of I/O operation
+ EBS Snapshot - Used to backup data on every snapshot of the instance, these are incremental backups
+ Lifecycle - It is used to automate EBS Volume and snapshot. It offers fast snapshot restore functionality.

------
## Network and Security
+ EC2 does have multiple IP addresses which can be used to most multiple websites on a single server, operate the network and redirect internal traffic,
+ It also does have Elastic IP addresses which is a static IPv4  address assigned for dynamic cloud computing. It is allocated to an AWS account.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/f7f00ef7-9cb6-4af3-be49-0dea6b7b6312)

+ We can create an Elastic IP address from the console in the `Network and Security section of EC2

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/9879accd-fbe3-497e-b1b0-fc5a50873e15)

------------------------
## Security Groups
Security groups, act as a firewall that controls the incoming(incoming) and outgoing traffic(outbound). We can define security groups or AWS will apply the default security on the instance.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/0fb9b539-122a-4104-a842-8fc3180a02ca)

----------
## Key Pairs
Key pairs are a set of security credentials used to prove identity while connecting to an EC2 instance. It provides a public key and a private key. EC2 stores the public key on the instance and we store their private keys to securely SSH to the instances.
![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/620b6f5a-0bf8-4362-b07e-2ba0cb04ac35)

--------

## Use Cases
![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/9059d4ca-d80a-4a3b-8b7c-2baf1d0fc7ec)

-------

## Provisions
![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/3d52ab3f-0481-4d75-a5eb-9521dd3abc54)

-------------

## Amazon Load Balancing
It automatically distributes the incoming traffic to multiple targets like instances, containers, and IP addresses depending upon the availability zones.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/85ddda65-ecd0-4068-b86c-ec310439eb46)


---------------------


