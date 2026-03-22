# Cortex Skill: Architectural Analysis

This skill generates a complete functional and architectural analysis for client proposals from a requirement document or conversation. It is designed to transform business needs into high-quality technical and executive artifacts, following a strict sequential flow. It has been tested with claude.ai / claudde code. The generation of artifacts such as HTML infographics will depend on the capabilities of each agent.

[Spanish version available here](README_es.md)

## Project Structure

```text
.
├── .gitignore                          # Configuration for ignored files
├── README.md                           # Main project documentation (English)
├── README_es.md                        # Project documentation (Spanish)
└── cortex-skill-architectural-analysis/ # Skill root directory
    ├── SKILL.md                        # Skill definition and logic
    └── references/                     # Templates and reference guides
```

## Skill Architecture

### Conceptual Architecture

The skill operates under a **sequential blocks** model with approval gates (*gates*). Each block generates a set of artifacts that serve as input for the next one.

```mermaid
graph TD
    P0[Step 0: Context Questionnaire] --> |Approval| BA[Block A: Diagnosis and Context]
    BA --> |Approval| BB[Block B: Executive Narrative]
    BB --> |Approval| BC[Block C: Technical Detail]
    
    subgraph "Block A (Internal/Client)"
        A1[A1: Executive Summary]
        A2[A2: NFRs]
        A3[A3: Process Map]
    end
    
    subgraph "Block B (Executive)"
        A4[A4: Infographic]
        A5[A5: Conceptual Architecture]
    end
    
    subgraph "Block C (Technical)"
        A6[A6: Contextual Arq.]
        A7[A7: Atomic Sequences]
        A8[A8: HTML Prototypes]
        A9[A9: Risks]
        A10[A10: ADRs]
        A11[A11: OpEx]
        A12[A12: Team]
        A13[A13: Sprints]
        A14[A14: RACI]
    end
```

### Operation Sequence Diagram

The interaction flow between the user and the skill ensures there is no over-engineering and that artifacts are consistent.

```mermaid
sequenceDiagram
    participant U as User
    participant S as Cortex Skill (Architect)
    
    U->>S: Provides Requirement / RFP
    S->>S: Activates Step 0 (Mandatory Gate)
    S->>U: Presents Context Questionnaire
    U->>S: Confirms Response / Adjusts Stack
    
    Rect rgb(240, 240, 240)
        Note over S, U: BLOCK A: Diagnosis
        S->>U: Generates A1-A3 with micro-checkpoints
        U->>S: Approves Block A (Checkpoint A)
    End
    
    Rect rgb(220, 240, 220)
        Note over S, U: BLOCK B: Narrative
        S->>U: Generates A4-A5 (Visuals/Strategic)
        U->>S: Approves Block B (Checkpoint B)
    End
    
    Rect rgb(200, 220, 255)
        Note over S, U: BLOCK C: Technical Detail
        S->>U: Activates PDA (Decision Protocol)
        U->>S: Confirms Technical Decisions
        S->>U: Generates A6-A14 (Technical Specification)
    End
    
    S->>U: Final Packaged Delivery (.md, .html, .mmd)
```

## Main Features

- **Context Propagation**: The technological stack and component names defined initially remain identical across all artifacts.
- **Architectural Decision Protocol (PDA)**: Before defining technical architecture, compute, data, and integration trade-offs are consulted.
- **Sequence Atomicity**: Sequence diagrams are divided into minimum verifiable flows.
- **Derived Prototyping**: UI screens are generated directly from the steps of the sequence diagrams.

## Skill Usage

To activate the skill, simply load a requirements document or describe your system. The skill will respond by starting **Step 0** to capture the base technological context (Cloud, Backend, Frontend, etc.).

> **Important**: No artifacts will be generated until Step 0 is explicitly confirmed.

## Design Guide (Design System)

All generated HTML artifacts follow a premium design system, with clear palettes and modern typography, ensuring a professional presentation for the final client. Refer to `references/design-system.md` for more details.

## Artifact Examples

Below are examples of some of the artifacts that this skill is capable of generating as part of an architectural analysis of a requirement.

### 1. Conceptual Architecture
This diagram shows the interaction of the system with external actors and internal layers.

![Contextual Architecture](examples/arquitectura_conceptual.png)

### 1.2 Contextual Architecture
This diagram shows the relationships between the components of the system.

![Contextual Architecture](examples/arquitectura_contextual.png)

### 2. Problem and Solution Infographic
Executive visualization of client challenges and the value proposition.

![Problem and Solution Infographic](examples/problema_solucion_inforgrafia.png)

### 3. Atomic Sequence Diagrams
Examples of detailed flows for diagnosis and reporting.

#### Reactive Diagnosis Detail
```mermaid
sequenceDiagram
    actor Operator as Support Staff
    participant Orch as Cortex Orchestrator
    participant Diag as Diagnostic Agent
    participant Know as Knowledge Agent
    participant OraDB as Oracle Autonomous DB AI
    participant Gemini as Gemini API

    Note over Operator,Gemini: ── HAPPY PATH (P03 — Reactive incident diagnosis) ──
    Note right of Operator: P95 < 5s end-to-end (Latency NFR)

    Operator->>Orch: "Fault in WebLogic-Prod-07. AdminServer not responding"
    Note right of Orch: Supervisor detects intent: incident diagnosis
    Orch->>Diag: task("diagnose AdminServer WebLogic-Prod-07")
    Diag->>OraDB: get_server_status("WebLogic-Prod-07")
    OraDB-->>Diag: {status: "degraded", cpu: 98%, heap: 95%, threads: "stuck"}
    Diag->>OraDB: get_server_logs("WebLogic-Prod-07", last=100)
    OraDB-->>Diag: [log_entries with OutOfMemoryError and stuck threads]
    Diag->>Know: task("search OutOfMemoryError WebLogic stuck threads")
    Know->>OraDB: vector_search("OutOfMemoryError WebLogic AdminServer")
    OraDB-->>Know: [{runbook: "wl_oom_remediation.md", score: 0.91}]
    Know-->>Diag: runbook_context
    Diag->>Gemini: analyze(logs + status + runbook, model=pro)
    Gemini-->>Diag: {root_cause: "Heap exhaustion due to thread leak", remediation: [...]}
    Diag-->>Orch: structured_diagnosis
    Orch-->>Operator: Diagnosis + root cause + suggested remediation steps
    Note right of Orch: AuditLog records all tool calls
```

#### Report Generation
```mermaid
sequenceDiagram
    actor Operator as Support Staff
    participant Orch as Cortex Orchestrator
    participant Rep as Reporting Agent
    participant Gemini as Gemini API
    participant Audit as AuditLog

    Note over Operator,Audit: ── HAPPY PATH (P06 — Incident report generation) ──

    Operator->>Orch: "Generate the report for the WebLogic-Prod-07 incident"
    Note right of Orch: Supervisor retrieves current session context
    Orch->>Rep: task("generate incident report", session_context)
    Rep->>Audit: get_session_actions(thread_id)
    Audit-->>Rep: [{tool: "get_server_logs", result: ...}, {tool: "get_server_status", result: ...}]
    Rep->>Gemini: generate_report(acciones + diagnosis + report_template, model=flash)
    Gemini-->>Rep: structured_report
    Note right of Rep: Structure: summary · timeline · diagnosis · lessons learned
    Rep-->>Orch: {report: structured_report, format: "markdown"}
    Orch->>Audit: log_action("generate_report", actor=Operator, result=ok)
    Orch-->>Operator: Full incident report

    Note over Operator,Audit: ── ALTERNATIVE ROUTE — No active diagnosis session ──
    Operator->>Orch: "Generate report" (no previous diagnosis in session)
    Orch-->>Operator: "I didn't find a diagnosis in the current session. Do you want to start one first?"
```

### 4. UI Prototypes
Example of generated interfaces for the system.

![UI Prototypes](examples/prototipo_pantallas.png)
