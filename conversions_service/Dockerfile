FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
 && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> /etc/profile

ENV PATH="/root/.local/bin:${PATH}"

COPY pyproject.toml ./
COPY conversions_service ./conversions_service
COPY scripts ./conversions_service/scripts

RUN poetry install --no-root --without dev

ENV PORT=8000

EXPOSE 8000

CMD ["poetry", "run", "python", "-m", "conversions_service"]