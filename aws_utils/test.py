import boto3

client = boto3.client('iam')

iam_response = client.get_instance_profile(
    InstanceProfileName='ec2-ssm-role'
)

iam_arn = iam_response['InstanceProfile']['Roles'][0]['Arn']
print(iam_arn)
iam_arn = iam_arn.replace(':role', ':instance-profile')
print(iam_arn)
