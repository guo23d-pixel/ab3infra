import aws_cdk as core
import aws_cdk.assertions as assertions

from ab3infra.ab3infra_stack import Ab3InfraStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ab3infra/ab3infra_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Ab3InfraStack(app, "ab3infra")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
