L'algorithme de régression linéaire est un algorithme d'apprentissage supervisé utilisé pour modéliser la relation linéaire entre une variable dépendante (cible) et une ou plusieurs variables indépendantes (caractéristiques). Voici comment fonctionne l'algorithme de régression linéaire de manière générale et comment vous pouvez l'utiliser en Python avec la bibliothèque scikit-learn.

### Fonctionnement de l'Algorithme de Régression Linéaire:

1. **Formulation du Modèle:**

   * L'idée de base est de modéliser la relation entre la variable dépendante **y** et les variables indépendantes **X** comme une équation linéaire. Pour une régression linéaire simple, l'équation prend la forme  **y**=**m**x+b, où **m** est la pente (coefficient) et **b** est l'ordonnée à l'origine.
2. **Entraînement du Modèle:**

   * L'algorithme ajuste les coefficients (**m** et **b**) du modèle de manière à minimiser l'erreur quadratique moyenne (Mean Squared Error - MSE) entre les prédictions du modèle et les valeurs réelles de la variable dépendante dans l'ensemble d'entraînement.
3. **Calcul des Coefficients:**

   * Les coefficients sont calculés à l'aide de techniques telles que la méthode des moindres carrés, qui minimise la somme des carrés des écarts entre les valeurs prédites et les valeurs réelles.
4. **Prédiction:**

   * Une fois que le modèle est entraîné, il peut être utilisé pour faire des prédictions sur de nouvelles données en utilisant la relation linéaire apprise pendant l'entraînement.

![img](https://i2.wp.com/miro.medium.com/1*CjTBNFUEI_IokEOXJ00zKw.gif)
