# ARCHITECTURE.md

# Real-Time Payment Fraud Detection System

---

# Overview

This project simulates a production-style payment gateway capable of processing transactions and detecting fraudulent activity asynchronously.

---

# High-Level Architecture

Client

↓

FastAPI

↓

Authentication

↓

PostgreSQL

↓

Kafka Producer

↓

Kafka Topic

↓

Kafka Consumer

↓

Fraud Detection Service

↓

Isolation Forest Model

↓

Update Transaction Status

↓

Client checks transaction status

---

# Components

## Client

Sends payment requests.

Examples

- Mobile App
- Web Application

---

## FastAPI

Responsibilities

- Authentication
- Request Validation
- REST APIs
- Publish Kafka Events

---

## PostgreSQL

Stores

- Users
- Transactions
- Fraud Scores

---

## Kafka

Acts as a message broker.

Allows asynchronous processing.

---

## Fraud Detection Service

Consumes transaction events.

Runs ML prediction.

Updates transaction status.

---

# Database Design

## User

- id
- username
- email
- password_hash
- created_at

---

## Transaction

- id
- user_id
- amount
- merchant
- merchant_category
- currency
- location
- status
- fraud_score
- created_at
- updated_at

---

# Transaction Status Flow

PENDING

↓

PROCESSING

↓

COMPLETED

or

↓

FRAUD

or

↓

FAILED

---

# API Design

Authentication

POST /auth/register

POST /auth/login

---

Transactions

POST /transactions

GET /transactions

GET /transactions/{id}

GET /transactions/{id}/status

---

# Folder Responsibilities

api/

Defines API routes.

---

services/

Contains business logic.

---

models/

Database tables.

---

schemas/

Request and response validation.

---

db/

Database connection.

---

core/

Configuration and security.

---

utils/

Helper functions.

---

# Why This Architecture?

- Separation of Concerns
- Scalable
- Easy to Maintain
- Interview Friendly
- Production Inspired

---

# Future Scope

- Redis
- WebSockets
- Prometheus
- Grafana
- Kubernetes
- CI/CD
- API Gateway
- OAuth2