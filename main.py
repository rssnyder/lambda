def lambda_handler(event, context):
    print(event)
    print(context)
    print(addition(1, 4))


def addition(first, second):
    return first + second
