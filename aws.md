# AWS

## Spinning up an EC2 Instance, the Clicky Way

 1. Go to your region's EC2 dashboard, e.g. [https://us-west-1.console.aws.amazon.com/ec2/v2/home?region=us-west-2](https://us-west-1.console.aws.amazon.com/ec2/v2/home?region=us-west-2)
 2. Click the big blue "Launch Instance" button.
 3. Choose an Amazon Machine Image (AMI). Ubuntu 14.04 LTS (HVM) may suit your needs well. Be sure choose an AMI that uses HVM virtualization [for a number of reasons](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/virtualization_types.html). 
 4. Choose an Instance Type. If your workload will allow it, a t2.micro instance may be eligible for [AWS's Free Tier](https://aws.amazon.com/free/). Otherwise, take a look at the [EC2 Pricing](https://aws.amazon.com/ec2/pricing/) and select an instance type appropriate for your needs and budget. Once selected, click "Next: Configure Instance Details". 
 5. Configure Instance Details. Depending on how moved-in you are in your AWS environment, you will configure the following options appropriate for your environment. The below assumes a fresh shiny new environment:
    * Number of instances: 1
    * Purchasing option: Uncheck "Request Spot Instances"
    * Network: Choose your default VPC, if you have only one. Otherwise, choose one as appropriate for your environment.
    * Subnet: Unless you care, choose "No preference". 
    * Auto-assign Public IP: Same as above, unless you care, choose "Enable" from the dropdown.
    * IAM role: Unless you have IAM roles configured, choose "None"
    * Shutdown behavior: Choose "stop" unless you want your instance to be destroyed (terminated) upon shutdown (probably not what you want if you're reading this). 
    * Enable termination protection: Unchecked
    * Monitoring: Unchecked
    * Tenancy: Shared
    * Click "Next: Add Storage"
 6. Add Storage. Depending on which AMI/Instance you chose, you will have the opportunity to change the default disk size at this step. In the case of a t2.micro instance, the fault is 8GB which may need a nudge depending on your needs. You can also add additional volumes at this step. When finished, click "Next: Tag Instance". 
 7. Tag Instance. Practically speaking, this is your best opportunity to name the instance you're creating in order to find it later. Enter an appropriate value for the Name key/value pair, e.g. wip1.lahacknight.com. Click "Next: Configure Security Group" when ready to continue. 
 8. Configure Security Group. Unless you already have some appropriate security groups setup, choose "Create a new security group". This, in essence, is the port filtering policy which will be enforced outside of your instance. Most likely you'll want to create a security group just for this instance, so give it a name that associates it with the instance name, e.g. wip1.lahacknight.com. Descriptions are nice, fill it in as you like e.g. "SSH/HTTP/HTTPS in for wip1 webapp.". Next, select what ports you would like to publish to the web. A standalone web app might have HTTP(80), HTTPS(443) open for web serving and also SSH(22) for console and file upload/downloads. You can always update this later, so feel free to be restrictive at first (e.g. just allow SSH from your own IP) if you like. Click "Review and Launch" when ready to proceed. 
 9. Review Instance Launch. Review the configuration and if all looks ok, click "Launch". You will be prompted to provide an SSH key pair. Unless you already have one configured you like to reuse for different hosts, select "Create a new key pair". Provide a meaningful name for the keypair, the instance Name is usually a good idea, e.g. 'wip1_lahacknight_com'. Click download keypair. Your browser will now receive a private key for you to store on your computer. Keep it in a safe place, this file is all one would need in order to gain shell access to your server. Typically you'll move the file from your Downloads directory into the `.ssh` directory within your home folder. It's a good idea to do this now before you forget (example: `mv ~/Downloads/wip1_lahacknight_com.pem ~/.ssh/`). If you are running a Unix-like system, you will need to change the permissions on this pem file so it is only readable by you. For example, `chmod 400 ~/.ssh/wip1_lahacknight_com.pem`. Once that's done, you can click "Launch Instances". 
 10. You will be directed to a Launch Status page which will have a link to your instance. Your instance is identified with an instance ID which may be in the format of i-ec2NNNNN. Go ahead and click on that link or click on the big blue "View Instances" button. 
 11. You will now be sent to your instance dashboard. Here you should see your new instance listed. Once they "Instance State" changes to "running", your instance is ready for use. You will also see the public IP you can use to access your new instance. 
 12. Congrats! You're done, you can now connect to your instance via SSH. To do so, you can add your private key identity to your SSH authentication agent via `ssh-add ~/.ssh/wip1_lahacknight_com.pem`. You can now connect to your host via `ssh ubuntu@your.public.ip.address`. If you're less lazy than me, you can skip adding the key and just specify the identity when connecting `ssh -i ~/.ssh/wip1_lahacknight_com.pem ubuntu@your.public.ip.address`. 
 
  


