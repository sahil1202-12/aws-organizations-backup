# AWS Organizations Backup

## Problem Statement

AWS Organizations is a service provided by Amazon Web Services (AWS) that allows you to centrally manage and govern multiple AWS accounts. It provides a way to organize your accounts into a hierarchical structure and apply policies across the organization.

The AWS Organizations Backup tool provides users with the ability to capture and backup various details related to their AWS accounts. It offers features to retrieve and store information such as account details, enabled services, enabled policy types, and policies.

By using this tool, users can gain insights into the changes made within their accounts and track important information. The backup process ensures that important data is preserved, allowing for easy reference and analysis.

In summary, AWS Organizations Backup simplifies the process of capturing and storing vital details about AWS accounts, providing users with a comprehensive view of their account configuration and changes over time.



## Permissions Required 

To successfully execute the scripts and access the necessary resources, the following AWS Identity and Access Management (IAM) permissions should be assigned to the user or role executing the project:

1. `organizations:DescribeOrganization` - Required to retrieve information about the AWS Organization.
2. `organizations:ListAccounts` - Needed to list the AWS accounts within the organization.
3. `organizations:ListAWSServiceAccessForOrganization` - Required to list the AWS services enabled for the organization.
4. `organizations:ListRoots` - Required to list the roots in the organization.
5. `organizations:DescribePolicyType` - Required to describe the policy types associated with the organization's roots.
6. `organizations:ListPolicies` - Required to list the policies in the organization.
7. `organizations:DescribePolicy` - Required to describe the details of a specific policy.
8. `organizations:ListTargetsForPolicy` - Required to list the targets associated with a policy.

Ensure that the user or role executing the scripts has the appropriate permissions assigned to successfully interact with the AWS Organizations service and access the required resources.

<<<<<<< HEAD

=======
Check out the following GIF to see the complete procedure of getting AWS Organization Dependency. 
![GIF](https://github.com/sahil121-12/aws-organizations-backup/blob/main/all-steps.gif)
>>>>>>> c49118fdd4386495edc91d3c5190837d72cac3b2


## Getting Started

To use this project, follow these steps:

1. Clone the repository to your local machine.
```bash
git clone https://github.com/sahil1202-12/aws-org-dependency-analyzer
```
2. Install the required dependencies listed in `requirement.txt`.
            
```bash
pip3 install -r requirement.txt
```
3. Make sure you run the above command before running the `main.py`.
4. Modify the scripts or add new functionality as needed.
5. Execute `main.py` to run the project.
6. Check the output files in the `output` directory for the generated results.

Feel free to explore each directory and file for more detailed information about their respective contents and functionalities.

