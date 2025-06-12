# scrap-generator

Gerador de métricas Prometheus customizado em Python, inspirado no Avalanche, mas com foco em:

- Baixo consumo de recursos
- Flexibilidade de geração
- Suporte a churn de séries
- Controle de randomização de valores via configuração

---

## 📦 Tecnologias

- Python 3.13+
- FastAPI
- Uvicorn
- Pydantic v2 (pydantic-settings)
- Clean Code & SOLID design
- Docker (multi-stage com `uv`)

---

## 🔧 Configuração

As variáveis de ambiente podem ser configuradas com prefixo `SG_`. Exemplo:

| Variável            | Descrição                                         |    Default    |
|---------------------|---------------------------------------------------|---------------|
| `SG_PORT`           | Porta do servidor HTTP                            | `9001`        |
| `SG_SERIES_COUNT`   | Quantidade de séries a gerar                      | `100`         |
| `SG_METRIC_NAME`    | Nome da métrica                                   | `test_metric` |
| `SG_LABELS_COUNT`   | Quantidade de labels por série                    | `3`           |
| `SG_CHURN_INTERVAL` | Intervalo de churn (0 = sem churn)                | `0`           |
| `SG_STATIC_VALUES`  | Desabilita randomização de valores (`true/false`) | `true`        |

Exemplo de `.env`:

```dotenv
SG_SERIES_COUNT=1000000
SG_STATIC_VALUES=false
SG_CHURN_INTERVAL=3600
```

---

## 🚀 Execução local

### Ativando o ambiente virtual

python -m venv .venv
source .venv/bin/activate
uv sync

### Rodando o servidor

```bash 
uvicorn scrap_generator.server:app --reload --host 0.0.0.0 --port 9001
```

---

## 🐳 Docker

### Build da imagem

```bash
docker build -t scrap-generator .
```

### Rodando via Docker

```bash
docker run -p 9001:9001 scrap-generator
```

---

## 🔬 Endpoints

- `GET /metrics` → Exposição no formato Prometheus exposition.

---

## 📈 Exemplo de resposta

test_metric{label0="val0",label1="val1",label2="val2",series_id="0"} 87.23
test_metric{label0="val0",label1="val1",label2="val2",series_id="1"} 45.67
...

---

## 💡 Objetivo

Simular cargas realistas de scraping Prometheus, incluindo:

- Volume alto de séries (`series_count`)
- Churn controlado de séries (`churn_interval`)
- Randomização ou estabilidade de valores (`static_values`)
- Configuração simples via env

---

## 📂 Estrutura do projeto

```plaintext
src/
  scrap_generator/
    app.py
    server.py
    config.py
    generator/
      generator.py
      churn.py
      label_generator.py
    routes/
      metrics.py
```

---

✅ Pronto para ser usado em testes com Prometheus Agent, Grafana Mimir, etc.