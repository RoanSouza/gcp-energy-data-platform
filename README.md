# ⚡ Plataforma de Dados de Energia na GCP

Este projeto simula uma **arquitetura completa de dados na Google Cloud Platform (GCP)** para o setor de energia.  
O objetivo é demonstrar **boas práticas de engenharia de dados**, desde ingestão até consumo.

---

## 🚀 Arquitetura

![Arquitetura GCP](architecture/gcp_architecture.png)

---

## 🔧 Tecnologias Utilizadas

- **Google Cloud Platform (GCP)**
  - Cloud Storage
  - BigQuery
  - Dataflow
  - Pub/Sub
  - Vertex AI
- **Python** (ETL e manipulação de dados)
- **SQL** (queries no BigQuery)
- **Airflow** (orquestração de pipelines)
- **Looker Studio** (visualização de dashboards)

---

## 📂 Estrutura do Projeto

- `notebooks/` → Scripts e notebooks em Python para ingestão e tratamento.  
- `sql/` → Queries usadas no BigQuery.  
- `airflow/` → DAGs de orquestração do pipeline de dados.  
- `dashboards/` → Dashboards criados no Looker Studio.  
- `architecture/` → Diagramas da arquitetura do projeto.  

---

## 🔄 Fluxo de Dados

1. **Ingestão** de dados de energia (histórico dos últimos 4 anos).  
2. **Armazenamento** no **Cloud Storage** (camada *raw*).  
3. **Transformação** via **Dataflow** e **BigQuery** (camadas *trusted* e *refined*).  
4. **Machine Learning** aplicado no **Vertex AI** para previsão de consumo.  
5. **Consumo** via dashboards no **Looker Studio** e API.  

---

## 📊 Exemplo de Dashboard

![Dashboard Energia](dashboards/energy_dashboard.png)

---

## ✨ Resultados

- Simulação de arquitetura real de dados em nuvem.  
- Aplicação de **boas práticas de camadas de dados (raw, trusted, refined)**.  
- Pipeline pronto para escalar e suportar novos dados.  
