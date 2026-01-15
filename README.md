# Agentic Commerce — Safe USDC Payments (Arc)

## 🇬🇧 English

### What is this project?

This project is a **research and hackathon demo** exploring a simple but critical question:

> **How can AI agents pay in USDC without making unsafe or irrational decisions?**

Instead of focusing on *how fast* an agent can pay, this demo focuses on **when an agent should NOT pay**.

---

### Core idea

In agentic commerce, AI agents may soon pay for APIs, compute, data, and digital services.
The main risk is not technical execution, but **automated money movement without judgment**.

This demo introduces a **safety gate** between:
```
Agent intent → USDC payment
```

If the action is safe, payment is allowed.  
If the action is unsafe or ambiguous, payment is blocked.

---

### Architecture overview

```
Agent → Safety Gate → Arc USDC Settlement (mocked)
```

The payment layer is intentionally mocked to avoid real fund movement and focus on decision logic.

---

### What this demo is (and is not)

✅ A conceptual safety pattern  
❌ Not a production payment system

---

### How to run

```bash
python demo/run_demo.py
streamlit run ui/app.py
```

---

### Hackathon context

Designed for the **Arc + Circle Agentic Commerce Hackathon**.

---

### Disclaimer

Research demo only. No real funds. Not production-ready.

---

### Intellectual Property & Usage Notice

This repository contains a **demonstration and conceptual prototype**.
Underlying decision logic and advanced safety systems remain proprietary and are not disclosed.
Reuse or production deployment requires explicit authorization.

---

## 🇫🇷 Français

### De quoi s’agit-il ?

Ce projet est une **démo de recherche / hackathon** répondant à une question clé :

> **Comment permettre à des agents IA de payer en USDC sans prendre de décisions dangereuses ?**

La démo montre **quand un agent ne doit pas payer**, plutôt que comment payer vite.

---

### Idée centrale

Le risque n’est pas technique mais décisionnel.
Une **barrière de sécurité** est placée avant tout paiement USDC.

---

### Architecture

```
Agent → Barrière de sécurité → Paiement USDC Arc (simulé)
```

---

### Ce que cette démo est (et n’est pas)

✅ Un prototype conceptuel  
❌ Un système de paiement réel

---

### Lancer la démo

```bash
python demo/run_demo.py
streamlit run ui/app.py
```

---

### Propriété intellectuelle & conditions d’usage

Ce dépôt contient une démo conceptuelle.
Les mécanismes avancés restent propriétaires et non divulgués.
Toute réutilisation ou déploiement en production nécessite une autorisation explicite.
