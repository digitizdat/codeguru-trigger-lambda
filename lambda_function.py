import json
import uuid

import boto3

print("Loading function")


def lambda_handler(event, context):
    # Extract the incoming message
    msg = json.loads(event["Records"][0]["Sns"]["Message"])

    # Extract the relevant CodeGuru call parameters
    repo = msg["detail"]["repositoryName"]
    branch = msg["detail"]["referenceName"]
    assn = None
    guru = boto3.client("codeguru-reviewer")
    for x in guru.list_repository_associations()[
        "RepositoryAssociationSummaries"
    ]:
        if x["Name"] == repo:
            assn = x["AssociationArn"]

    if assn == None:
        m = f"No CodeGuru association found for repo {repo}"
        print(m)
        return json.dumps({"status": m})

    # Call CodeGuru
    result = guru.create_code_review(
        Name=f"{msg['detail']['repositoryName']}-{uuid.uuid4().hex}",
        RepositoryAssociationArn=assn,
        Type={
            "RepositoryAnalysis": {"RepositoryHead": {"BranchName": branch}},
            "AnalysisTypes": [
                "Security",
                "CodeQuality",
            ],
        },
    )

    # Return the result of the Boto call
    return json.dumps(result, default=str)
