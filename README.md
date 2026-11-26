# Victorian ED Flow

Which part of emergency care should a service review first? In 2025–26 the proportion of ED visits under four hours was 25.2 percentage points below target, the largest gap of four monitored Victorian standards.

Open **index.html** in a browser. It runs offline. For GitHub Pages, publish the branch containing these files from its root directory.

- **data/annual-results.csv** — eight published annual observations with source links.
- **docs/ba/** — business case through glossary, including requirements, tests and traceability.
- **docs/Business_Analysis.docx** — formatted BA pack.
- **tests/check_register.py** — run `python tests/check_register.py` from the repository to verify the register and headline calculations.
- **social/** — LinkedIn draft, two figures and image descriptions.

The annual measures cover different patient groups. Hospital-level delay, causes and service impact need local records. Educational portfolio project. Not clinical advice.

Author: Gaurav Warke. Source publications retain their original terms. A licence for the original project files has yet to be selected.

## GitHub setup

Suggested repository name: `victorian-ed-flow`

Description: Victorian emergency department performance across four time standards, with public source data and reproducible checks.

1. Create an empty public repository and extract this package locally. Keep index.html at the top level.
2. From the extracted directory, run the commands below. Replace YOUR-ACCOUNT with the GitHub account that owns the empty repository.

```sh
python tests/check_register.py
git init -b main
git add .
git commit -m "Publish Victorian ED Flow dashboard and evidence pack"
git remote add origin https://github.com/YOUR-ACCOUNT/victorian-ed-flow.git
git push -u origin main
```

3. In repository Settings > Pages, select Deploy from a branch, choose main and /(root), then Save.
4. Once deployed, open Visit site, check all four views and download the register. Add the verified site URL to the repository About field and the LinkedIn post.

[GitHub Pages publishing instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
