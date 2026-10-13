# cyber-service-outage-screening

Supplementary Material S1 for the paper **Screening cyber service outages in supply chains using flow bounds and timed recourse**.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23293162.svg)](https://doi.org/10.5281/zenodo.23293162)

**DOI:** [https://doi.org/10.5281/zenodo.23293162](https://doi.org/10.5281/zenodo.23293162)  
**GitHub release:** [cyber-service-outage-v1.0.0](https://github.com/chrisgilbertp/chrisgilbertp/releases/tag/cyber-service-outage-v1.0.0)  
**Zenodo record:** [https://zenodo.org/records/23293162](https://zenodo.org/records/23293162)

This repository folder contains the runnable code and documentation. The complete archive (including frozen network inputs, results, and figure sources) is available from the GitHub release and the Zenodo deposit above.

---

We evaluate cyber dispatch-service failures with a timed inventory model, operational screening measures, and exact small-controller protection problems. This archive contains the frozen inputs and computational evidence for **Screening cyber service outages in supply chains using flow bounds and timed recourse**. `Supplementary_Methods_S2.md` gives the extended definitions and results. `HISTORY.md` describes how the empirical record changed during revision.

## Reproduce the analysis

Use Python 3.11 or a compatible later release with the supplied package versions. From the extracted archive root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
bash run_all.sh
```

`run_all.sh` verifies frozen input hashes, discovers and runs the tests, executes all experimental phases, derives summaries, regenerates four figures, and refreshes the manifest. BLAS and OpenMP thread limits are one. The full calculation includes repeated 1024-node optimization and can take several minutes.

To rerun one phase:
```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/run_all.py --phase core
```
Replace `core` with `sensitivity`, `robustness`, `published`, `scaling`, or `witnesses`.

## Contents

| Location | Contents |
| --- | --- |
| `data/core` | 48 frozen synthetic inputs, archived nominal plans, three-node worked example |
| `data/extended` | Matched operating-condition inputs and scaling sizes |
| `data/published` | Sioux Falls topology and 12 synthetic cyber configurations |
| `code/model.py` | Timed recourse, outage windows, prerequisites, disposal |
| `code/metrics.py` | Static max flow, flow exposure, path decomposition, DPB certificate |
| `code/hardening.py` | Exact subset recourse and primary-failure hardening |
| `code/run_all.py` | Orchestrates all experimental phases |
| `results/` | Controller scores, associations, timings, summaries |

## Paper

**Screening cyber service outages in supply chains using flow bounds and timed recourse**

Keywords: cyber dependency; supply chain vulnerability; flows over time; network interdiction; inventory; hardening

## Citation

```text
chrisgilbertp. (2026). chrisgilbertp/chrisgilbertp: Cyber service outage screening – supplementary material S1 (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.23293162
```

Also available on GitHub: https://github.com/chrisgilbertp/chrisgilbertp/tree/main/cyber-service-outage-screening

## Licence

See `LICENSE` and `NOTICE.md` (third-party Sioux Falls topology terms). Zenodo deposit is under Creative Commons Attribution 4.0 International (CC BY 4.0).
