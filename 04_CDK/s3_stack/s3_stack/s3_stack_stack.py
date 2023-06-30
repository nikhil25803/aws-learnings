from constructs import Construct
from aws_cdk import (
    # Duration,
    Stack,
    # aws_iam as iam,
    # aws_sqs as sqs,
    # aws_sns as sns,
    # aws_sns_subscriptions as subs,
    aws_s3 as s3
)

class S3StackStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_bucket = s3.Bucket(
            self,
            "mybucket1",
            bucket_name="s3bucket30062023",
            versioned=True,
            public_read_access=True,
        )


        # queue = sqs.Queue(
        #     self, "S3StackQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        # topic = sns.Topic(
        #     self, "S3StackTopic"
        # )

        # topic.add_subscription(subs.SqsSubscription(queue))
