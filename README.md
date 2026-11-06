# Harmattan Pay

A deliberately vulnerable fintech web app, built for learning offensive and defensive security.

> **WARNING: This application is intentionally insecure. Do NOT deploy it to the public internet or any shared network. Run it only on your own machine, in an isolated lab. It contains real, exploitable vulnerabilities on purpose.**

Harmattan Pay is a small mock mobile-money app with signup, login, a dashboard and a balance. It is modelled on training apps like DVWA: each feature can run in a vulnerable mode or a secure mode using a built-in security switch, so you can attack it, apply the fix, and confirm the attack fails.

## What it is for

Learning how web vulnerabilities work from both sides. How the flawed code creates the hole, how an attacker exploits it, and how the correct code closes it.

## Security levels

The Security Level page has two settings:
- **Low**: vulnerabilities are active and exploitable.
- **High**: the secure, fixed version of each feature.

Switch levels and re-run the same attack to see the difference.

## Vulnerabilities (growing list)

- SQL injection in the login, leading to authentication bypass.

More features and vulnerabilities are being added over time.

## Running it locally

Requires Python 3.

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python init_db.py
    python app.py

Then open http://127.0.0.1:5000 in your browser.

Seeded test accounts:
- catherine / harmattan123
- amaka / chelsea2020

## Disclaimer

This project is for education and authorised testing only. Only ever attack this app on a machine you own. Never use these techniques against systems you do not have explicit permission to test.
