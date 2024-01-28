Cross-Validation and k-Nearest Neighbor Classification

Option 1. Study the KNeighborsClassifier class from the scikit-learn library. For the iris dataset, find the best combination of hyperparameters (n_neighbors, weights and metric) for the kNN classifier according to its F1-score of cross-validation. You do not have to check each combination manually. Use lists and for-loops. Also you can use the GridSearchCV to perform this subtask. 70 / 100 points

Le KNeighborsClassifier est un algorithme d'apprentissage supervisé utilisé pour la classification. Son fonctionnement est basé sur le principe que les points de données similaires devraient avoir des étiquettes similaires. Plus spécifiquement, voici comment fonctionne le KNeighborsClassifier :

1. Choix du nombre de voisins (k) : L'algorithme commence par fixer un nombre entier positif k, qui représente le nombre de voisins à prendre en compte lors de la prise de décision. Ce paramètre est spécifié lors de la création de l'instance du KNeighborsClassifier.
2. Entraînement : Lors de la phase d'entraînement, l'algorithme stocke simplement les exemples d'apprentissage dans la mémoire.
3. Prédiction : Lorsqu'un nouvel exemple doit être classifié, l'algorithme calcule la distance entre cet exemple et tous les exemples d'apprentissage. La distance peut être mesurée de différentes manières, comme la distance euclidienne.
4. Sélection des k voisins les plus proches : Les k exemples d'apprentissage ayant les distances les plus courtes par rapport au nouvel exemple sont sélectionnés.
5. Vote majoritaire : Pour un problème de classification, l'algorithme effectue un vote majoritaire parmi les étiquettes des k voisins sélectionnés. L'étiquette qui apparaît le plus souvent parmi les voisins est attribuée au nouvel exemple.

Cet algorithme est simple mais efficace dans de nombreuses situations, en particulier lorsque les frontières de décision sont relativement simples et que les données sont bien comportées. Cependant, il peut ne pas fonctionner aussi bien dans des cas où les frontières de décision sont complexes et non linéaires, ou lorsque les données sont bruitées.

Il est important de noter que le choix de la distance (euclidienne, manhattan, etc.) et du poids des voisins (uniforme ou pondéré) peuvent également influencer les performances du modèle, et ces options peuvent être spécifiées en tant que paramètres lors de la création de l'instance du KNeighborsClassifier.

Option 2. Try to implement K Nearest Neighbors classifier without the scikit-learn, For the iris dataset, find the best combination of hyperparameters (type of window, h or k, metric) for the kNN classifier according to its F1-score of cross-validation. You can use the GridSearchCV to perform this subtask. 100 / 100 points

Option 3*. Try to implement K Nearest Neighbors classifier with or without the scikit-learn, but for any multiclass dataset. You can use the GridSearchCV to perform this subtask. 150 / 100 points

For the best combination of parameters (weights and metric) found, build a plot of quality of classification as a function of the number of nearest neighbors.

https://en.wikipedia.org/wiki/Kernel_(statistics)
