import pandas as pd
import json
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings("ignore")

# Sample dataset (replace with your JSON file or API call in a real environment)
dataset = [
    {
        "condition": None,
        "conditionVersion": None,
        "createdBy": "",
        "createdOn": "2025-02-08T12:34:26.110962+00:00",
        "delegatedManagedIdentityResourceId": None,
        "description": None,
        "id": "/subscriptions/3ec54845-d845-4c08-8c5e-f2ab376b0e6e/providers/Microsoft.Authorization/roleAssignments/be00961e-47c7-445a-aaa6-5e9a69e6e90f",
        "name": "be00961e-47c7-445a-aaa6-5e9a69e6e90f",
        "principalId": "ba86f87e-0de7-43c5-abfb-88ca3012ae74",
        "principalName": "admin@gitsa619.onmicrosoft.com",
        "principalType": "User",
        "roleDefinitionId": "/subscriptions/3ec54845-d845-4c08-8c5e-f2ab376b0e6e/providers/Microsoft.Authorization/roleDefinitions/8e3af657-a8ff-443c-a75c-2fe8c4bcb635",
        "roleDefinitionName": "Owner",
        "scope": "/subscriptions/3ec54845-d845-4c08-8c5e-f2ab376b0e6e",
        "type": "Microsoft.Authorization/roleAssignments",
        "updatedBy": "",
        "updatedOn": "2025-02-08T12:34:26.110962+00:00"
    },
    {
        "condition": None,
        "conditionVersion": None,
        "createdBy": "ba86f87e-0de7-43c5-abfb-88ca3012ae74",
        "createdOn": "2025-04-06T21:40:54.071037+00:00",
        "delegatedManagedIdentityResourceId": None,
        "description": None,
        "id": "/subscriptions/3ec54845-d845-4c08-8c5e-f2ab376b0e6e/providers/Microsoft.Authorization/roleAssignments/1cc1d6b9-ccaa-40fd-8b57-679e68f46ab2",
        "name": "1cc1d6b9-ccaa-40fd-8b57-679e68f46ab2",
        "principalId": "1ba86577-8d68-46ca-ab1e-0718edb7f258",
        "principalName": "b9cc276d-4d90-46b6-9073-d29f974d6526",
        "principalType": "ServicePrincipal",
        "roleDefinitionId": "/subscriptions/3ec54845-d845-4c08-8c5e-f2ab376b0e6e/providers/Microsoft.Authorization/roleDefinitions/b24988ac-6180-42a0-ab88-20f7382dd24c",
        "roleDefinitionName": "Contributor",
        "scope": "/subscriptions/3ec54845-d845-4c08-8c5e-f2ab376b0e6e",
        "type": "Microsoft.Authorization/roleAssignments",
        "updatedBy": "ba86f87e-0de7-43c5-abfb-88ca3012ae74",
        "updatedOn": "2025-04-06T21:40:54.071037+00:00"
    },
    {
        "condition": None,
        "conditionVersion": None,
        "createdBy": "ba86f87e-0de7-43c5-abfb-88ca3012ae74",
        "createdOn": "2025-04-24T16:01:46.813230+00:00",
        "delegatedManagedIdentityResourceId": None,
        "description": None,
        "id": "/subscriptions/3ec54845-d845-4c08-8c5e-f2ab376b0e6e/providers/Microsoft.Authorization/roleAssignments/d244800a-0962-429d-8f94-9c03b3f57b08",
        "name": "d244800a-0962-429d-8f94-9c03b3f57b08",
        "principalId": "f0e6ce37-3017-4e0a-a0ab-43e9ceb6f8d5",
        "principalName": "4995ef7b-4944-40df-826d-20e21b2a08ba",
        "principalType": "ServicePrincipal",
        "roleDefinitionId": "/subscriptions/3ec54845-d845-4c08-8c5e-f2ab376b0e6e/providers/Microsoft.Authorization/roleDefinitions/b24988ac-6180-42a0-ab88-20f7382dd24c",
        "roleDefinitionName": "Contributor",
        "scope": "/subscriptions/3ec54845-d845-4c08-8c5e-f2ab376b0e6e",
        "type": "Microsoft.Authorization/roleAssignments",
        "updatedBy": "ba86f87e-0de7-43c5-abfb-88ca3012ae74",
        "updatedOn": "2025-04-24T16:01:46.813230+00:00"
    },
    {
        "condition": None,
        "conditionVersion": None,
        "createdBy": "ba86f87e-0de7-43c5-abfb-88ca3012ae74",
        "createdOn": "2025-04-24T16:01:47.961543+00:00",
        "delegatedManagedIdentityResourceId": None,
        "description": None,
        "id": "/subscriptions/3ec54845-d845-4c08-8c5e-f2ab376b0e6e/providers/Microsoft.Authorization/roleAssignments/819fc6a8-bceb-467d-8658-683f15203324",
        "name": "819fc6a8-bceb-467d-8658-683f15203324",
        "principalId": "f0e6ce37-3017-4e0a-a0ab-43e9ceb6f8d5",
        "principalName": "4995ef7b-4944-40df-826d-20e21b2a08ba",
        "principalType": "ServicePrincipal",
        "roleDefinitionId": "/subscriptions/3ec54845-d845-4c08-8c5e-f2ab376b0e6e/providers/Microsoft.Authorization/roleDefinitions/18d7d88d-d35e-4fb5-a5c3-7773c20a72d9",
        "roleDefinitionName": "User Access Administrator",
        "scope": "/subscriptions/3ec54845-d845-4c08-8c5e-f2ab376b0e6e",
        "type": "Microsoft.Authorization/roleAssignments",
        "updatedBy": "ba86f87e-0de7-43c5-abfb-88ca3012ae74",
        "updatedOn": "2025-04-24T16:01:47.961543+00:00"
    }
]

# Save dataset to a JSON file for processing (optional, for demo)
with open("role_assignments.json", "w") as f:
    json.dump(dataset, f)

# Load dataset into a pandas DataFrame
df = pd.DataFrame(dataset)

# Select relevant features for ML analysis
features = ['principalType', 'roleDefinitionName', 'scope']

# Preprocess the data
# Encode categorical variables
le_principal = LabelEncoder()
le_role = LabelEncoder()
le_scope = LabelEncoder()

df['principalType_encoded'] = le_principal.fit_transform(df['principalType'])
df['roleDefinitionName_encoded'] = le_role.fit_transform(df['roleDefinitionName'])
df['scope_encoded'] = le_scope.fit_transform(df['scope'])

# Create feature matrix for ML
X = df[['principalType_encoded', 'roleDefinitionName_encoded', 'scope_encoded']]

# Initialize Isolation Forest model
model = IsolationForest(contamination=0.25, random_state=42)

# Fit the model and predict anomalies
df['anomaly'] = model.fit_predict(X)

# Define risky roles that could enable privilege escalation
risky_roles = ['Owner', 'User Access Administrator']

# Analyze anomalies and risky configurations
print("Privilege Escalation Vulnerability Scan Results")
print("=" * 50)

for index, row in df.iterrows():
    if row['anomaly'] == -1 or row['roleDefinitionName'] in risky_roles:
        print(f"\nPotential Vulnerability Detected:")
        print(f"- Role Assignment ID: {row['id']}")
        print(f"- Principal: {row['principalName']} ({row['principalType']})")
        print(f"- Role: {row['roleDefinitionName']}")
        print(f"- Scope: {row['scope']}")
        print("Reason:")
        if row['roleDefinitionName'] in risky_roles:
            print(f"  - '{row['roleDefinitionName']}' role is highly privileged and can enable privilege escalation.")
        if row['anomaly'] == -1:
            print("  - Identified as an anomaly by ML model due to unusual configuration.")
        if row['principalType'] == 'ServicePrincipal' and row['roleDefinitionName'] in risky_roles:
            print("  - Service principals with high-privilege roles are particularly risky.")

# Save results to a file
results = df[df['anomaly'] == -1][['id', 'principalName', 'principalType', 'roleDefinitionName', 'scope']]
results.to_csv("privilege_escalation_vulnerabilities.csv", index=False)
print("\nResults saved to 'privilege_escalation_vulnerabilities.csv'")