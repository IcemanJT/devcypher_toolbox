FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
 && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> /etc/profile

ENV PATH="/root/.local/bin:${PATH}"

# Copy only the project metadata for dependency installation
COPY conversions_service/pyproject.toml conversions_service/poetry.lock* ./conversions_service/

# Switch into the project dir for Poetry
WORKDIR /app/conversions_service

COPY . .

RUN poetry install --no-root --without dev

ENV PORT=8080
ENV ENV=prod
ENV PYTHONPATH=/app

EXPOSE 8080

CMD [ "/bin/bash", "ls"]
CMD ["poetry", "run", "python", "conversions_service/app.py"]