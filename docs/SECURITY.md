# 🛡️ Security Policy
### Ensuring the Integrity of Your Autonomous Workflows

We take the security of the **N8N AI Agent Hub** seriously. Because these agents interact with sensitive external platforms (WordPress, LinkedIn, Search APIs), maintaining a secure configuration is paramount.

---

## 🔒 Security Architecture

Our modular design is built to minimize the "blast radius" of any potential compromise:
1. **Isolated Environments**: Each agent is a standalone workflow.
2. **Credential Decoupling**: We use n8n’s internal encrypted credential store rather than hardcoding keys.
3. **Pre-Publish Sanitization**: Logic is included to clean AI outputs before they reach public-facing APIs.

---

## 🚀 Secure Deployment Checklist

Before deploying this hub in a production environment, ensure:
- [ ] **HTTPS Only**: Your n8n instance must be behind a Reverse Proxy (Nginx/Traefik) with valid SSL.
- [ ] **Authentication**: Use **OAuth2** or **Strong Basic Auth** to restrict dashboard access.
- [ ] **Docker Hardening**: Run your n8n Docker container as a **non-root user**.
- [ ] **Firewall**: Restrict incoming traffic to only necessary ports (e.g., 443 for webhooks).

---

## 🔐 Secret Management Standards

To protect your API keys:
- **Environment Variables**: Store sensitive keys in your `.env` file, never in the workflow logic.
- **Workflow Placeholders**: When exporting agents as `.json`, check that all keys are replaced with `ENTER_YOUR_KEY`.
- **Git Safety**: Our `.gitignore` is configured to prevent `.env` and `*.json` (with keys) from being committed.

---

## 🚨 Reporting a Vulnerability

**Please do not open public issues for security vulnerabilities.**

If you discover a security-related issue, please report it via:
1. **Private Reporting**: Use the [GitHub Security Advisory](https://github.com/beydah/N8N-AI-Agent/security/advisories/new) feature.
2. **Direct Email**: Reach out to `info.beydahsaglam@gmail.com`.

### Our Commitment
- **Acknowledge**: Within 24 hours.
- **Triage**: Within 48 hours.
- **Resolution**: Timeline based on severity (Critical issues prioritized).

---
**Last Updated: April 2026**
