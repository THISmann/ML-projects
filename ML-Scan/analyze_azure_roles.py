# import json

# # Règles de Détection des Risques
# RISKY_ROLES = ["Owner", "User Access Administrator", "Contributor"]
# SCOPE_THRESHOLD = "/subscriptions/"  # Niveau Abonnement

# def load_data(file_path):
#     with open(file_path, 'r') as f:
#         return json.load(f)

# def analyze_assignments(assignments):
#     findings = []
    
#     for assignment in assignments:
#         role = assignment.get("roleDefinitionName", "")
#         principal_type = assignment.get("principalType", "")
#         scope = assignment.get("scope", "")
        
#         # Règle 1 : Rôles à Haut Risque
#         if role in RISKY_ROLES:
#             risk_level = "CRITIQUE" if role == "Owner" else "ÉLEVÉ"
#             reason = f"Rôle à haut risque : {role}"
            
#             # Règle 2 : Scope au Niveau Abonnement
#             if SCOPE_THRESHOLD in scope:
#                 reason += " | Scope : Abonnement entier"
                
#             # Règle 3 : ServicePrincipal avec Droits Élevés
#             if principal_type == "ServicePrincipal" and role in ["Contributor", "User Access Administrator"]:
#                 reason += " | ServicePrincipal avec privilèges élevés"
            
#             findings.append({
#                 "id": assignment.get("id"),
#                 "principal": assignment.get("principalName"),
#                 "role": role,
#                 "risk": risk_level,
#                 "reason": reason
#             })
    
#     return findings

# if __name__ == "__main__":
#     assignments = load_data("role_assignments.json")
#     results = analyze_assignments(assignments)
    
#     print("=== Résultats de l'Analyse ===")
#     for item in results:
#         print(f"[{item['risk']}] {item['principal']} ({item['role']})")
#         print(f"  Raison : {item['reason']}")
#         print(f"  ID : {item['id']}\n")



import json
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report

# Règles de Détection des Risques
RISKY_ROLES = ["Owner", "User Access Administrator", "Contributor"]
SCOPE_THRESHOLD = "/subscriptions/"  # Niveau Abonnement

def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def analyze_assignments(assignments):
    findings = []
    
    for assignment in assignments:
        role = assignment.get("roleDefinitionName", "")
        principal_type = assignment.get("principalType", "")
        scope = assignment.get("scope", "")
        
        # Règle 1 : Rôles à Haut Risque
        if role in RISKY_ROLES:
            risk_level = "CRITIQUE" if role == "Owner" else "ÉLEVÉ"
            reason = f"Rôle à haut risque : {role}"
            
            # Règle 2 : Scope au Niveau Abonnement
            if SCOPE_THRESHOLD in scope:
                reason += " | Scope : Abonnement entier"
                
            # Règle 3 : ServicePrincipal avec Droits Élevés
            if principal_type == "ServicePrincipal" and role in ["Contributor", "User Access Administrator"]:
                reason += " | ServicePrincipal avec privilèges élevés"
            
            findings.append({
                "id": assignment.get("id"),
                "principal": assignment.get("principalName"),
                "role": role,
                "risk": risk_level,
                "reason": reason
            })
    
    return findings

def prepare_data_for_ml(assignments):
    data = []
    for assignment in assignments:
        role = assignment.get("roleDefinitionName", "")
        principal_type = assignment.get("principalType", "")
        scope = assignment.get("scope", "")
        
        # Définir le niveau de risque comme étiquette (1: critique, 0: élevé)
        risk_label = 1 if role == "Owner" else (0 if role in ["User Access Administrator", "Contributor"] else -1)
        
        data.append({
            "role": role,
            "principal_type": principal_type,
            "scope": scope,
            "risk_label": risk_label
        })
    
    df = pd.DataFrame(data)
    df = df[df['risk_label'] != -1]  # Retirer les lignes sans risque défini
    return df

def build_model_pipeline():
    categorical_features = ['role', 'principal_type']
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ])
    
    return Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ])

if __name__ == "__main__":
    assignments = load_data("role_assignments.json")
    
    # Analyse avec règles
    results = analyze_assignments(assignments)
    
    print("=== Résultats de l'Analyse ===")
    for item in results:
        print(f"[{item['risk']}] {item['principal']} ({item['role']})")
        print(f"  Raison : {item['reason']}")
        print(f"  ID : {item['id']}\n")

    # Préparation des données pour le ML
    df_ml = prepare_data_for_ml(assignments)
    
    # Séparer les caractéristiques et les étiquettes
    X = df_ml[['role', 'principal_type']]
    y = df_ml['risk_label']

    # Division des données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Construction et entraînement du modèle
    model = build_model_pipeline()
    model.fit(X_train, y_train)

    # Prédictions sur l'ensemble de test
    y_pred = model.predict(X_test)
    
    # Affichage du rapport de classification
    print("\n=== Rapport de Classification ===")
    print(classification_report(y_test, y_pred))

    # Analyser avec le modèle ML
    predictions = model.predict(X)
    
    # Ajouter les prédictions aux résultats d'analyse
    for i, item in enumerate(results):
        item['ml_risk'] = 'CRITIQUE' if predictions[i] == 1 else 'ÉLEVÉ' if predictions[i] == 0 else 'NORMAL'
    
    print("\n=== Résultats de l'Analyse avec ML ===")
    for item in results:
        print(f"[{item['ml_risk']}] {item['principal']} ({item['role']})")
        print(f"  Raison : {item['reason']}")
        print(f"  ID : {item['id']}\n")