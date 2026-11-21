# The developing paper

- [Read the PDF](main.pdf).
- [Main TeX file](main.tex).
- [Mathematical sections](sections/).

The manuscript contains proved analytic reductions and explicitly conditional comparisons with the quasi-RH methods. It is **not yet a complete proof of GRH**. The unresolved arithmetic estimates are collected in the final section, and the separate source audit records what has actually been inspected.

Build from the repository root with:

```sh
python3 scripts/build_paper.py
```

This uses pdfLaTeX, stabilizes cross-references, rejects undefined references and overfull boxes, and writes `certificates/paper-build.json` with the source and output hashes. It makes no network requests. A normal TeX installation needs the standard AMS, geometry, Latin Modern, microtype, and hyperref packages. A local fallback supports an already installed TeX tree whose generated format or filename database is missing.

The paper is organized by mathematical dependence. Recovery records and source-code details belong outside it. When adding a result, update the exposition where that result is needed, rather than appending a chronological entry.
