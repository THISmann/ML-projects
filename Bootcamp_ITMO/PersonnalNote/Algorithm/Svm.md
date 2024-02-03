

L'algorithme Support Vector Machine (SVM) est un outil de classification supervisée qui cherche à maximiser la marge entre les hyperplanes séparateurs des classes. Cette méthode permet de classer des données multidimensionnelles en utilisant des hyperplanes linéaires ou non linéaires. Voici comment l'algorithme de SVM fonctionne :

1. **Transformation des données** : Si les données sont non linéaires, elles doivent être transformées en un espace de haute dimension où elles deviennent linéairement séparables. La transformation est effectuée par un kernel function, tel que la fonction de kernel radial basis function (RBF).
2. **Calcul des marges** : Les marges sont les distances entre les points les plus proches des hyperplanes séparateurs et les hyperplanes eux-mêmes. Plus grande est la marge, mieux la classification est.
3. **Optimisation du paramètre C** : Le paramètre C contrôle le trade-off entre la précision de la classification et la taille des marges. Plus grand est C, moins grandes seront les marges, mais plus précise sera la classification.
4. **Training** : L'objectif est de trouver les hyperplanes séparateurs optimaux qui maximisent les marges. Cela est accompli en minimisant la somme des distances aux hyperplanes pour toutes les données.
5. **Prédiction** : Lorsqu'une nouvelle donnée doit être classifiée, elle est projetée dans l'espace de haute dimension grâce au kernel function. Ensuite, elle est classifiée en fonction de la côté de l'hyperplan séparateur qu'elle appartient.

L'avantage principal de SVM est sa capacité à gérer les données non linéaires et ses performances excellentes même avec des données imbalancées. Cependant, il peut être sensible

![img](https://machinelearningmastery.ru/img/0-875815-724259.gif)

![Formulating the Support Vector Machine Optimization Problem – Math ∩  Programming](https://jeremykun.com/wp-content/uploads/2017/06/svm_solve_by_hand-e1496076457793.gif)
