# SQS - Simple Queue Service

One of the first AWS services launched in 2006 along with S3 bucket and EC2. AWS SQS offers asynchronous message-based communication as an alternative to making API calls. It is scalable, highly available with more uptimes, fully managed in the background by AWS, and cost-effective as well. As a free tier, it offers around one million free requests.

# How is it useful?

+ Very viable for data processing
+ Real-time applications like analytics dashboard
+ Famous for job queueing
+ Can also be used as a timer-based service integrating it with Cloud Watch.

# Core Concepts
The core concept of SQS is queue, a First In First Out(FIFO) based structure as defined in computer science terms and real life as well. Similarly, here queue can be termed as an envelope of messages queued for some processing or consumed by any other AWS resource (lambda). These messages can be in text or JSON formats of a max size of 256KB per message entry.

A publisher like SNS ad messages to these queues, and consumers consume these messages periodically for further processing.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/6ff5b037-423b-4fab-809f-ee8dfea4f599)

# Why use SQS over API calls?

+ Backcrosses Control - Using SQS allows the consumer to choose the rate of processing
+ Fire and Forget - Publishers do not have to worry about the insights of the client processing. This simply decouples the dependencies of the publisher and the consumer. SQS works here as a middleman.
+ Event Guaranteed Processing - It is for async and non-Realtime applications.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/7d8f86aa-711d-490a-89b9-20c8115bee33)

# Standards vs FIFO Queues

In the standard queue, the order of the message published and consumed is not in the original order. Whereas in FIFO queues, the messages are consumed in the order they are published sequentially. 

The standard queue offers at least one delivery at a time, but in FIFO exactly one processing is allowed at a time. However, we can define and set a batch(say 10) which means that in one processing up to 10 messages can be processed or consumed. The maximum we can set is a batch of 300.

Using FIFO is quite expensive as compared to standard.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/864c83a3-986b-4529-bd4b-482c35fcf33e)

# Applications

+ Fanout - To implement functionality like a one-to-many notification service where we publish messages on one SNS topic and we can deliver it to different queues defined which are here consumers for the SNS.
+ Serverless Processing - The coupling of AWS lambda and SQS is very famous in AWS and among serverless infrastructure. Where a lambda function is integrated as a consumer to the SQS and it consumes the message periodically and performs further processing.
+ Job buffering - Consider a scenario like taking a snapshot of a database every morning, we can schedule the SQS to trigger other AWS services like EC2 and Lambda functions for some computation.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/f29757d0-0f91-48f2-aa74-414f456e50f3)

# Hands-on

### Create a SQS queue
Go to the SQS console and click on create a queue, this will ask some basic questions to configure the SQS and its further behavior will depend upon the configuration we make.  At first, it will ask for the Standard vs FIFO queue, you can select one basis on the discussion we had above. For learning purposes, go for the Standard queue. Then given this queue a name, the name is not required to be globally unique, unlike SQS.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/187ae24c-79e7-4c89-be1b-d621fab21640)

Next to the configuration part, it does ask for a decent number of fields. 
+ Visibility Timeout - By default it is 30 sec. So when a message enters a queue, what happens in the background is that a thread picks up a message and put it in the queue, so until a set time, it will be invincible to other threads so that they won't pick them up. Within the visibility timeout, if the message doesn't get consumed or processed, it will again be available for a thread to put back in the queue for a retry.

+ Message Retention Period - This is simply the amount of time a message stays in the queue. It is suggested to keep it low, 1 day and even lower because it doesn't make any sense that a message will stay in a queue for some 4 days. Again, it depends upon the requirements of the application one is building.

+ Delivery Delay - When a message is published to the queue initially,  we do not want it to be visible for a thread to process until a set delivery delay. By default, it is 0 sec which means that it will be immediately available for processing as soon as the messages are published. Useful in condition like a race condition, where you wants something to process first.

+ Maximum message size - Set the maximum size of the message a publisher can send to the queue. The max one can set is 128 KB. However, there are some libraries available using which we can publish messages up to size 2 GB integrating S3 bucket (obviously).

+ Receive message wait time - The service side can decide the messages to process based on the data. Say if a message is empty, it will wait for receive message wait time to check if there's any other message in the queue that does have data or not, else it will process the empty message only.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/c965304f-9767-4922-b14b-0eb37e245b17)

In the Access Policy, here we can define who can send messages to the queue and who can consume messages from these queues. By default, it is limited to the owner, but additionally, we can allow other AWS accounts or AIM users by providing the required identification or credentials.

Dead Letter Queue - When a message in the queue fails to process or consumed, after a delay it will again enters the queue for a retry. But what if it keeps happen again and again? Using dead letter queue, SQS add this to a secondary queue using the dead letter queue configuration. Additionally we can set alarm to this secondary queue where if it exceed a given number it will notify me. We can even program it such that after a defined condition or time, the main queue can again pick these secondary queue messages and attempts for the processing.
The secondary queue created is sister DLQ in, and follows a name convention like if main queue is named `DemoQueue`, then the sister queue is known as `DemoQueueDLQ`
![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/7d7981af-cda6-42ac-bc12-702ebade5d59)

Once created the queue, the dashboard looks like

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/5bb77d53-9ab6-4e6c-adfc-01a8ed23a335)

In the dahsboard, there is a `Purge` button on the top right which means that we can delete all the messages at once. You can send messages using the dashboard and can can play around it.
While sending a message, ther's a optional message attributes section which is used to filter data on basis of some tags, attributes to be precise. On messgae can have at max 10 attributes.

![image](https://github.com/nikhil25803/aws-learnings/assets/93156825/26040594-75a3-4f75-ba57-2da7e2c9a98c)

At the receiver end, we can see that there is a `Maximum Message Count` section , which simply defines the batch size of the message to be processed at once. On clicking the `Poll Message` you can receive the messages that you sent or added to the queue.

