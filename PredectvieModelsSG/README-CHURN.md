##### **OBJECTIF:**

L'objectif du mod&#232;le pr&#233;dictif de la pr&#233;-attrition est d'anticiper la tomb&#233;e en inactivit&#233;  d'un client. Cela permet ainsi au charg&#233; de client&#232;le de prioriser ses prises de contact pour renouer avec le client et chercher ainsi &#224;  revaloriser et renforcer la relation.


##### **D&#200;FINITION:**

- Un client pr&#233;-attritioniste selon le mod&#232;le pr&#233;dictif est un client actif qui a effectu&#233; au moins une transaction durant le mois M, et qui risque de faire < 3 op&#233;rations dans les mois M+1, M+2, M+3 et M+4;

- Cette d&#233;finition se base sur les usages et le mode de consommation des produits de la banque par le client. Elle int&#232;gre les principales op&#233;rations de caisse en agence (Versement, retrait, remise/&#233;mission ch&#232;que, virement &#233;mis…), les op&#233;rations de carte (Achat et retrait) et les op&#233;rations via l'application mobile (Paiement facture, virement compte &#224; compte, virement, recharge, mise &#224; disposition) 
- Cette d&#233;finition apporte une vision globale et multicanale sur l'interaction du client avec la banque;
- Pour identifier les clients pr&#233;-attritioniste, le mod&#232;le pr&#233;dictif se base sur les techniques de Machine Learning pour analyser le comportement de ces clients en &#233;tudiant plusieurs variantes : Equipement, &#233;volution des mouvements cr&#233;diteurs et d&#233;biteurs, le PNB, le solde; 
>
> Ce mod&#232;le a fait l'objet d'un travail de recalibrage en T2-22 pour am&#233;liorer l'efficacit&#233; pr&#233;dictive du mod&#232;le;
>
##### **SCOPE:**

* Client&#232;le CLIPRI.
>
##### **VOLUMETRIE:**

| Output du use case*| Output du mod&#232;le avec filtre m&#233;tier** | Fr&#233;quence | Canal    |  
| -------------     |:-------------------------------------:| -----------------:|---------:|
| ~ 8K clients      | ~ 5K clients                          | Chaque 4 mois     | LCP/INTAJ|

> *Ce seuil peut etre param&#233;tr&#233; selon la note du score &#224; d&#233;finir ou Top clients &#224; contacter.
>
> **Segment &#224; forte valeur, non MRE, exclusion de CSP &#224; faible valeur, CCH ouvert, M&#224;J des donn&#233;es d'activit&#233;.
