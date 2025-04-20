Idée de projet : Prédiction des conversions des visiteurs

✅ Objectif : Prédire si un visiteur d’un site e-commerce va acheter ou non
✅ Modèle : Classification (Random Forest)
✅ Approche :
- Exploration des données 📊 (Analyse des tendances)
- Nettoyage et prétraitement 🛠️ (Gestion des valeurs manquantes, normalisation)
- Feature Engineering 🔍 (Sélection des variables les plus pertinentes)
- Entraînement du modèle 🤖 (Test avec plusieurs algorithmes)
- Évaluation des performances 🎯 (Mesures de précision, recall, F1-score)

Ce dataset est lié aux comportements des visiteurs sur un site e-commerce,
avec des variables comme BounceRates, ExitRates, PageValues et Revenue.
Nous allons nous appuyer dessus pour pouvoir prédire si un utilisateur 
va effectuer un achat ou non en fonction de son comportement de navigation.


L'ensemble de données comprend 10 attributs numériques et 8 attributs catégoriels. 
L'attribut « Revenu » peut être utilisé comme étiquette de classe.
Les attributs « Administratif », « Durée administrative », « Informationnel », « Durée informative »,
« Lié au produit » et « Durée liée au produit » représentent le nombre de pages consultées par le visiteur
au cours de la session, ainsi que le temps total passé dans chacune de ces catégories.
Les valeurs de ces attributs sont dérivées des URL des pages consultées par l'utilisateur et mises à jour
en temps réel lorsqu'il effectue une action, par exemple en passant d'une page à une autre. 
Les attributs « Taux de rebond », « Taux de sortie » et « Valeur de page » représentent 
les indicateurs mesurés par Google Analytics pour chaque page du site e-commerce. 
La valeur de l'attribut « Taux de rebond » pour une page web correspond au pourcentage de visiteurs
qui accèdent au site depuis cette page, puis le quittent (« rebondissent ») 
sans déclencher d'autres requêtes auprès du serveur d'analyse au cours de la session.
La valeur de la fonctionnalité « Taux de sortie » pour une page web spécifique est calculée comme
le pourcentage de pages vues les plus récentes de la session, pour toutes les pages consultées.
La fonctionnalité « Valeur de la page » représente la valeur moyenne d'une page web consultée par
un utilisateur avant de finaliser une transaction e-commerce. La fonctionnalité « Jour spécial » 
indique la proximité de la consultation du site avec un jour spécial spécifique 
(par exemple, la fête des Mères ou la Saint-Valentin), où les sessions sont plus susceptibles
d'aboutir à une transaction. La valeur de cet attribut est déterminée en tenant compte de la dynamique
du e-commerce, comme le délai entre la date de commande et la date de livraison. 
Par exemple, pour la Saint-Valentin, cette valeur prend une valeur non nulle entre le 2 et le 12 février,
zéro avant et après cette date, sauf si elle est proche d'un autre jour spécial, et sa valeur maximale est
de 1 le 8 février. L'ensemble de données inclut également le système d'exploitation,
le navigateur, la région, le type de trafic, le type de visiteur (récurrent ou nouveau visiteur),
une valeur booléenne indiquant si la date de la visite est un week-end et le mois de l'année.