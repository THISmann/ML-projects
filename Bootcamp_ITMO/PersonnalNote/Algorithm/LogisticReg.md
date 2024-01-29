

La régression logistique est un modèle de classification qui utilise une fonction sigmoïde pour prédire les probabilités d'appartenance à chaque classe. Voici comment l'algorithme de régression logistique fonctionne :

1. **Échantillonnage des données** : Le premier pas consiste à échantillonner les données et à séparer les variables indépendantes (features) des variables dépendantes (cibles). Dans le cas du jeu de données Iris, les features sont les caractéristiques physiques des fleurs (longueur de sépale, largeur de sépale, longueur de pétale et largeur de pétale), tandis que la cible est la catégorie de la fleur (setosa, versicolor ou virginica).
2. **Calculation des coefficients** : L'objectif de la régression logistique est de calculer les coefficients beta (β) de la ligne droite équivalente au modèle linéaire. Pour ce faire, elle utilise une méthode itérative appelée gradient descent, qui minimise la fonction de perte entre les prédictions et les valeurs réelles. Les coefficients beta représentent l'impact de chacune des features sur la probabilité d'appartenance à chaque classe.
3. **Prédiction des probabilités** : Une fois les coefficients beta calculés, la régression logistique peut être utilisée pour prédire les probabilités d'appartenance à chaque classe en utilisant la formule suivante : 

   $$
   P(\text{Y}=k|\mathbf{x})=\frac{\exp\left(\sum_{j=1}^{J}\beta_{jk}x_{j}+\beta_{0k}\right)}{\sum_{m=1}^{M}\exp\left(\sum_{j=1}^{J}\beta_{jm}x_{j}+\beta_{0m}\right)}
   $$

   , où Y est la variable cible, 

   $$
   \mathbf{x}
   $$

    est la matrice des features, J est le nombre total de features, M est le nombre total de classes, 
   $$
   \beta
   $$

    est le vecteur des coefficients beta et 
   $$
   \beta_{0}
   $$

    est le terme constant. Cette formule calcule la probabilité de chaque classe en comparant les scores de probabilité pour toutes les classes.
4. **Classement final** : Enfin, la régression logistique effectue un classement final en choisissant la classe avec la plus grande probabilité. Si plusieurs classes ont la même probabilité maximale, il est possible qu'il y ait une erreur dans les données ou que la distinction entre ces classes soit difficile.

En résumé, la régression logistique est un modèle de classification basé sur une fonction sigmoïde qui permet de prédire les probabilités d'appartenance à chaque classe en utilisant les coefficients beta obtenus par gradient descent. Elle est souvent utilisée pour analyser des données binaires ou multinomiales et peut être adaptée aux besoins spécifiques grâce à ses options de paramétrage.



![img](https://i.pinimg.com/originals/76/6e/99/766e99697e5fb929ae56f3380ecfaf72.jpg)
