import json
import random


def random_drink():
    drinks = ["wine", "coffee", "beer"]
    return random.choice(drinks)


def lambda_handler(event, context):
    drink = random_drink()
    message = f"You should now drink: {drink}"

    return {"statusCode": 200, "body": json.dumps({"message": message, "drink": drink})}
