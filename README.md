# InsightForge - AI Data Analyst Copilot📊⚡

**Forge meaningful insights from your data through natural language conversations and intelligent analytics.**

InsightForge is an AI-powered, multi-agent analytics platform that automates data profiling, cleaning, visualization, and insight generation from structured datasets (CSV and Excel files). Built with **LangGraph**, **FastAPI**, and **Streamlit**, it transforms natural language queries into precise data manipulations, interactive visualizations, and actionable business recommendations.

---

## 📸 Demo
Watch the Demo video of the project.
[▶️ Watch Demo](./assets/demo.mp4)

---


## 🚀 Key Features

* **Automated Data Profiling**: Instantly analyze dataset structure, including row and column counts, missing values, and data types.
* **Conversational Analytics**: Ask questions about your data in plain English and receive intelligent answers, statistics, and aggregations.
* **Multi-Agent Orchestration**: Uses LangGraph to coordinate planning, code generation, execution, visualization, and insight synthesis.
* **Interactive Visualizations**: Dynamically creates interactive Plotly charts tailored to user requests.
* **Safe Code Execution**: Generates and executes Python code locally within a controlled environment.
* **Multiple LLM Providers**: Supports Groq (Llama 3.3), Gemini (Gemini 2.5), and Nvidia AI Endpoints out of the box.
* **Decoupled Architecture**: Combines a scalable FastAPI backend with a lightweight Streamlit frontend.

---

## 🏗️ Multi-Agent Architecture

InsightForge leverages a graph-based agent workflow to deliver reliable and explainable analytics.

### 1. Planner Agent

Analyzes dataset metadata and determines the sequence of steps required to answer the user's query.

### 2. Code Generation Agent

Generates Python code using Pandas and NumPy, executes it safely, and produces the required outputs.

### 3. Visualization Agent

Identifies appropriate chart types and creates interactive Plotly visualizations.

### 4. Insight Generation Agent

Transforms analytical results into human-readable summaries, key findings, and business recommendations.

---

## 📁 Project Structure

```text
├── app/
│   ├── agents/          # Specialized AI agents
│   ├── api/             # FastAPI endpoints
│   ├── frontend/        # Streamlit application
│   ├── graph/           # LangGraph workflow definitions
│   ├── llm/             # LLM provider integrations
│   ├── schema/          # Pydantic schemas
│   ├── services/        # Business logic
│   ├── tools/           # Agent tools and utilities
│   ├── utils/           # Shared helper functions
│   └── main.py          # FastAPI application entry point
├── assets/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vintagevikas090/Insight-Forge.git

cd insight-forge
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows (PowerShell)**

```bash
.\venv\Scripts\Activate.ps1
```

**Windows (CMD)**

```bash
.\venv\Scripts\activate.bat
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Add your API credentials:

```env
GROQ_API_KEY="your_groq_api_key"
HF_TOKEN="your_huggingface_token"
```

---

## 🚦 Running the Application

The application consists of a FastAPI backend and a Streamlit frontend.

### Start the Backend Server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### Start the Streamlit Frontend

Open another terminal and run:

```bash
streamlit run app/frontend/streamlit_app.py
```

The frontend will launch at:

```text
http://localhost:8501
```

---

## 🧰 Tech Stack

### AI & Orchestration

* LangGraph
* LangChain
* Groq
* Google GenAI
* Nvidia AI Endpoints

### Backend

* FastAPI
* Pydantic
* Python Dotenv

### Data Processing

* Pandas
* NumPy
* OpenPyXL

### Visualization

* Plotly

### Frontend

* Streamlit

---

## 🎯 Example Queries

Users can interact with their datasets using natural language:

```text
• Show me the top 10 products by revenue.
• Which columns have missing values?
• Create a bar chart of monthly sales.
• What are the average salaries by department?
• Find correlations between numerical features.
• Summarize the key business insights from this dataset.
```

---

## 🌟 Vision

InsightForge aims to make advanced data analytics accessible through conversation, enabling users to transform raw datasets into meaningful insights without writing code.

**Talk to your data. Visualize your story. Forge better decisions.**

---

## 👨‍💻 Author

**Vikas Prajapat**

- GitHub: https://github.com/vintagevikas090

---
