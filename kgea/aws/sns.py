#!/usr/bin/env python
#
# This CLI script will take  host AWS account id, guest external id and
# the name of a host account IAM role, to obtain temporary AWS service
# credentials to execute an AWS Secure Token Service-mediated access
# to a Simple Notification Service (SNS).
#
import sys
from os.path import abspath, dirname
from pathlib import Path

from json import dumps

import boto3

from kgea.aws.assume_role import AssumeRole


def usage(err_msg: str = ''):
    if err_msg:
        print(err_msg)
    print("Usage: ")
    print(
        "python -m kgea.aws." + Path(sys.argv[0]).stem +
        " <host_account_id> <guest_external_id> <target_iam_role_name>"
    )
    exit(0)


# Run the module as a CLI
if __name__ == '__main__':
    
    account_id_from_user: str = ""
    external_id: str = ""
    role_name_from_user: str = ""
    
    # Prompt user for target and action for the EC2 service
    if len(sys.argv) >= 4:
        
        account_id_from_user = sys.argv[1]
        external_id = sys.argv[2]
        role_name_from_user = sys.argv[3]
        
        assumed_role = AssumeRole(
            host_account=account_id_from_user,
            guest_external_id=external_id,
            iam_role_name=role_name_from_user
        )
        
        sns_client = assumed_role.get_client('sns')

        # TODO: SNS specific actions here
    