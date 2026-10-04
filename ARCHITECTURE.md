---

# Task 1: Functional & Non-Functional Requirements Breakdown

### 1.1 Functional Requirements (FRs)
| Req ID | Category | Description | Priority |
| :--- | :--- | :--- | :--- |
| **FR-01** | Face Detection | System must detect human faces from incoming IP camera streams in real-time. | High |
| **FR-02** | Facial Recognition | System must match detected faces against student/staff embeddings in the database. | High |
| **FR-03** | Attendance Logging | System must log entry time, student ID, confidence score, and camera ID upon face recognition. | High |
| **FR-04** | Database Synchronization | System must sync attendance logs with the central cloud/university database every 5 minutes. | Medium |
| **FR-05** | Real-time Alerts | System must trigger instant alerts to security/admins upon detecting unauthorized individuals. | High |

### 1.2 Non-Functional Requirements (NFRs)
| Req ID | Metric / Area | Specification / Threshold | Priority |
| :--- | :--- | :--- | :--- |
| **NFR-01** | Frame Rate | System must sustain a minimum processing rate of 25-30 FPS per camera channel. | High |
| **NFR-02** | Model Accuracy | Facial recognition accuracy threshold must be >= 98.5% on benchmark test sets. | High |
| **NFR-03** | Processing Latency | Face detection to attendance log latency must be < 200 ms per frame. | High |
| **NFR-04** | Edge Power Usage | Edge device (e.g., Jetson/Raspberry Pi) power consumption must not exceed 25W. | Medium |
| **NFR-05** | Data Privacy & Security | AES-256 encryption for stored facial embeddings; strict compliance with data privacy regulations. | High |

---

---

# Task 2: System Boundary, User Persona, & Input/Output Mapping

### 2.1 System Boundary & Primary Actors
* **Security Operator:** Views live camera analytics, bounding boxes, and security alerts.
* **System Administrator:** Configures camera RTSP streams, updates model weights, and manages user databases.
* **Automated Trigger System:** Relays real-time event notifications to external gateways (SMS/Email/Database).

### 2.2 Input & Output Mapping
| Component | Parameter / Data Item | Specifications / Data Format |
| :--- | :--- | :--- |
| **System Inputs** | RTSP Stream | IP Camera H.264/H.265 video feed @ 1080p resolution |
| | Camera Metadata | Camera ID, Location Tag, RTSP Credentials |
| | Sensor Data | Ambient Light Level, PIR Motion Signals |
| **System Outputs** | Visual Overlays | Bounding box coordinates `[x1, y1, x2, y2]`, labels, confidence scores |
| | Alert Notifications | JSON payloads for Telegram/Email/SMS security alerts |
| | Log Entries | Structured attendance records written to PostgreSQL / SQLite |

### 2.3 Operational Constraints
* **Memory Footprint:** Maximum RAM usage must stay below **4 GB** per stream instance.
* **Network Bandwidth:** Network consumption capped at **5 Mbps** per RTSP video pipeline.
* **Storage Limit:** Local log buffer limited to **10 GB** before automated cloud archival.

---

---

# Task 3: Data-Flow Diagrams (DFDs)

### 3.1 Level 0 DFD (Context Diagram)
```mermaid
graph TD
    A[IP Camera Sensor] -->|Raw RTSP Video Feed| B((Smart Vision System))
    B -->|Bounding Boxes & Logs| C[Security Operator / Dashboard]
    B -->|Attendance Logs| D[(Central Database)]
    E[Admin User] -->|Config & Thresholds| B

---

graph TD
    A[RTSP Stream] --> P1[1.0 Data Ingestion]
    P1 -->|Raw Frame Arrays| P2[2.0 Image Preprocessing]
    P2 -->|Normalized Tensor| P3[3.0 Model Inference Engine]
    P3 -->|Bounding Boxes & Features| P4[4.0 Post-Processing & Matching]
    P4 -->|Recognized Student ID| P5[5.0 Attendance & Alert Logger]
    P5 --> D1[(Attendance Database)]
    P5 --> D2[(System Alert Logs)]

    