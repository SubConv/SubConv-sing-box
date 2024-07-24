FROM --platform=$BUILDPLATFORM python:3.11.8-alpine3.19 AS builder
LABEL name="subconv-sing-box"

WORKDIR /app

COPY . .

# Install dependencies
RUN apk add --update-cache ca-certificates tzdata patchelf clang ccache

# Insall python and dependencies
RUN pip3 install -r requirements.txt && \
    pip3 install nuitka

# Use nuikta to compile the python code
RUN --mount=type=cache,target=/root/.cache/Nuitka \
    python3 -m nuitka --clang --onefile --standalone main.py && \
    chmod +x main.bin


FROM alpine

WORKDIR /app

COPY --from=builder /app/main.bin /app/main.bin
COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY static /app/static
COPY config.json /app/config.json

EXPOSE 8080

ENTRYPOINT ["/app/main.bin"]