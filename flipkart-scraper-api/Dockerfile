# Stage 1: Build the application
FROM docker.io/rust:1.73-slim-bullseye AS builder
WORKDIR /usr/src/flipkart-scraper-api

# Install necessary dependencies
RUN apt update && apt install -y libssl-dev

# Set environment variables
ENV DEPLOYMENT_URL=0.0.0.0:3000
ENV OPENSSL_LIB_DIR=/usr/lib/x86_64-linux-gnu
ENV OPENSSL_INCLUDE_DIR=/usr/include

# Copy source code and build the application
COPY Cargo.toml .
COPY ./src/ ./src
RUN cargo build --release

# Stage 2: Create the final image
FROM docker.io/debian:bullseye-slim

# Install necessary runtime dependencies
RUN apt update && apt install -y ca-certificates

WORKDIR /usr/local/bin/

# Copy the built application from the builder stage
COPY --from=builder /usr/src/flipkart-scraper-api/target/release/flipkart-scraper-api .

# Expose the application's port and set the entrypoint
EXPOSE 3000
CMD ["flipkart-scraper-api"]
