# Responsible AI Lifecycle Mapping – Patient Education Assistant

This document maps system components to the Responsible AI lifecycle.

---

## 1. Intended Use & Scope
Defined in:
- README.md

Key controls:
- Education-only purpose
- Explicit exclusion of diagnosis, treatment, prescriptions

---

## 2. Safety & Harm Prevention
Implemented in:
- safety.py

Controls:
- Policy-based intent detection
- Blocking of clinical decision requests
- Safe redirection to licensed clinicians

---

## 3. Human-Centered Response Design
Implemented in:
- app.py

Controls:
- Non-authoritative tone
- Reinforced clinician consultation
- No medical instructions

---

## 4. Post-Interaction Evaluation
Implemented in:
- evaluator.py

Signals captured:
- Safety block events
- User-declared demographic context
- Interaction metadata for auditability

---

## 5. Fairness & Drift Awareness
Enabled by:
- Aggregated evaluator logs
- Demographic-based block rate visibility

Supports:
- Bias detection
- Policy refinement
- Long-term monitoring

---

## 6. Auditability & Governance
Supported by:
- Structured logging
- Deterministic system behavior
- Explicit lifecycle documentation
