import boto3
client = boto3.client('ec2')
response = client.run_instances(
    ImageId='string',
    InstanceType='t2.micro',
    KeyName='string',
    MaxCount=0,
    MinCount=0,
)
