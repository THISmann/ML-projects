import json
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Configuration des paramètres
NUM_ENTRIES = 1000  # Taille du dataset
ROLES = ["Owner", "Contributor", "User Access Administrator", "Reader", "Security Admin", "Storage Blob Data Contributor"]
PRINCIPAL_TYPES = ["User", "ServicePrincipal", "Group"]
SCOPES = [
    "/subscriptions/3ec54845-d845-4c08-8c5e-f2ab376b0e6e",
    "/subscriptions/3ec54845-d845-4c08-8c5e-f2ab376b0e6e/resourceGroups/prod-rg",
    "/subscriptions/3ec54845-d845-4c08-8c5e-f2ab376b0e6e/resourceGroups/test-rg"
]

def generate_fake_dataset():
    dataset = []
    
    for _ in range(NUM_ENTRIES):
        # Génération de dates réalistes
        created_on = fake.date_time_between(
            start_date="-2y", 
            end_date="now"
        ).isoformat() + "Z"
        
        entry = {
            "condition": random.choice([None, "RequireMultiFactorAuth", "RequireApproval"]),
            "createdOn": created_on,
            "id": f"/subscriptions/3ec54845-d845-4c08-8c5e-f2ab376b0e6e/providers/Microsoft.Authorization/roleAssignments/{fake.uuid4()}",
            "principalId": fake.uuid4(),
            "principalName": fake.user_name() + "@" + fake.domain_name() if random.random() > 0.3 else None,
            "principalType": random.choice(PRINCIPAL_TYPES),
            "roleDefinitionName": random.choice(ROLES),
            "scope": random.choice(SCOPES),
            "risk_label": 0,  # Nouvelle colonne pour le ML
            "has_mfa": random.choice([True, False]),
            "last_access_time": (datetime.fromisoformat(created_on[:-1]) + timedelta(days=random.randint(0, 365))).isoformat() + "Z"
        }
        
        # Ajout de motifs d'attaque réalistes
        if entry["roleDefinitionName"] in ["Owner", "User Access Administrator"] and entry["scope"].startswith("/subscriptions"):
            entry["risk_label"] = 1 if random.random() > 0.2 else 0
        
        if entry["principalType"] == "ServicePrincipal" and entry["roleDefinitionName"] == "Contributor":
            entry["risk_label"] = 1 if random.random() > 0.3 else 0
        
        dataset.append(entry)
    
    return dataset

# Génération et sauvegarde du dataset
dataset = generate_fake_dataset()
with open("azure_role_assignments_large.json", "w") as f:
    json.dump(dataset, f, indent=2)

print(f"Dataset généré avec {NUM_ENTRIES} entrées")