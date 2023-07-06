# SNS - Simple Notification Service

It is a `PubSub` concept-based messaging and processing service. Pub stands for publisher and Sub stands for subscriber, also called consumer.

The SNS is responsible for sending a message at an event. So whenever a message is sent to the publisher, an identical clone of the same message is sent to their subscribers. This is a one-to-many relationship.

The limit is 10m consumers, so a publisher can publish messages to millions of consumers. These consumers can be SQS, Email, HTTP points, text messages, or even push notifications.

It is highly durable for automatic scaling. Fully managed in the sense means that AWS takes care of a lot of things, we just need to guarantee the integration and configuration. We even do not need to worry about hardware provisioning.

The Topics(pub) and Subscription(Sub) are two main concepts.

We can configure SNS for an application-to-person perspective where we publish emails or texts to the customers.  Moreover, we can also do the same for an application-to-application idea, where useful asynchronous message communication between large scalable systems.

# Application to Person
Say I am an owner of a large e-commerce company, and I want to notify my known customers about the sales which will start next week. We can implement this functionality in our application using SNS. Regarding the implementation, we pass a payload to the SNS topic and it processes the message and publishes it to the different phone numbers in the form of text messages and an email in case of email is provided.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/96579221-b3f0-40cb-b098-827cf963e3b4)

In this one-to-many relationship, what if we want to have one customer? Here we can use SNS messaging to publish or send the message to only one person or customer.

# Application to application

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/d323189a-431c-42c6-89cb-cc7b1d5b338e)

In a scaled system, one has different services like fraud detection service, analytical services, etc. In the same way, an organization set up a specific service for messaging, say Customer Order Service for a moment, this service will publish a message to Customer Order Topic (needs to be configured for a PubSub task). This published message can contain different contents, hence depending upon the type of message we can integrate it with different services. 

We can pass it to the AWS Lambda for some processing and task, a node or flask webserver for some analysis and processing or we can send it to the SQS, where all the messages will be queued and a resource like AWS lambda integrated with it can consume if periodically.


# Why needs a topic?

For example, the Customer Order Service mentioned in the above example, needs to know what device we are delivering or publishing the message to. Is it a node server, is it AWS Lambda, or SQS?  This issue is termed type-coupling, integrating a topic solves this problem because there we define and configure the type of service consuming the message published.

Another issue one faces by not integrating an SNS topic is scaling.

# SNS Console/Dashboard

The dashboard section of AWS SNS is pretty interesting, where a brief insight about the service is given along with the navigation section on the left side, where one can navigate to
+ `Dashboard` - where all your created resources regarding SNS are listed
+ `Topics` - This page contains all the information about the topics created
+ `Subscription` - All the subscriptions created are listed here along with the topics they belong to.
+ `Mobile` - The section for mobile is listed separately because it is believed that it is comparatively difficult to set up the push notification and SMS.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/b6336a8b-33ae-440f-a0a9-cbb24574ba1b)

# Create Topic and Subscription

+ Go to the topic dashboard and create a topic, give the topic a name and an alias optionally.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/d1a84eff-8e82-4094-b560-abb84493fdfa)

+ Other fields are
  + `Encryption` - If the message you are publishing is highly classified, you can encrypt it so that even in case of data leaks, it won't cause potential harm. Else keep disabling it for now
  + `Access Policy` - It controls the permission of who can access the topic, by default it is the user. We can choose who can create a topic and who can publish that topic. It is highly suggested to not allow everyone in the permission because in that case anyone who knows the `arn` can use it to manipulate the topic you created. Optionally you can keep it to default or can allow specific accounts by providing the accounts id
    
  ![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/139cc911-9576-4631-968f-59d4f6bdd7fc)
  
  + `SNS Delivery Retry Policy` - In this section, we can define how an SNS will retry the execution if it fails to deliver the required message.
    + We can define the number of retries, the maximum we can choose is 100, but not recommended. 3-5 is a healthy number
    + Next we can choose no delay retires, by default, it is `0`. Which means if there's any delay then it what time it must retry the next attempt within the range of the number of retries?
    + `MinimumDelay` and `MaximumDelayRetries` when a message fails there is something pre-backoff phase, backoff phase, and post-backoff phase. It is an advanced topic in itself and will try to cover it separately.
    + Try to keep them in range `0` to `20`.
    + On the very top it means that on failing a message, the maximum delay we can afford for a retry of a message must be in this defined range.
    + `backoffFunction` - It can be linear, exponential, arithmetic, etc. Exponential is advised, because using this we can define the wait on failure. For example, on choosing exponential at first it will take 2 seconds, then 4 at the next attempt, and then 16 at the next attempt.
    
  ![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/0f96aae8-dcb8-45fd-9390-526d550800be)

  + `Status Logging` - This is configured of logging the message to CloudWatch logs. We can choose the following resources where I want to log our messages in. The success sample rate is defined by what percentage of you want messages to be logged. It can be costly as logging on CloudWatch can be costly, it is fine to go for it but a constant monitor is advised. 
    
    ![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/a5c07757-32cf-465a-8e78-2a3e0bbd8b9a)

  + `Tags` - We can create tags as key-value pair to differentiate SNS topics and can monitor the cost.
  + On successful creation, the dashboard will look like

    ![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/e49204ec-3d69-4116-adf5-14efacccfeed)

+ Create a new subscription
  + To create a new subscription we can either go to the subscription console or can chose the topic and there's a `Create Subscription` field using which we can create a subscription respective to the specified topic. This will open a page with some values pre-filled as per to configure what topic this subscription belongs to.
  + On creating the Subscription, we need to define what protocol the subscription will follow, this will look as follows. Note that for every subscription, we need to make some configurations accordingly.
    
    ![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/36c73663-21cf-455a-bf1d-0ec6581efff5)

  + `Subscription filter policy` - This is used to define the delicacy of the user we want to publish the message to, say we have 3 people the organization has 2 variants of the message, message A and message B. So what if person 1 and 3 wants to receive group A message and person 2 wants to receive group B messages? This can either be done by some programming login in the consumer, or we can define it here in the Subscription Policy. This looks like

    ![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/20f6353b-0865-4a38-ac08-b9c859631b44)

    Where `anyMandatoryKey` is the defined category, and `"any", "of", and "these"` are here the groups, like group A and B messages.
    
  + `Reddrive Policy - DLQ(dead letter queue)` - In some cases the message not be delivered if the person is offline, then SNS looks at the retry policy and makes a retry. But even after exceeding the maximum number of retries, it retries the entire process again after a certain time limit, says `48 hours`.
  + The failed message here is known as `Dead letters`. The failed message is stored in DLQ, where we can set an alarm to re-publish the messages for the people who didn't receive the emails.

# Publish a message

There are many ways to publish a message, we can use the console to publish the message simply or we can do it programmatically using `arn`, which is unique for every topic.

Through the console, select the topic and click `Publish Message` at the right top. This will ask a few questions

+ `Topic ARN` - It is simply the unique ARN of the topic where we want to publish the message
+ `Subject` - A title to the message, just like we write subjects in emails.
+ `TTL` - Time to leave, applicable to mobile notification service only. When we send push notifications that remain actual for a very limited time - 1 or 2 days. How can we ensure that the devices that were offline during this period will not receive an outdated push? TTL helps us make sure of that.
+ `Message Body`

  This is interesting, we can either select a general body as a payload to publish to all kinds of resources which are added as a subscription

 ![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/4795bc7c-5d01-4b9c-b0db-7081853df627)

  Or, we can define separate messages depending upon what type of subscription the message is publishing to.
  
  ![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/1cd16404-b132-4145-94e2-fdd8b70c72d8)

+ `Message Attributes - In the message attributes section, we can define the key-value pair, which will only be sent over the message. For example, we are only publishing those messages whose payload data-id of type `www`
![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/b70c6dfb-00fe-4696-9770-72a0dc4dfdf6)



# Mobile Push Notification

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/69fdea97-f96d-4635-a0f0-d3c8bea26e1a)

[ Updating this section soon ..... ]
  


 
