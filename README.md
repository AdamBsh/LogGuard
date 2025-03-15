# LogGuard 🛡️

Un script python simple pour détecter les tentatives de connexion suspectes dans les fichiers logs.

## Pourquoi j'ai créé LogGuard

En tant qu'étudiant intéressé par la sécurité et les réseaux, j'ai voulu créer un outil simple qui montre comment :

1. Analyser des fichiers logs
2. Détecter simplement des activités suspectes (tentatives de connexions multiples)
3. Générer des rapports de sécurité

Ce projet m'a aidé à améliorer mes compétences en Python en l'appliquant à des sujets de sécurité.

## Structure du projet

```bash
LogGuard/
├── logguard.py          
├── sample_logs.txt 
└── README.md            
```

## Ce que fait LogGuard

LogGuard analyse les fichiers logs pour trouver les adresses IP qui ont fait trop de tentatives de connexion échouées (threshold). Cela peut indiquer une tentative d'attaque par force brute où quelqu'un essaie de deviner un mot de passe.

## Adaptation à différents systèmes d'exploitation

LogGuard peut facilement être adapté pour fonctionner avec différents systèmes d'exploitation :

- Linux : Modifier le code pour analyser les fichiers comme /var/log/auth.log qui contiennent généralement "Failed password for"
- macOS : Adapter pour les logs système accessibles via la commande log show
- Windows : Ajuster pour analyser les journaux d'événements de sécurité Windows

## Installation

```python
git clone https://github.com/AdamBsh/LogGuard.git
```

```python
python logguard.py sample_logs.txt 5
```

```text
===== LOGGUARD SECURITY REPORT =====
Analysis Date: 2025-03-15 15:45:32
File analyzed: sample_logs.txt
Alert threshold: 3 attempts

ALERT: 3 suspicious IP(s) detected!

IP: 192.168.1.101 - 4 failed login attempts
  First attempt: 2023-03-12 08:45:23
  Last attempt: 2023-03-12 08:45:23

IP: 192.168.1.100 - 3 failed login attempts
  First attempt: 2023-03-12 08:25:30
  Last attempt: 2023-03-12 08:30:10

IP: 192.168.1.210 - 3 failed login attempts
  First attempt: 2023-03-12 10:23:15
  Last attempt: 2023-03-12 10:27:10

Total IPs analyzed: 3
Total failed attempts: 10
```