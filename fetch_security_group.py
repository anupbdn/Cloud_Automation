import boto3


var_instance_id = input('enter instance id: ')

print(f'#### Security Groups of {var_instance_id} #####')

ec2 = boto3.resource('ec2')
instance = ec2.Instance(var_instance_id)

sg_list = []
for group in instance.security_groups:
    # print(group['GroupId'])
    sg_list.append(group['GroupId'])

# for group in sg_list:
#     print(group)

call_ec2 = boto3.client('ec2')

for groupid in sg_list:
    response = call_ec2.describe_security_groups(GroupIds=[groupid])
    print(f'\nRules for {groupid} \n')
    print(response['SecurityGroups'][0])