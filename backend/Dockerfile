# Multi-Stage Build for High-Performance Rust Backend
FROM rust:1.80-alpine AS builder

RUN apk add --no-cache musl-dev pkgconfig openssl-dev

WORKDIR /usr/src/app
COPY backend/Cargo.toml backend/Cargo.lock* ./
# Pre-build dependencies layer
RUN mkdir src && echo "fn main() {}" > src/main.rs && cargo build --release || true && rm -rf src

# Copy real sources
COPY backend/src ./src
COPY markdowns /usr/src/markdowns
RUN cargo build --release

# Minimal Runtime Container
FROM alpine:3.20

RUN apk add --no-cache ca-certificates tzdata

WORKDIR /app
COPY --from=builder /usr/src/app/target/release/interview-guide-backend /app/server
COPY markdowns /app/markdowns

ENV MARKDOWNS_DIR=/app/markdowns
ENV PORT=3000
EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD wget -q --spider http://localhost:3000/health || exit 1

CMD ["/app/server"]
