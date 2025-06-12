FROM python:3.13-slim-bookworm AS base

RUN apt-get update && \
    apt-get install -yqq curl dumb-init \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

FROM base AS builder

COPY --from=ghcr.io/astral-sh/uv:0.4.9 /uv /bin/uv

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

WORKDIR /app

COPY uv.lock pyproject.toml /app/

RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --frozen --no-install-project --no-dev

COPY . /app/

RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --frozen --no-dev

FROM base AS runner

WORKDIR /app

COPY --from=base /usr/bin/dumb-init /usr/bin/dumb-init
COPY --from=builder /app /app

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH=/app/src

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

CMD ["python", "-m", "scrap_generator.server"]