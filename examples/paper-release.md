# 📄 Academic Paper Release Archetype (`paper-release`)

## Target Audience
- **AI/Physics Researchers & Peer Reviewers**.
- **Core Principle**: **Zero cognitive overhead**. Single-command replication.

## Before Reorganization
```
paper-code/
├── README.md
├── eval_script.py
├── train_script.py
├── model_v1.py
├── model_v2_final.py
├── plot1.png
├── plot2.png
├── checkpoint_epoch_10.pt
└── test_logs.txt
```

## After Reorganization (Minimal Friction)
```
paper-code/
├── README.md                  # Abstract, Paper link, 1-line reproduction command
├── LICENSE
├── requirements.txt
├── run_eval.py                # Flat 1-command evaluation script
├── src/                       # Core model & loss definitions
│   └── model.py
├── weights/                   # Pretrained model checkpoints
│   └── model_final.pt
├── scripts/                   # Multi-GPU training shell scripts
│   └── train_distributed.sh
└── figures/                   # Paper plots
    ├── figure1_architecture.png
    └── figure2_benchmark.png
```
