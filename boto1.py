import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)


ec2 = boto3.resource('ec2')
vpc = ec2.create_vpc(CidrBlock='10.0.2.0/24',TagSpecifications=[
        {
            'ResourceType': 'vpc',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'my_vpc2'
                },
            ]
        },
    ])
print(vpc)
# vpc.create_tags(Tags=[{"Key": "Name", "Value": "my_vpc1"}])

vpc.wait_until_available()

# enable public dns hostname so that we can SSH into it later
ec2Client = boto3.client('ec2')

print(ec2Client)
ec2Client.modify_vpc_attribute( VpcId = vpc.id , EnableDnsSupport = { 'Value': True } )
ec2Client.modify_vpc_attribute( VpcId = vpc.id , EnableDnsHostnames = { 'Value': True } )