# codeguru-trigger-lambda
Basic Lambda function that triggers a CodeGuru review from an SNS notification from a CodeCommit push

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

This example shows how to automatically trigger a CodeGuru Code Review on a push (rather than just on a pull request). You just need to follow a couple basic steps to enable push notifications on the repo and create a Lambda function that will subscribe to the notifications and trigger a CodeGuru review for the given repo / branch.

1. Create an [SNS topic configured to receive CodeCommit notifications](https://docs.aws.amazon.com/dtconsole/latest/userguide/troubleshooting.html#troubleshooting-no-SNS).
1. Create a [CodeCommit trigger for an Amazon SNS topic](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify-sns.html), checking the "Branches and tags... updated" box.

1. Write a Lambda function to take the SNS message and trigger the CodeGuru review. The function will need an execution role that can read the SNS topic and make the CodeGuru calls. I have provided sample code here to get you started.
