# Safety Scale (Demo Explanation)

## 🇬🇧 English

This demo uses a **simple safety scale from 1 to 10** to illustrate decision gating
before any USDC payment.

This scale is **not a real risk model**.
It is a **pedagogical abstraction** for hackathon purposes.

---

### Scale interpretation

- **1–5** → Low risk  
  Action is considered safe  
  → Payment allowed (demo mode)

- **6–10** → Elevated or ambiguous risk  
  Action is considered unsafe  
  → Payment blocked

---

### Why payments may differ between CLI and UI

- The **CLI demo** runs a predefined low-risk scenario (amount = 3)
  → Payment is allowed.

- The **UI demo** allows interactive values (1–10)
  → Payments above the threshold are intentionally blocked.

This difference is **intentional** and demonstrates the safety gate in action.

---

### Important note

This scale does **not** represent:
- a real financial risk engine
- a fraud detection system
- a production rule set

It is a **visual and conceptual tool** to show
how decision gating works before settlement.

---

## 🇫🇷 Français

Cette démo utilise une **échelle de sécurité simple de 1 à 10**
pour illustrer le contrôle décisionnel avant tout paiement USDC.

Cette échelle **n’est pas un vrai modèle de risque**.
Il s’agit d’une **abstraction pédagogique** utilisée pour le hackathon.

---

### Interprétation de l’échelle

- **1–5** → Risque faible  
  Action considérée comme sûre  
  → Paiement autorisé (mode démo)

- **6–10** → Risque élevé ou ambigu  
  Action considérée comme non sûre  
  → Paiement bloqué

---

### Pourquoi le paiement diffère entre la CLI et l’UI

- La **démo en ligne de commande (CLI)** exécute un scénario sûr prédéfini (montant = 3)
  → Paiement autorisé.

- La **démo UI** permet de choisir une valeur interactive (1–10)
  → Les valeurs au-dessus du seuil sont volontairement bloquées.

Cette différence est **volontaire** et montre le rôle de la barrière de sécurité.

---

### Note importante

Cette échelle ne représente **pas** :
- un moteur de risque réel
- un système anti-fraude
- des règles de production

C’est un **outil conceptuel** destiné à illustrer
le contrôle avant règlement.
