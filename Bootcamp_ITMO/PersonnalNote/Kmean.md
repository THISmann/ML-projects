

L'algorithme de k-méans fonctionne selon les étapes suivantes :

1. **Initialisation** : On choisit initialement k points aléatoires dans l'espace des données pour servir de centres initiaux. Ces points sont appelés "centroïdes".
2. **Attribuer chaque point à un centre** : Pour chaque point dans les données, on détermine quel centroïde est le plus proche en distance euclidienne. Le point est alors attribué au groupe associé à ce centroïde.
3. **Mettre à jour les centroïdes** : Pour chaque groupe formé, on calcule la position du nouveau centroïde en prenant la moyenne des positions des points appartenant au groupe. Les nouveaux centroïdes ainsi obtenus remplacent les anciens centroïdes.
4. **Répéter les étapes 2 et 3** : On reprend les étapes 2 et 3 jusqu'à ce qu'aucun point ne change de groupe ou jusqu'à ce qu'on atteigne un certain nombre d'itération maximum.
5. **Affecter chaque point au groupe le plus proche** : Enfin, on affecte chaque point à son groupe le plus proche en distance euclidienne parmi les nouveaux centroïdes calculés.

Le but de l'algorithme de k-méans est de trouver un partitionnement optimal des données en k groupes, où chaque groupe est représenté par un centroïde. La qualité de cette partitionnement est généralement évaluée grâce à la distance entre les points et leurs centroïdes, ou encore par l'analyse de la silhouette des points.



![img](https://sandipanweb.files.wordpress.com/2017/03/wkmeans3.gif?w=676)

![](https://upload.wikimedia.org/wikipedia/commons/7/7b/Kmeans_animation_withoutWatermark.gif)
