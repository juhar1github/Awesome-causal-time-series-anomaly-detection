Awesome Causal Time-Series Anomaly Detection
============================================

A curated collection of papers, official implementations, libraries, datasets, and benchmarks for causality-based time-series anomaly detection and root-cause analysis.

Scope
-----

This collection includes work where causality is central to at least one of the following:

1. Anomaly scoring or detection
2. Granger-causal or structural-causal graph discovery
3. Root-cause localization or intervention recognition
4. Causality-aware representation learning
5. Causal benchmarks for multivariate time series

The main list prioritizes official author repositories. A blank code cell means that no verified public implementation was located.

Papers
------

| Year | Method | Paper | Venue | Paper link | Code link | Main causal idea |
|---:|---|---|---|---|---|---|
| 2026 | CGT | Causally-Constrained Probabilistic Forecasting for Time-Series Anomaly Detection | arXiv | [Paper](https://arxiv.org/abs/2604.17998) | [Code](https://github.com/p-khn/CGT-V1) | Time-lagged causal graph masks a probabilistic forecasting model |
| 2026 | CAAD | CAAD: Causality-Aware Multivariate Time Series Anomaly Detection via Multi-Scale Alignment and Structural Causal Consistency | arXiv | [Paper](https://arxiv.org/abs/2607.08555) |  | Continuous verification of Granger-causal consistency |
| 2025 | AERCA | Root Cause Analysis of Anomalies in Multivariate Time Series through Granger Causal Discovery | ICLR | [Paper](https://openreview.net/forum?id=k38Th3x4d9) | [Code](https://github.com/hanxiao0607/AERCA) | Joint Granger causal discovery and intervention-based root-cause scoring |
| 2025 | CAROTS | Causality-Aware Contrastive Learning for Robust Multivariate Time-Series Anomaly Detection | ICML | [Paper](https://arxiv.org/abs/2506.03964) | [Code](https://github.com/kimanki/CAROTS) | Causality-aware contrastive representation learning |
| 2025 | causRCA | causRCA Dataset and Benchmarking Framework | Dataset and benchmark | Not available | [Code](https://github.com/causalgraph/causRCA) | Ground-truth causal structures and fault scenarios |
| 2025 | CGAD | Entropy Causal Graphs for Multivariate Time Series Anomaly Detection | ACM TIST | [Paper](https://arxiv.org/abs/2312.09478) | [Code](https://github.com/falihgoz/CGAD) | Transfer-entropy causal graph with graph and temporal convolutions |
| 2025 | RCAEval | RCAEval: A Benchmark for Root Cause Analysis of Microservice Systems with Telemetry Data | The Web Conference | [Paper](https://arxiv.org/abs/2412.17015) | [Code](https://github.com/phamquiluan/RCAEval) | Includes reproducible causal and graph-based RCA baselines |
| 2025 | GCAD | GCAD: Anomaly Detection in Multivariate Time Series from the Perspective of Granger Causality | arXiv | [Paper](https://arxiv.org/abs/2501.13493) |  | Dynamic gradient-based Granger-causality discovery |
| 2025 | OracleAD | Structured Temporal Causality for Interpretable Multivariate Time-Series Anomaly Detection | arXiv | [Paper](https://arxiv.org/abs/2510.16511) |  | Structured temporal causal modeling |
| 2024 | RUN | Root Cause Analysis in Microservice Using Neural Granger Causal Discovery | AAAI | [Paper](https://arxiv.org/abs/2402.01140) | [Code](https://github.com/zmlin1998/RUN) | Contrastive temporal encoder plus neural Granger discovery and personalized PageRank |
| 2023 | EasyRCA | Root Cause Identification for Collective Anomalies in Time Series given an Acyclic Summary Causal Graph with Loops | AISTATS | [Paper](https://arxiv.org/abs/2303.04038) | [Code](https://github.com/ckassaad/EasyRCA) | Causal graph, anomaly timing, d-separation, and direct-effect changes |
| 2023 | PyRCA | PyRCA: A Library for Metric-based Root Cause Analysis | arXiv / open-source library | [Paper](https://arxiv.org/abs/2306.11417) | [Code](https://github.com/salesforce/PyRCA) | Unified causal-graph construction and graph-based RCA methods |
| 2023 | CausalAD | A Causal Approach to Detecting Multivariate Time-Series Anomalies and Root Causes | ICLR | [Paper](https://arxiv.org/abs/2206.15033) |  | Detects violations of local causal mechanisms |
| 2022 | CIRCA | Causal Inference-Based Root Cause Analysis for Online Service Systems with Intervention Recognition | KDD | [Paper](https://arxiv.org/abs/2206.05871) | [Code](https://github.com/NetManAIOps/CIRCA) | Recognizes interventions through changes in conditional mechanisms |

Important copyright and license rule
------------------------------------

This repository links to external implementations. It does not copy or redistribute another author's code.

Before reusing an implementation:

1. Read the original repository's license
2. Preserve required copyright and license notices
3. Cite the associated paper
4. Mark unofficial implementations clearly
5. Do not redistribute code that has no reuse license

Quality labels
--------------

Use one of these code-status labels:

- Official
- Official resource
- Unofficial reproduction
- Code announced
- No official code located
- Link unavailable

Search keywords
---------------

causal time-series anomaly detection, multivariate time-series anomaly detection, Granger causality, causal discovery, structural causal model, root-cause analysis, intervention recognition, causal graph, AIOps, industrial monitoring

Disclaimer
----------

Metadata can change when preprints are accepted or repositories are released. Verify paper versions, venues, and licenses before reuse.
