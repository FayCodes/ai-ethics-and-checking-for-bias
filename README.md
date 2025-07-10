# 🌍 COMPAS Bias Audit & AI Ethics Report

This project explores the ethical dimensions of AI through a comprehensive analysis of the COMPAS Recidivism Dataset. It blends theoretical insight, case study evaluation, technical bias auditing, and policy design, demonstrating responsible AI development aligned with fairness, transparency, and human-centric principles.

---

## 📚 Assignment Overview: "Designing Responsible and Fair AI Systems"

Submitted for the AI Ethics unit, this group assignment includes:

- ✅ Theoretical responses on key ethical concepts
- ✅ Case study analysis of real-world bias scenarios
- ✅ Fairness audit of the COMPAS dataset
- ✅ Ethical reflection on future project values
- ✅ Bonus healthcare policy proposal for ethical AI use

---

## 🧠 Part 1: Theoretical Understanding

**Short Answers:**
- Defined algorithmic bias with examples in finance and hiring.
- Differentiated transparency vs. explainability in AI systems.
- Analyzed GDPR's impact on EU-based AI development and data governance.

**Ethical Principles Matching:**
- Justice → Fair distribution of AI benefits/risks  
- Non-maleficence → Ensuring AI does no harm  
- Autonomy → Respecting users’ control over data and decisions  
- Sustainability → Environmentally responsible AI design

---

## 🧪 Part 2: Case Study Analysis

**Case 1: Amazon’s Biased Hiring Tool**
- Source of bias: Gender-skewed training data
- Fixes:
  - Diversify training datasets
  - Strip gendered proxies from input features
  - Implement post-training fairness constraints
- Evaluation Metrics: Disparate impact ratio, false negative rate difference, Equal Opportunity Difference

**Case 2: Facial Recognition in Policing**
- Ethical risks: Misidentification, wrongful arrests, data privacy violations
- Deployment Recommendations:
  - Human review for all matches
  - Transparency with affected communities
  - Independent model audits and bias thresholding

---

## 📊 Part 3: Practical Audit (Using AI Fairness 360)

Audited the COMPAS dataset for racial and gender bias using Python.

**Libraries Used:**
- `aif360`
- `pandas`
- `matplotlib`
- `scikit-learn`

**Protected Attributes Analyzed:**
- Race (`Caucasian` vs. `African-American`)
- Sex (`Male` vs. `Female`)

**Metrics Calculated:**
- Statistical Parity Difference
- Disparate Impact
- Equal Opportunity Difference
- Average Odds Difference
- False Positive/Negative Rate Differences

**Visualizations Saved:**
- `compas_bias_analysis_race.png`
- `compas_bias_analysis_sex.png`

**Report Delivered:**
- `report.txt` – 300-word summary of findings and mitigation recommendations  
> Technical audit completed with support from Cursor AI and Copilot for debugging, validation, and ethical framing.

---

## 💬 Part 4: Ethical Reflection

Reflecting on future bias analysis tools, key ethical values included:

- Designing for inclusive fairness audits
- Ensuring explainability through interpretable models
- Transparent documentation of model design and limitations
- Preserving human decision oversight in AI-augmented systems

---

## 🏥 Bonus Task: AI Policy Proposal for Healthcare

**Document: `policy_guideline.txt`**

Outlines protocols for ethical AI deployment in healthcare, including:

- **Patient Consent Protocols**:
  - Clear opt-in/opt-out policies
  - Assurance of human oversight

- **Bias Mitigation Strategies**:
  - Inclusive training data
  - Routine fairness audits
  - Stakeholder inclusion

- **Transparency Requirements**:
  - Explainable model outputs
  - Disclosure of AI usage in clinical workflows

---

## ⚙️ Full Tool Stack Used

| Tool               | Purpose                               |
|--------------------|----------------------------------------|
| `Python`           | Scripting language                     |
| `aif360`           | IBM Fairness toolkit                   |
| `pandas`           | Data cleaning and manipulation         |
| `matplotlib`       | Visualization                          |
| `scikit-learn`     | Utility functions & data prep          |
| `Cursor AI`        | Code debugging assistant               |
| `Copilot`          | Guidance, ethical framing & reporting  |
| `Google Colab`     | Notebook environment                   |

---

## 📌 Submission Format

- PDF document: Written answers and case study analysis  
- GitHub Repository: Code, visualizations, and README  
- Article (Bonus): Policy proposal shared with PLP Academy

---

## 🌟 Why This Matters

Ethical AI is the cornerstone of trustworthy, impactful technology. This project demonstrates:
- Awareness of social implications
- Technical competency in bias auditing
- Commitment to responsible, transparent AI development

