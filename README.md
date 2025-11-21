# bbc-news-etl-pipeline

ETL pipeline en Python para extraer noticias desde BBC Mundo, procesarlas y almacenarlas en una base de datos **PostgreSQL en Azure**. Incluye scraping, transformaciones mínimas, control de versiones de artículos, y tracking/auditoría de ejecuciones (schema `etl_logs`).

> **Atención**: respeta `robots.txt` y políticas de uso de BBC antes de ejecutar scraping en producción.

## Contenido
- `etl/` — código del pipeline (extract, transform, load, orchestrator)
- `utils/` — utilidades (conexión a BD, logging)
- `sql/` — scripts para crear schemas y tablas
- `.github/workflows/run_pipeline.yml` — workflow para ejecutar cada hora (usar GitHub Secrets)

## Requisitos
- Python 3.10+
- Azure Database for PostgreSQL (o PostgreSQL compatible)
- GitHub repository (para usar Actions)

## Instalación local (prueba)
1. Crear las tablas en tu BD:
   - Ejecuta `sql/create_schemas.sql` y `sql/create_tables.sql` en tu servidor PostgreSQL.

2. Crear Secrets en GitHub (si vas a usar Actions):
   - `AZURE_PG_HOST`
   - `AZURE_PG_PORT` (opcional, default 5432)
   - `AZURE_PG_DB`
   - `AZURE_PG_USER`
   - `AZURE_PG_PASSWORD`

3. (Opcional local) Exportar variables de entorno equivalentes si pruebas localmente:
```bash
export AZURE_PG_HOST="tu-host.postgres.database.azure.com"
export AZURE_PG_USER="usuario"
export AZURE_PG_PASSWORD="password"
export AZURE_PG_DB="mi_bd"
export AZURE_PG_PORT="5432"
