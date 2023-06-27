## AWS CLI - Accessing AWS and Services through Command Line Interface

+ To access the CLI, the user be it Admin or IAM user, must have the access key and secret key to configure the CLI. this can be done by routing to the `Security Credentials` section and generating an access key.
  
![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/d0cdd6bf-c887-4356-a61b-1f2dd2c6749d)

+ You can download and set up the CLI through the documentation given. [Link](https://aws.amazon.com/cli/)
+ You can check the installation by running the following command in the terminal
```bash
aws --version
```

+ Now you have to configure the CLI with the credentials. This can be done by following the below steps
+ Step 1
```bash
aws configure
```

+ Step 2 - Add the credentials as asked

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/1996d090-561e-469c-a6ea-ccaa03a6c9eb)

+ On successfully adding the credentials, your CLI has been configured now and you can use AWS resources(allowed one) from the CLI 😎

## CLI hands-on
+ Run `aws help and you will get a never-ending list of the AWS services or function you can access from the CLI

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/432a9f53-37fa-40d2-afae-1e810a85863f)

+ To get more specific help, say you want to see the resources available for the **EC2**, you can run `aws ec2 help`
  
![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/20b04802-bd35-4065-bf1b-f1e67d120b6c)
