# 🏆 Competition & Research Archetype (`competition-research`)

## Target Audience
- **Competition Judges**: Want `.docx` / PPT deliverables at specific paths.
- **Technical Reviewers**: Want methodology logbooks (`LOGBOOK.md`).
- **General Scientists / Developers**: Want single CLI runner (`main.py --mode full`).

## Before Reorganization (Messy Root)
```
my-competition-repo/
├── README.md
├── main.py
├── simulator.py
├── agent.py
├── figure1.png
├── figure2.png
├── exploratory_log.csv
├── scientific_signals.json
├── 开放探索赛初赛问题定义文档_filled.docx
├── 问题定义文档_v2_重写版.docx
├── Datawhale_AI4Research_Final_Report_v1.1.0.docx
├── Econophysics_preliminary.pptx
├── .~lock.DOCX#
└── __pycache__/
```

## After Reorganization (Clean Hub)
```
my-competition-repo/
├── README.md                  # Quick navigation + embedded visual results
├── LICENSE
├── requirements.txt
├── main.py                    # Unified CLI runner
├── src/                       # Core python package
│   ├── simulator.py
│   └── agent.py
├── docs/                      # Multi-audience documentation hub
│   ├── README.md              # Guide explaining doc folders
│   ├── submission/            # Official deliverables for judges
│   │   ├── 01_初赛问题定义文档_v2.docx
│   │   └── 02_Final_Report.docx
│   ├── logbook/               # Research trajectory & iteration logs
│   │   └── LOGBOOK.md
│   └── references/            # Background PDFs, PPTs, templates
│       └── Econophysics_preliminary.pptx
├── outputs/                   # Figures & data logs
│   ├── README.md              # Figure & schema index
│   ├── figure1.png
│   ├── figure2.png
│   ├── exploratory_log.csv
│   └── scientific_signals.json
└── notebooks/                 # Interactive Jupyter demos
    └── demo.ipynb
```
