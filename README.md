# ai-ethics-and-checking-for-bias

This project explores the ethical dimensions of AI through a comprehensive analysis of the **COMPAS Recidivism Dataset**. It blends theoretical insight, case study evaluation, technical bias auditing, and policy design to demonstrate responsible AI development aligned with fairness, transparency, and human-centric principles.

---

## 📚 Project Overview
* **Goal**: Conduct a comprehensive fairness audit of the COMPAS dataset and design protocols for responsible AI systems.
* **Assignment**: Submitted for the "Designing Responsible and Fair AI Systems" unit, covering theory, real-world case studies, and technical implementation.
* **Deliverables**: Theoretical analysis, fairness audit reports, technical visualizations, and a healthcare-specific AI policy proposal.

---

## 🧠 Part 1: Theoretical & Case Study Analysis
* **Ethical Framework**: Applied principles of Justice, Non-maleficence, Autonomy, and Sustainability to AI governance.
* **Amazon Hiring Case**: Analyzed gender-skewed training data and proposed mitigation through diversified datasets and removing gendered proxies.
* **Policing & Facial Recognition**: Identified risks of misidentification and wrongful arrest, recommending human-in-the-loop oversight and independent audits.

---

## 📊 Part 2: Technical Audit (AI Fairness 360)
Using **Python** and the **aif360** toolkit, I conducted a technical audit of the COMPAS dataset to identify racial and gender disparities.
* **Protected Attributes**: Race (Caucasian vs. African-American) and Sex (Male vs. Female).
* **Metrics Calculated**: Statistical Parity Difference, Disparate Impact, Equal Opportunity Difference, and Average Odds Difference.
* **Findings**: Detailed bias analysis saved in `compas_bias_analysis_race.png` and `compas_bias_analysis_sex.png`.

---

## 🏥 Part 3: Healthcare AI Policy Proposal
Outlined in `policy_guideline.txt`, this proposal establishes protocols for ethical AI deployment in clinical settings:
* **Patient Protections**: Established clear opt-in/opt-out consent policies and mandated human oversight for clinical decisions.
* **Bias Mitigation**: Protocols for inclusive training data and routine fairness audits to prevent diagnostic disparities.
* **Transparency**: Requirements for explainable model outputs and full disclosure of AI usage in medical workflows.

---

## ⚙️ Tool Stack
* **Languages & Environments**: Python, Google Colab.
* **Libraries**: aif360 (IBM Fairness toolkit), pandas, matplotlib, scikit-learn.

---

## 👤 About the Developer

**Faith Blessing Wafula**

Lead Developer and Data Scientist focused on building intelligent systems and data-driven solutions that bridge the gap between technical excellence and community impact.
