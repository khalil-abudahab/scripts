import os
import requests
from datetime import datetime

project_id = "2uBbvYgdqRTiiK5XbvwrKh"
api_token = os.getenv("MICROREACT_ACCESS_TOKEN")

# Get the Microreact document for the project
resp = requests.get(
    f"https://microreact.org/api/projects/json?project={project_id}",
    headers={"Access-Token": api_token}
)
mr_document = resp.json()

# Display list of keys in the Microreact document
print(mr_document.keys())

# Define the content of the new metadata file
new_metadata_file_content = """
id,__latitude,__longitude,Country,Country__colour,Country__shape,Pedalism
Bovine,46.227638,2.213749,France,Red,Square,Four
Gibbon,15.870032,100.992541,thailand,Green,circle,Two
Orangutan,-0.589724,101.3431058,sumatra,Blue,Circle,Two
Gorilla,1.373333,32.290275,Uganda,#CC33FF,Circle,Two
Chimp,-0.228021,15.827659,Congo,orange,Circle,Two
Human,55.378051,-3.435973,UK,#CCFF33,Circle,Two
Mouse,40.463667,-3.74922,Spain,#00FFFF,square,four
NEW SAMPLE,0,0,US,#000000,,
"""

# Update metadata file
mr_document["files"]["data-file-1"]["url"] = None
mr_document["files"]["data-file-1"]["blob"] = new_metadata_file_content

# Update project title
mr_document["meta"]["name"] = f"Last updated at {datetime.utcnow().isoformat()}"

# Prepare to update the project with the modified document
update_resp = requests.post(
    f"https://microreact.org/api/projects/update?project={project_id}",
    headers={
        "Access-Token": api_token,
        "Content-type": "application/json; charset=UTF-8"
    },
    json=mr_document
)

# Check if the update was successful
if update_resp.status_code == 200:
    print("Project updated successfully.")
else:
    print("Failed to update project:", update_resp.status_code, update_resp.text)
