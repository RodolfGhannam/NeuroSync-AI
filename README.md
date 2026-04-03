# NeuroSync AI: Co-Adaptive Causal Attribution for Resilience and Empathy (C-CARE)

**A Technical Artifact for the Mobiliar Lab for Analytics (ETH Zurich)**  
**Aligned with the MTEC Foundation research agenda**  
**Author:** Rodolf Mikel Ghannam Neto

---

## 1. Overview and Symbiotic Research Agenda

NeuroSync AI is a dual-layer conversational architecture designed to solve the paradox of artificial empathy in frontline service encounters. Built specifically to address the open challenges identified by the **Mobiliar Lab for Analytics**, this artifact operationalises the lab's recent theoretical breakthroughs into a testable, research-grade Proof of Concept system.

### Addressing Open Challenges from the Mobiliar Lab:
1. **The Trojan Horse Paradox (Uysal et al., 2025):** While Uysal proved that AI empathy protects against service failures in routine tasks but harms in complex ones, the study relied on static 2x2 experimental designs. **NeuroSync AI operationalises this** by introducing dynamic, real-time calibration of anthropomorphism based on user cognitive load, extending the foundational *Trojan Horse* framework (Uysal et al., 2024).
2. **The Trustworthy LLM Gap (Benk et al., 2025, AAAI):** Benk identified a critical gap between LLM standards and user expectations for transparency. **NeuroSync AI operationalises this** by using transparency as an operational tool: when user stress peaks, the bot explicitly down-regulates empathy, signaling its machine nature to reduce relational uncertainty.
3. **Chatbot Uncertainty Taxonomy (Asisof, 2025):** Asisof mapped the 5 dimensions of user uncertainty (CUT). **NeuroSync AI operationalises this taxonomy** by using causal inference to measure exactly which type of uncertainty is reduced when anthropomorphism is calibrated.

By bridging these gaps, NeuroSync AI is designed to run large-scale, closed-loop field experiments that prove the causal business impact of the Mobiliar Lab's theories.

---

## 2. Architecture: The C-CARE Protocol

The system is built on a robust, research-grade Proof of Concept stack, prioritizing low latency and rigorous causal tracking (addressing the architectural limitations identified in *EventChat*, Ollier et al., 2024/2026).

```text
[User Input: Voice/Text] 
       │
       ▼
┌─────────────────────────────────────────────────────────┐
│ SYNCHRONOUS LAYER (Real-Time Affective Computing)       │
│ - Engine: Hume AI (EVI) / OpenClaw                      │
│ - Logic: Decodes user stress (Neuroception of Safety)   │
│ - Action: Dynamically calibrates Anthropomorphism Level │
└─────────────────────────────────────────────────────────┘
       │ (Affective State & Chat Logs)
       ▼
┌─────────────────────────────────────────────────────────┐
│ ORCHESTRATION & API LAYER                               │
│ - Engine: FastAPI / Flask (Gunicorn)                    │
│ - Logic: Routes data, manages state, enforces low       │
│   latency for real-time service encounters              │
└─────────────────────────────────────────────────────────┘
       │ (Structured Encounter Data)
       ▼
┌─────────────────────────────────────────────────────────┐
│ ASYNCHRONOUS LAYER (Causal Inference & Business Value)  │
│ - Engine: EconML (Microsoft) / Weights & Biases         │
│ - Logic: Double Machine Learning (DML)                  │
│ - Action: Estimates Heterogeneous Treatment Effects     │
│   (HTE) of Anthropomorphism on NPS & Churn              │
└─────────────────────────────────────────────────────────┘
```

---

## 3. Theoretical Foundations & Mobiliar Lab Alignment

NeuroSync AI is grounded in rigorous Marketing and Information Systems theory, directly extending the work of Prof. Florian von Wangenheim and Dr. Joseph Ollier.

| Theory / Framework | Key Reference | Symbiotic Application in NeuroSync AI |
| :--- | :--- | :--- |
| **The Trojan Horse Effect** | Uysal et al. (2025) | Transforms static empathy findings into a dynamic, real-time calibration engine. |
| **Trustworthy LLM Standards** | Benk et al. (2025) | Operationalizes user expectations for transparency during high-stress encounters. |
| **Chatbot Uncertainty Taxonomy (CUT)** | Asisof (2025) | Maps dynamic tone adjustments to specific reductions in functional and relational uncertainty. |
| **Agentic Recommender Systems** | Ollier et al. (2024/2026) | Adds the missing "affective causal layer" to the EventChat architecture. |

---

## 4. Repository Structure

This repository serves as a Proof of Concept (PoC) for the C-CARE protocol.

```text
NeuroSync-AI/
├── src/
│   ├── api_sync.py              # Flask/FastAPI routing and synchronous logic
│   └── neuro_engine.py          # Hume EVI integration (placeholder)
├── notebooks/
│   └── 01_DML_Causal_Inference_PoC.py # EconML script proving the Trojan Horse effect
├── Dockerfile                   # Production-ready containerization (Gunicorn)
├── requirements.txt             # Python dependencies (EconML, Flask, Hume)
├── .gitignore                   # Standard Python gitignore
├── LICENSE                      # MIT License
└── README.md                    # This document
```

---

## 5. Getting Started (Proof of Concept)

To run the Asynchronous Causal Layer (DML) simulation:

1. Clone the repository:
   ```bash
   git clone https://github.com/RodolfGhannam/NeuroSync-AI.git
   cd NeuroSync-AI
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the DML Simulation:
   ```bash
   python notebooks/01_DML_Causal_Inference_PoC.py
   ```
   *Expected Output:* The script will generate synthetic service encounters and use EconML to prove that high anthropomorphism increases NPS in routine tasks (+1.89) but decreases NPS in complex tasks (-1.81), validating the Trojan Horse hypothesis mathematically.

---

## 6. References

1. Uysal, E., Efthymiou, F., Mari, A., & Brooks, S. (2025). No hard feelings - The protective power of AI empathy during service interaction failures. *SSRN*.
2. Benk, M., Wettstein, L., Schlicker, N., von Wangenheim, F., & Scharowski, N. (2025). Bridging the Knowledge Gap: Understanding User Expectations for Trustworthy LLM Standards. *Proceedings of the AAAI Conference on Artificial Intelligence*.
3. Asisof, A. (2025). Retrieving Under Uncertainty: Towards a Chatbot Uncertainty Taxonomy (CUT) for Information Retrieval. *ACM*.
4. Ollier, J., et al. (2024/2026). EventChat: Implementation and user-centric evaluation of a large language model-driven conversational recommender system. *ACM Transactions*.
5. Huang, M.-H., & Rust, R. T. (2021). A strategic framework for artificial intelligence in marketing. *Journal of the Academy of Marketing Science*.
