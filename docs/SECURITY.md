# Security Guide

[Back to Docs](./README.md) | [Back to Home](../README.md) | [Go Source](../src/README.md) | [Go Content Creator](../src/contect_creator/README.md) | [Go Lead Generator](../src/lead_generator/README.md) | [Go Contributing](./CONTRIBUTING.md)

These workflows connect to external APIs and publishing systems, so exported JSON files should be treated as configuration artifacts that can accidentally leak secrets if they are not cleaned before commit.

## Core Rules

- Never commit live API keys, tokens, or private IDs in `agent.json`.
- Prefer n8n credentials over inline values whenever possible.
- Replace exported secrets with placeholders such as `ENTER_YOUR_API_KEY`.
- Review the diff before every commit and before every push.

## Safe Export Checklist

- [ ] All API keys are placeholders.
- [ ] OAuth or account names in screenshots and examples are safe to publish.
- [ ] Test data does not expose private business or customer information.
- [ ] Links in README files do not point to private endpoints.

## If a Secret Was Committed

1. Rotate the secret at the provider immediately.
2. Remove the value from the current files.
3. Rewrite the affected git history if the secret was pushed.
4. Force-push the cleaned branch only after verifying the replacement commit.

## Vulnerability Reporting

Do not open a public issue for a security problem.

- Private report: [GitHub Security Advisory](https://github.com/beydah/N8N-AI-Agent/security/advisories/new)
- Email: `info.beydahsaglam@gmail.com`

## Related Documents

- [Back to Home](../README.md)
- [Go Docs](./README.md)
- [Go Contributing](./CONTRIBUTING.md)
