## AWS Lambda

## History

In the early 2000s, there was a tradition of data centers where companies used to install hardware on their data centers which was an expensive idea, with network-related threats and it all comes with high maintenance costs.


In the last 2000s, when cloud computing came in buzz, AWS EC2 was launched, which was a revolutionary idea at that time. With this, Amazon enabled us to build our cloud-based data centers with virtual servers and pay as per the choice of hardware and usage concepts. We can control storage, security, and many more things over the stuff or facilities provided by AWS.

In the summer of 2014, AWS enhanced cloud infrastructure and launched the revolutionary AWS lambda. Like EC2, it is also a computing service with the concept of pay-per-use. We get all the benefits of EC2, from load balancing to integration and it is a lot easier. Also, for low traffic, we don't get charged but for high traffic, we may charge per invoke.


![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/e9ddfd68-e63a-4313-ae3a-3041b16af2cd)

------

## What is AWS lambda?

Run code on scale, without the worry about the servers and maintaining them. In this compute service, we write a function that is a primary unit of the lambda. These functions can be from 10 lines to 1000 lines. 

 These are useful in event processing, timer-based jobs, and API hosting

----

## Lambda Workflow
+ Create a function (through CLI, console, and CDK)
+ Upload your code(in Python, Go, TS, etc)
+ Deploy and invoke the function.
+ The invoke work can be done in many ways like API gateway, SNS, event triggers like S3 upload, and even a lambda can invoke another lambda.

------
## Why it is useful?

+ No server to maintain and manage.
+ Patching and security concerns are taken care of by AWS.
+ Auto-scaling.
+ It is a pay-for-use service, hence is no overhead charge for maintenance.
+ Very fast and scalable.
+ We can increase provision memory to improve its performance.
+ It can integrate with almost every service of AWS like DynamoDB, SNS, etc.

----------------
![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/ad16878a-692b-4191-961e-08d0ee2f2f44)

------

## Key use cases
+ API Gateway Integration

To expose the functionality of the lambda function, we can integrate it with the API gateway. It is a service of AWS which allows us to build HTTP and REST endpoints. It provides a URL to invoke a lambda function and it returns a response. 

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/c0021bfa-3007-49d2-a891-13778b60c846)

+ Serverless CRON Jobs

CRON jobs allow us to invoke a block of code at a certain time. At first, we need to set up a server and configure the cron job in the project settings. In AWS, we can use Cloudwatch, using which we can make time-based events. We can even control the content provided, it may be static or dynamic. We can use it to implement features like updating a dashboard and writing dynamic emails after a certain period.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/811470e7-9389-4cba-a728-1d601c021aad)

+ Event processing with SNS and SQS

Using SNS, we get notified when an event occurs, and based on that, we can perform some action. In the case of SNS, it is a pub-sub service. We have a publisher and a subscriber, here lambda is the subscriber to a SNS service. So whenever a publisher publishes a message, all the subscribers to that topic will be invoked, which is lambda here. In this way, we implement asynchronous invocation. 

Now SQS stands for Simple Queue Service. In this case, there is a one-to-one relationship, where an SQS queues a lambda function for its invocation. A message queued messages in the queue at the SQS periodically and invoke periodically as well.


![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/790c69e9-a70f-4a30-b1e6-06b61c61d664)

But the much more common pattern followed here is we publish a message on SNS and it delivers to the SQS, where the messages get queued and pulled by the lambda periodically.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/d653de7e-1690-475b-b029-21fa247ba45d)

+ File upload processing on S3

For the time being, say we want to do some processing on the data provided, like a face detection and recognition functionality on an image. We can add lambda as a trigger to that S3 bucket. So whenever a new picture is uploaded to the S3, it invokes the lambda function, pulls the latest upload, does the required processing, and responds to the result. The result of the lambda can be used to publish a new message, add to DynamoDB, or invoke another lambda based upon it, we can do as per required.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/70a47142-bb42-4226-b8b8-c840060b8aa3)

+ Glue Logic for Step Function Workflow

Based on the result provided by the Lambda function, we can proceed further. A visual example is explained in the picture below

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/5fb5cdef-1ee3-4d33-a298-cca0f510eac1)


--------

## How a lambda function looks like?
To create a lambda function, just go to the lambda console, and click Create a new function. Name your function and chose the runtime. Let other fields default as of now.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/0a568f1f-694a-4487-9fc5-390f8cb48cd0)

Here, I am implementing a basic lambda function in Python. A basic lambda function looks like
```python
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': JSON.dumps(event)
    }
```
+ Terminologies
  + In every lambda function, the `lambda_handler` function is the entry point. We can add different functions as well, but while invocation this function will execute first.
  + Now what is this `event` and `context`🤔 that is the function accepting as the arguments? Do we also need to pass it as a parameter while invocation?
    
    ![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/059793e6-d9f7-4842-8447-f34e72344e4d)

  + Event - The event simply contains the information about the resources or services using which we invoked the lambda. For example, if the lambda were triggered from an HTTP api call via API Gateway, then the event object would look something like
    ```python
    {
    "resource": "/",
    "path": "/",
    "httpMethod": "GET",
    "requestContext": {
        "resourcePath": "/",
        "httpMethod": "GET",
        "path": "/Prod/",
        ...
    },
    "headers": {
        "accept": "text/html",
        "accept-encoding": "gzip, deflate, br",
        "Host": "xxx.us-east-2.amazonaws.com",
        "User-Agent": "Mozilla/5.0",
        ...
    },
    "multiValueHeaders": {
        "accept": [
            "text/html"
        ],
        "accept-encoding": [
            "gzip, deflate, br"
        ],
        ...
    },
    "queryStringParameters": {
        "postcode": 12345
        },
    "multiValueQueryStringParameters": null,
    "pathParameters": null,
    "stageVariables": null,
    "body": null,
    "isBase64Encoded": false
    }
    ```
  + As we can see here that it contains all the information about the HTTP request, from the path, HTTP method, request, etc along with some default lambda details
  + What about `Context`?
  + It contains information about the lambda function, unlike event which changes depending upon the trigger.
      
    ![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/50bc8673-dd0b-4df3-9006-a6f81a8df63f)

  + We can return the desired value from the lambda, as per the requirements. But must be in JSON format looks like `json.dumps(data_to_return)`.

-----------------
