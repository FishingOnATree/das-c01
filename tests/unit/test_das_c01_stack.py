import aws_cdk as core
import aws_cdk.assertions as assertions

from das_c01.das_c01_stack import DasC01Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in das_c01/das_c01_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DasC01Stack(app, "das-c01")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
