# 🛡️ Security Policy

<p align="center">
  <b>🏡 <a href="../README.md">Repository Home</a></b> • 📖 <a href="./README.md">Docs Overview</a> • 📁 <a href="../src/README.md">Source Packages</a> • <b>🛡️ Security Policy</b> • ✍️ <a href="./CONTRIBUTING.md">Contributing Guide</a>
</p>

---

Since these automation workflows connect directly to your live website, AI providers, and social accounts, **keeping credentials secure is our absolute priority**. 

Please read this policy to make sure you protect your API keys and accounts when using or editing these workflows.

---

## 🔒 Golden Rules of Safety

- **Never Commit Secrets:** Do not commit actual passwords, private tokens, or live API keys to this repository.
- **Use n8n Credentials:** Always use n8n's built-in credential management fields instead of hardcoding API keys in code or HTTP request headers.
- **Replace with Placeholders:** If you export a workflow from n8n to share, edit the JSON file first and replace any private names or values with uppercase placeholders (e.g. `ENTER_YOUR_API_KEY`).

---

## 📋 Safe Export Checklist

Before sharing your customized workflow files:
- [ ] No real API keys or tokens are in the JSON file.
- [ ] Account and username identifiers in settings or URLs are cleaned.
- [ ] Test data in the code nodes does not contain private customer info.
- [ ] No test links point to private sandbox or staging portals.

---

## 🚨 What to do if a Secret is Leaked?

If you accidentally commit a live secret:
1. **Change it immediately** at the provider (e.g., rotate your Gemini key, change your WordPress application password).
2. Delete the value from the file locally.
3. Clean your Git commit history to erase the secret from history.
4. Push the cleaned branch only after verifying it is safe.

---

## ✉️ Vulnerability Reporting

If you find a security bug or a leak, please **do not open a public issue**. Contact us privately:

- **Private Advisory:** [GitHub Security Advisory Portal](https://github.com/beydah/N8N-AI-Agent/security/advisories/new)
- **Direct Email:** `info.beydahsaglam@gmail.com`
