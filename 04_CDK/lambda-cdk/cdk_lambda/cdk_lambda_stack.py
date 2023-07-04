from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda,
    aws_apigateway,
    # aws_sqs as sqs,
)


from constructs import Construct


class CdkLambdaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        random_drink_function = aws_lambda.Function(
            self,
            id="RandomDrinkV0307",
            code=aws_lambda.Code.from_asset("compute"),
            handler="random_drink.lambda_handler",
            runtime=aws_lambda.Runtime.PYTHON_3_8,
        )

        aws_apigateway.LambdaRestApi(
            self,
            "Endpoint",
            handler=random_drink_function,
        )
