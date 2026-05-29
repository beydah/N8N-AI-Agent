# 🛡️ Security Policy

<p align="center">
  <b>🏡 <a href="../README.md">Repository Home</a></b> • 📖 <a href="./README.md">Docs Overview</a> • 📁 <a href="../src/README.md">Source Packages</a> • <b>🛡️ Security Policy</b> • ✍️ <a href="./CONTRIBUTING.md">Contributing Guide</a>
</p>

---

Because these automation workflows connect directly to your live websites, database entries, AI providers, and social accounts, **credential security is our absolute priority**.

Please follow this policy to safeguard your API keys, credentials, and user data when deploying or updating workflows.

---

## 🔒 Safety Guidelines

* **No Committed Secrets:** Do not commit passwords, API keys, or active account credentials to Git history.
* **Leverage n8n Credentials:** Always use n8n's dedicated built-in credential manager instead of placing keys directly in headers or request body nodes.
* **Sanitize Exports:** If exporting a custom workflow for sharing, inspect the JSON structure and replace personal tokens or private links with uppercase placeholders (e.g. `ENTER_YOUR_API_KEY`).

---

## 📋 Pre-Commit Checklist

Verify the following before contributing or sharing workflow files:
- [ ] Raw API keys, tokens, or app passwords have been removed.
- [ ] Custom domain usernames or profile slugs in settings and URLs have been sanitized.
- [ ] Test parameters in the code block nodes do not contain private customer data.
- [ ] Staging links and Sandbox webhook endpoints have been replaced with generic placeholders.

---

## 🚨 Security Incident Handling

If you accidentally commit an active credentials secret:
1. **Rotate the Secret Immediately:** Deauthorize the exposed API key or credential at the provider side (e.g. Google AI Studio, WordPress site administrator dashboard).
2. Remove the active string value from the file locally.
3. Rewrite the git commit history to purge the credential from previous history.
4. Push the cleaned branch only after verifying it is sanitized.

---

## ✉️ Vulnerability Reporting

If you locate a security leak or vulnerability in the repository, please **do not open a public issue**. Proactively open a secure report:

* **Private Advisory:** Propose a report using the [GitHub Security Advisory Portal](https://github.com/your-github-repo/security/advisories/new)
* **Direct Contact:** Contact the repository maintainers directly via security email.
