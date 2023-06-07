import boto3
import json

def list_backup_policies():
    # Create a Boto3 client for AWS Organizations
    client = boto3.client('organizations')

    # Retrieve the list of backup policies
    response = client.list_policies(Filter='BACKUP_POLICY')

    # Extract the list of policies
    backup_policies = response['Policies']

    # Specify the output folder where JSON files will be stored
    output_folder = '/home/sahil/Documents/All_detail/output/Policies/backup_policies'

    # Get the details of each backup policy
    for backup_policy in backup_policies:
        policy_id = backup_policy['Id']
        policy_name = backup_policy['Name']

        # Retrieve the policy content
        policy_response = client.describe_policy(PolicyId=policy_id)
        policy_content_str = policy_response['Policy']['Content']

        # Create a separate JSON file for each backup policy in the output folder
        policy_file_name = f"{output_folder}/{policy_name}.json"

        # Load the policy content as JSON to format it
        policy_content = json.loads(policy_content_str)

        # Write the formatted policy content to the JSON file
        with open(policy_file_name, 'w') as file:
            json.dump(policy_content, file, indent=4)

        print(f"JSON file generated for policy '{policy_name}'.")



