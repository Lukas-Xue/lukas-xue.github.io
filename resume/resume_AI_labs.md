# Renhao (Lukas) Xue

**ML / Research Engineer · LLM Post-Training & Inference**
Seattle, WA · lukas.rxue@gmail.com · 470-775-1452 · [lukasxue.com](https://lukasxue.com) · {{icon:github|https://github.com/Lukas-Xue}} {{icon:linkedin|https://www.linkedin.com/in/lukas-xue/}} {{icon:scholar|https://scholar.google.com/citations?user=oaIhxugAAAAJ&hl=en}}

---

## Experience

**Amazon Web Services, Generative AI Innovation Center** · Seattle, WA
**Machine Learning Engineer II, Custom Model Optimization** · *May 2025 – Present*

- Post-trained foundation models **up to 30B parameters** (Qwen3, Llama 3.1, Nova 2 Lite; text and vision-language) with SFT, DPO, and GRPO — from single-GPU LoRA (Unsloth) to distributed SageMaker HyperPod runs on 8×H200 and 8×A100 clusters — shipping custom models to enterprise production.
- Fine-tuned **Nova 2 Lite** (VLM) for document understanding (classification, key-information extraction, packet splitting) via single-phase shuffled-heavy fine-tuning: **matched Claude Sonnet 4.5 quality at ~1/10 the inference cost**, with 2× ordered-split accuracy and 96% page classification on shuffled multi-page PDFs.
- Built distributed multi-node/multi-GPU training and inference for a single-cell foundation model at a premier research institute (**77–90% training speedups**); a RAPIDS cuML + Dask pipeline cut cell-type evaluation from hours to minutes; reference architecture adopted across teams.
- **3.7× peak throughput** (70 → 261 req/s) and **39% lower P50 latency** for the Large Payment Model, a top-10 global bank's fraud-detection foundation model, vs the bank's FP32 PyTorch baseline: TensorRT on Triton with dynamic batching, lifting GPU utilization from ~40% to 90%+; INT8 QAT added +68% throughput at near-lossless embedding fidelity.
- Profiled with Nsight Systems to isolate CPU-side bottlenecks, then vectorized concurrent tokenization and bucketized CUDA Graphs to cut kernel-launch overhead; designed the burst-absorption serving path (~370 requests / 50 ms: bounded per-pod batching queues with backpressure, warm pods, EKS auto-scaling). **In production, accelerating go-live by 3 months.**
- Built a text-to-PySpark agentic workflow for an enterprise networking data lake: DSPy auto-prompt optimization (**+46% CodeBLEU**), complexity-aware query routing (+43% on complex queries), and LangGraph workflow optimization (−19% end-to-end latency).

**Software Development Engineer, Amazon Bedrock / SageMaker** · promoted to SDE II · *Feb 2023 – May 2025* (Intern, *2022*)

- **Led and shipped on-demand, token-based serving of fine-tuned models to production**: multi-tenant LoRA serving (shared base model in memory, per-customer adapters hot-swapped at runtime) with KV-cache-aware request routing — **92–99% lower inference cost** for spiky low-traffic workloads and 90% faster deployment than provisioned throughput, driving adoption of Bedrock model customization.
- Shipped **Llama 3 SFT and distillation** in Bedrock Model Customization (**launched at re:Invent 2024**); cut fine-tuning job failures **50%** with an API-layer validation system.

---

## Publications

- C. Ling, et al. (incl. **R. Xue**). *Deep Graph Representation Learning and Optimization for Influence Maximization.* **ICML 2023.** [arXiv](https://arxiv.org/abs/2305.02200)
- R. Wang\*, **R. Xue**\* et al. *PRISM: Position-encoded Regressive Inverse Spectral Model for Multilayer Thin-Film Design.* ICML Workshop on AI for Physics, 2026. *(\*equal contribution)* [arXiv](https://arxiv.org/abs/2605.26502)
- R. Wang, **R. Xue**, et al. *AME-TS: Anchored Mixture-of-Experts for Time Series Forecasting.* ICML 2026 Workshop; extended version under review at NeurIPS. [arXiv](https://arxiv.org/abs/2605.25166)
- Y. Cui, **R. Xue**, et al. *From Errors to Rules: Iterative Prompt Optimization for Text Classification.* Preprint, 2026. [arXiv](https://arxiv.org/abs/2607.20497)
- **R. Xue** et al. *Inference-Time Model Steering via Predictive-State Intervention: A Survey.* Preprint, 2026. [preprint](https://www.researchsquare.com/article/rs-9849186/v1)

---

## Open Source

- **[awslabs/mcp](https://github.com/awslabs/mcp/tree/main/src/mcp-lambda-handler)**: Code owner and recurring contributor to AWS's official Model Context Protocol repo.
- **[nanoLLaDA](https://github.com/Lukas-Xue/nanoLLaDA)**: Minimal (~500-line) masked diffusion language model · **[PRISM](https://www.prism-playground.com/)**: inverse thin-film design transformer (interactive playground) · **[awesome-inference-time-steering](https://github.com/Lukas-Xue/awesome-inference-time-steering)**: curated survey.

---

## Education

- **B.S. Computer Science** (Minor: Applied Math), **Emory University** · *2019 – Dec 2022* · GPA 3.94/4.00. Student researcher (graph neural networks); TA for ML (CS334) and Algorithms (CS326).
- M.S. Information Studies, Trine University (part-time) · *2025 – 2026*

---

## Technical Skills

**Post-Training:** SFT, DPO, GRPO, CPT, distillation, LoRA/adapters, quantization (QAT/PTQ)
**Frameworks:** PyTorch, HuggingFace (Transformers/PEFT/TEI), Lightning, Unsloth, FSDP, DDP, Dask, RAPIDS, DSPy, LangGraph
**Inference / Serving:** vLLM, TensorRT, Triton, ONNX Runtime, CUDA graphs, dynamic batching · **Distributed:** multi-node/multi-GPU, data/model parallelism, SageMaker HyperPod
**Infra / Profiling:** AWS (Bedrock, SageMaker, EKS, MSK, Lambda, FSx), Kubernetes, Docker, Terraform, Nsight, DCGM, Prometheus, Grafana, OpenTelemetry · **Languages:** Python, Java, SQL, TypeScript
