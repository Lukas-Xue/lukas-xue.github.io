# Renhao (Lukas) Xue

**Machine Learning Engineer · Generative AI, LLM Training & Inference at Scale**
Seattle, WA · lukas.rxue@gmail.com · 470-775-1452 · [lukasxue.com](https://lukasxue.com) · {{icon:github|https://github.com/Lukas-Xue}} {{icon:linkedin|https://www.linkedin.com/in/lukas-xue/}} {{icon:scholar|https://scholar.google.com/citations?user=oaIhxugAAAAJ&hl=en}}

---

## Summary

AWS ML engineer with **two re:Invent launches**: distributed post-training of foundation models, Bedrock's multi-tenant serving platform for fine-tuned models, and inference optimization that cuts enterprise latency, cost, and time-to-launch.

---

## Experience

### Amazon Web Services, Generative AI Innovation Center
**Machine Learning Engineer II** · Seattle, WA · *May 2025 – Present*

- Post-train foundation models **up to 30B parameters** (Qwen3, Llama 3.1, Nova 2 Lite; text and vision-language) with SFT, DPO, and GRPO — from single-GPU LoRA (Unsloth) to distributed SageMaker HyperPod runs on 8×H200 and 8×A100 clusters — shipping custom models to enterprise production.
- Fine-tuned **Amazon Nova 2 Lite** (VLM) for document understanding (classification, key-information extraction, packet splitting), **matching Claude Sonnet 4.5 quality at ~1/10 the inference cost**; 2× ordered-split accuracy on shuffled multi-page PDFs, 96% page classification.
- **3.7× peak throughput** (70 → 261 req/s) and **39% lower P50 latency** serving the Large Payment Model, a top-10 global bank's fraud-detection foundation model, vs the bank's FP32 PyTorch baseline: TensorRT on Triton with dynamic batching, lifting GPU utilization from ~40% to 90%+; INT8 QAT added +68% throughput at near-lossless accuracy.
- Designed the burst-traffic architecture for the same platform (~370 requests / 50 ms): NLB ingress, per-pod bounded batching queues with backpressure, warm over-provisioned pods, and EKS auto-scaling; profiled with Nsight Systems and validated with open- and closed-loop benchmarks. **In production, accelerating go-live by 3 months.**
- Built distributed multi-node training and inference for a single-cell foundation model (**77–90% training speedups**) and a RAPIDS cuML + Dask pipeline cutting cell-type evaluation from hours to minutes; reference architecture adopted across teams.
- Built a text-to-PySpark agentic workflow for an enterprise networking data lake: DSPy auto-prompt optimization (**+46% CodeBLEU**), complexity-aware query routing (+43% accuracy on complex queries), and LangGraph workflow optimization (−19% end-to-end latency).

**Software Development Engineer, Amazon Bedrock / SageMaker** · promoted to SDE II · *Feb 2023 – May 2025* (Intern, *2022*)

- **Led on-demand, token-based hosting of fine-tuned models to production**: multi-tenant LoRA serving (shared base model, per-customer adapters hot-swapped at runtime) with KV-cache-aware request routing — **92–99% lower inference cost** and 90% faster deployment than provisioned throughput, driving adoption of Bedrock model customization.
- Shipped **Llama fine-tuning and distillation** in Bedrock Model Customization (**launched at re:Invent 2024**) across production regions; cut fine-tuning job failures **50%** with an API-layer validation system.
- Led AWS Graviton integration for Amazon MSK (**launched at re:Invent 2023**) with platform-aware deployment automation, **+45% performance** over M5 clusters.

---

## Selected Projects & Open Source

- **[awslabs/mcp](https://github.com/awslabs/mcp/tree/main/src/mcp-lambda-handler)**: Code owner and recurring contributor to AWS's official Model Context Protocol repository.
- **[nanoLLaDA](https://github.com/Lukas-Xue/nanoLLaDA)**: Minimal (~500-line) masked diffusion language model implementation.
- **[PRISM](https://www.prism-playground.com/)**: Deployed interactive playground serving an autoregressive transformer for inverse thin-film optical design.

---

## Publications

- C. Ling et al. (incl. **R. Xue**). *Deep Graph Representation Learning and Optimization for Influence Maximization.* **ICML 2023.** [arXiv](https://arxiv.org/abs/2305.02200)
- R. Wang, **R. Xue**, et al. *AME-TS: Anchored Mixture-of-Experts for Time Series Forecasting.* ICML 2026 Workshop; extended version under review at NeurIPS. [arXiv](https://arxiv.org/abs/2605.25166)
- Y. Cui, **R. Xue**, et al. *From Errors to Rules: Iterative Prompt Optimization for Text Classification.* Preprint, 2026. [arXiv](https://arxiv.org/abs/2607.20497)
- **R. Xue** et al. *Inference-Time Model Steering via Predictive-State Intervention: A Survey.* Preprint, 2026. [preprint](https://www.researchsquare.com/article/rs-9849186/v1)

---

## Education

- **B.S., Computer Science** (Minor: Applied Mathematics), Emory University · *Sep 2019 – Dec 2022* · GPA 3.94/4.00
- M.S., Information Studies, Trine University (part-time) · *2025 – 2026*

---

## Technical Skills

- **Languages:** Python, Java, SQL, TypeScript, Bash
- **ML / Training:** PyTorch, HuggingFace, PyTorch Lightning, Unsloth, FSDP, DDP, Dask, RAPIDS; SFT, DPO, GRPO, distillation, quantization
- **Inference / Serving:** vLLM, TensorRT, Triton, ONNX Runtime, dynamic batching, CUDA graphs
- **Cloud / Infra:** AWS (Bedrock, SageMaker HyperPod, EKS, MSK, Lambda, EC2, S3, FSx), Kubernetes, Docker, Terraform
- **Observability:** Prometheus, Grafana, DCGM, OpenTelemetry, NVIDIA Nsight

*AWS Certifications: ML Engineer (Associate), ML (Specialty), AI Practitioner, Developer (Associate).*
