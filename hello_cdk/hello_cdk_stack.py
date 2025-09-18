from aws_cdk import (
    Stack,
    aws_lambda as _lambda, # Import the Lambda module
    CfnOutput, # Import CfnOutput
    )
from constructs import Construct

class HelloCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # Define Lambda inside _init_
        my_function = _lambda.Function(
            self, "HelloWorldFunction",
            runtime=_lambda.Runtime.NODEJS_20_X,  # Provide any supported Node.js runtime
            handler="index.handler",
            code=_lambda.Code.from_inline(
                """
                exports.handler = async function(event) {
                  return {
                    statusCode: 200,
                    body: JSON.stringify('Hello CDK!'),
                  };
                };
                """
            ),
        )

        # Add a Function URL
        my_function_url = my_function.add_function_url(
                auth_type=_lambda.FunctionUrlAuthType.NONE,
        )

        # Output the URL to CloudFormation
        CfnOutput(self,"myFunctionUrlOutput",value=my_function_url.url,)
