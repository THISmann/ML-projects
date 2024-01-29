

Le Naive Bayes est un modèle de classification probabiliste basé sur la loi de Bayes. Il fait l'hypothèse simplificatrice selon laquelle tous les attributs sont indépendants les uns des autres, ce qui facilite considérablement l'application de la loi de Bayes. Voici comment l'algorithme de Naive Bayes fonctionne :

1. **Échantillonnage des données** : Le premier pas consiste à échantillonner les données et à séparer les variables indépendantes (features) des variables dépendantes (cibles). Dans le cas du jeu de données Iris, les features sont les caractéristiques physiques des fleurs (longueur de sépale, largeur de sépale, longueur de pétale et largeur de pétale), tandis que la cible est la catégorie de la fleur (setosa, versicolor ou virginica).
2. **Estimation des probabilités conditionnelles** : Pour chaque feature et chaque classe, le Naive Bayes estime les probabilités conditionnelles P(C|F) et P(F|C), où C est la classe et F est la feature. Ces estimations peuvent être réalisées en analysant les fréquences des différents éléments dans les données. Par exemple, si la longueur de sépale varie entre 4.9 cm et 6.9 cm pour les fleurs setosas, alors P(Setosa | Longueur de sépale > 5.5 cm) sera faible car cette longueur ne se trouve pas dans cet intervalle.
3. **Classification** : Lorsqu'un nouveau sample doit être classifié, le Naive Bayes calcule les probabilités conditionnelles P(C|F) pour chaque classe et chaque feature. Ensuite, il multiplie ces probabilités ensemble pour obtenir la probabilité totale de chaque classe. Finalement, il choisit la classe avec la probabilité totale la plus élevée comme étant la classe du sample.

Voici un exemple simple de calcul de probabilité conditionnelle pour illustrer le principe :

Supposez que nous avons deux features A et B, et trois classes C1, C2 et C3. Nous voulons calculer P(A=a | C=c), où a est une valeur possiblement différente pour A, et c est une valeur possiblement différente pour C.

La loi de Bayes stipule que P(A=a | C=c) = P(C=c | A=a) * P(A=a) / P(C=c)

Dans le cas du Naive Bayes, nous faisons l'hypothèse que les features sont indépendantes, donc P(A=a & B=b | C=c) = P(A=a | C=c) * P(B=b | C=c)

Il est important de noter que cette hypothèse simplificateuse peut entraîner des erreurs lorsque les features sont corrélées. Malgré cela, le Naive Bayes reste un modèle efficace et facile à implémenter pour de nombreux problèmes de classification.



![img](https://avatars.mds.yandex.net/i?id=0a2b43f043006d20f3ccbb0ce5300830-4408158-images-thumbs&n=13)

![](https://avatars.mds.yandex.net/i?id=212b2993bbd9be2aca526f3900ee9db4f14ca741-9867831-images-thumbs&n=13)
