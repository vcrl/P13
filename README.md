# Outil de gestion - Salon de Toilettage - Super Toutous

Cet outil est le résultat d'une recherche approfondie sur le métier de toiletteur. Il permet aux propriétaires de salons de toilettage de gérer leur clientèle, leur rendez-vous, mais également leurs revenus et les races prises en charges dans leur boutique.

Ce panel administratif a pour objectif d'être simple, droit-au-but et intuitif pour pouvoir être utilisé par quiconque.

Grâce à un système d'authentification et de gestion administratif, les chefs d'entreprises pourront gérer leurs employés directement sur l'application et posséderont des identifiants spécifiques leur permettant d'avoir un accès privilégié à leur plateforme de gestion.

L'application est développée en Python avec Django.

## Spécificités et Utilisations

### Authentification
Les administrateurs se verront prescrire des identifiants personnels et privés qui leur permettra d'accéder à toutes les fonctionnalités de l'application. En effet, si aucun utilisateur n'est connecté, la plateforme est inaccessible et une page de connexion s'ouvre à chaque tentative d'accès à différentes pages.
Ainsi, une première connexion est obligatoire.
![alt text](https://dev.vruel.fr/p13/login.png)

### Accueil
La page d'accueil se veut être un résumé de la situation de l'entreprise. Les utilisateurs y verront le nombre de clients réguliers (rubrique: clients inscrits), le chiffre d'affaire réalisé pendant le mois actuel (rubrique: réalisés ce mois-ci, le bénéfice est affiché sous forme net), les races toilettées et prises en charges par l'entreprise (rubrique: races toilettées), ainsi que les rendez-vous planifiés (rubrique: rendez-vous planifiés).

Cette vue d'ensemble vise à faciliter la tâche des utilisateurs en affichant l'information la plus utile dès la première connexion sur l'application.
![alt text](https://dev.vruel.fr/p13/dashboard.png)

### Gestion des employés
Les utilisateurs pourront ajouter des employés à l'application, en renseignant leurs informations personnelles ainsi que leur date de recrutement dans le but de faciliter, pour le chef d'entreprise, la gestion des recrutements.
/!\ Un employé doit absolument être enregistré avant l'ajout d'un client. En effet, chaque client se voit attitré un toiletteur favoris lors de l'inscription.
![alt text](https://dev.vruel.fr/p13/employés.png)

### Gestion des rendez-vous
Les rendez-vous sont affichés sous forme de liste pour permettre à l'adminitrateur de garder une trace précise de chaque élement d'un rendez-vous (nom du client, nom du toiletteur, revenu estimé, temps de réalisation du service, commentaire).
Les rendez-vous sont triés de sorte que les plus imminents soient affichés en haut de la liste, ce qui permet, là aussi, une meilleure vision générale des rendez-vous et une meilleure organisation, l'objectif étant de simplifier au maximum l'utilisation de l'application.
![alt text](https://dev.vruel.fr/p13/rdv.png)

### Gestion des revenus
Pour chaque rendez-vous créé sur l'application, deux options d'offrent aux utilisateurs :
- Encaissement,
- Suppression
L'option encaissement permet d'information l'application que ce rendez-vous a bien été pris en compte et réalisé en temps voulu. Ainsi, les revenus du rendez-vous seront calculés automatiquement, la TVA sera déduite du prix final, et ceux-ci se verront être ajouté au bilan mensuel et/ou annuel disponible dans la rubrique "Revenus".
Les pages de bilan ont été simplifié au maximum pour permettre une impression rapide de ceux-ci ainsi qu'une lisibilité facilitée des revenus.
![alt text](https://dev.vruel.fr/p13/revenus.png)

## Réponse aux besoins
Pour réaliser cette application, je me suis rensigné auprès d'un salon de toilettage de ma ville pour me permettre de cibler les besoins que pourraient avoir ces toiletteurs s'ils étaient mes clients et fonction de cette liste, j'ai établi un listing des fonctionnalités qui pourraient êtres implémentés efficacement.
Ainsi, certaines fonctionnalités comme celle d'ajouter indivuellement les animaux indépendemment de leurs propriétaires sur l'application vient directement d'une suggestion d'un toiletteur que j'ai rencontré. En effet, il leur est parfois plus facile d'idenfitifer un client par le nom et la race du chien que par celui du client lui-même ! Ceci peut se comprendre de leur point de vue, mais si je ne m'étais pas renseigné auprès d'eux, cette fonctionnalité m'aurait très probablement échappé, d'où l'importance de ma démarche.
Je considère donc mon application comme répondant au maximum aux besoins d'une profession spécifique.

## Développement
Inspiré par les pratiques de l'exTreme Programming, j'ai essayé, au maximum, de mettre en place ces principes dans la conception et le développement de mon application pour me permetttre d'adopter des manières de coder efficaces.

La réalisation de tests unitaires à hauteur de 85% me permet d'avoir un contrôle total sur mon application, et je peux ainsi ajouter ou retirer toute fonctionnalité sans compromettre l'application dans son entièreté.

En considérant les bonnes pratiques de développement avec Django, chaque fonctionnalité du site est séparée en une application Django différente. La gestion d'authentification, les rendez-vous, les clients ou la gestion des revenus : toutes ces fonctionnalités sont gérées de manière indépendantes dans une application respesctive possédant une plage de tests individualisée.

## Conclusion

J'estime avoir beaucoup appris de la réalisation d'une application censée réponse à un besoin spécifique. En effet, plusieurs fonctionnalités qui me paraissaient logique aux premiers abords n'avaient en fait aucune utilité dans l'objectif final de mon projet (répondre aux besoins d'un salon de toilettage).

Cette immersion dans un projet de développement professionnel m'a donné une indication de ce dans quoi je m'engageais à l'avenir, et bien que plusieurs axes d'améliorations sont possibles, j'ai eu le goût d'une expérience enrichissante et motivante.
