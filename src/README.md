# 📁 Source Packages

<p align="center">
  <b>🏡 <a href="../README.md">Repository Home</a></b> • 📖 <a href="../docs/README.md">Documentation Hub</a> • <b>📁 Source Packages</b> • 🛡️ <a href="../docs/SECURITY.md">Security Policy</a> • ✍️ <a href="../docs/CONTRIBUTING.md">Contributing Guide</a>
</p>

---

This directory houses the workflow packages available for import into your n8n workspace. To maintain a clean, modular repository layout, each package resides in its own folder and contains its sanitized JSON configuration next to its setup documentation.

---

## 🗺️ Directory Architecture

The source folders are organized as follows:

```mermaid
graph TD
    Source["📁 src/ Source Root"] --> Content["✍️ contect_creator/"]
    Source --> Blogger["🤖 wordpress_blogger/"]
    Source --> Leads["🎯 lead_scraper/"]

    Content --> ContentJson["agent.json (Workflow)"]
    Content --> ContentReadme["README.md (Guide)"]
    Blogger --> BloggerJson["agent.json (Workflow)"]
    Blogger --> BloggerReadme["README.md (Guide)"]
    Leads --> LeadsJson["agent.json (Workflow)"]
    Leads --> LeadsReadme["README.md (Guide)"]
```

---

## 📦 Package Catalog

| Package Name | Contents | Description | Integrations |
| :--- | :--- | :--- | :--- |
| **✍️ [Content Creator](./contect_creator/README.md)** | `agent.json`, `README.md` | Generates article drafts, cover image prompts, and schedules publishing resources. | n8n, Gemini AI, WordPress, LinkedIn, Google Drive |
| **🤖 [WordPress Blogger](./wordpress_blogger/README.md)** | `agent.json`, `README.md` | Periodically parses tech feeds, writes SEO-friendly articles, drafts voxel cover art, and posts. | n8n, Gemini AI, RSS Feeds, WordPress REST API |
| **🎯 [Lead Scraper](./lead_scraper/README.md)** | `agent.json`, `README.md` | Gathers local business info, runs deduplication logic, and logs unique leads. | n8n, Google Maps & Places APIs, Google Sheets |

---

## 📥 How to Import a Workflow

1. Click on the package name from the catalog table above.
2. Review its credential requirements and database schema setup details.
3. Download the `agent.json` file.
4. Go to your **n8n instance** dashboard.
5. Create a new workflow, click **Import from File**, and select the downloaded `agent.json` file.
6. Configure your custom API keys, toggle the workflow state to **Active**, and start running!

---

> [!NOTE]
> *Note on directory naming:* The folder name `contect_creator` has been preserved to prevent breaking references in existing automation endpoints.
