import boto3
import json

def list_scp_policies():
    # Create a Boto3 client for AWS Organizations
    client = boto3.client('organizations')

    # Retrieve the list of SCPs
    response = client.list_policies(Filter='SERVICE_CONTROL_POLICY')

    # Extract the list of policies
    scp_policies = response['Policies']

    # Specify the output folder where JSON files will be stored
    output_folder = '/home/sahil/Documents/All_detail/output/Policies/scp_policies'

    # Get the details of each SCP
    for scp_policy in scp_policies:
        policy_id = scp_policy['Id']
        policy_name = scp_policy['Name']

        # Retrieve the policy content
        policy_response = client.describe_policy(PolicyId=policy_id)
        policy_content_str = policy_response['Policy']['Content']

        # Create a separate JSON file for each SCP policy in the output folder
        policy_file_name = f"{output_folder}/{policy_name}.json"

        # Load the policy content as JSON to format it
        policy_content = json.loads(policy_content_str)

        # Write the formatted policy content to the JSON file
        with open(policy_file_name, 'w') as file:
            json.dump(policy_content, file, indent=4)

        print(f"JSON file generated for policy '{policy_name}'.")



