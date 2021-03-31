from jinja2 import Template

shortname = input("shortname: ")
accountid = input("Enter your accountid: ")
ellucianaccountid = input("ellucianaccountid: ")
region = input("region: ")
vpc_id = input("vpcid: ")
pubsub1 = input("pubsub1: ")
pubsub2 = input("pubsub2: ")

tm = Template(
    
"""
- '{{ accountid }}':
    ellucian_account_id: '{{ ellucianaccountid }}'
    region: {{region}}
    shortname: {{shortname}}        
    vpc_id: {{vpc_id}}        
    pub_sub_id_1: {{pubsub1}}
    pub_sub_id_2: {{pubsub2}}
    listeners: ["7100"]
    services:
        - service-touchnet: https://git.ellucian.com/scm/cloudops/service-touchnet.git@master """)
msg = tm.render(accountid=accountid, ellucianaccountid=ellucianaccountid, shortname=shortname, region=region, vpc_id=vpc_id, pubsub1=pubsub1, pubsub2=pubsub2  )

print(msg)