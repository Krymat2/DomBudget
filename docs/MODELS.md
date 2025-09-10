# 🏗️ Models – Home Budget App

This document describes the database models used in the **Home Budget App** Django project.

---

## 1. `Uzytkownicy`

Represents the users of the application.

| Field       | Type               | Description                         |
|------------|------------------|-------------------------------------|
| id         | AutoField         | Primary key                         |
| username   | CharField(150)    | Unique username                     |
| email      | EmailField        | Unique email address                |
| password   | CharField(128)    | User password (hashed)              |
| created_at | DateTimeField     | Timestamp of account creation       |

**String representation:** `username`

---

## 2. `Budzety`

Represents budgets that can be shared between users.

| Field          | Type               | Description                                        |
|----------------|------------------|--------------------------------------------------|
| id             | AutoField         | Primary key                                      |
| name           | CharField(100)    | Name of the budget                               |
| budget_amount  | DecimalField(10,2)| Total budget amount                              |
| date           | DateField         | Creation date / default today                    |
| users          | ManyToManyField   | Users associated with this budget (through `UzytkownikBudzetPolaczenia`) |

**Methods:**
- `users_list()` – Returns a comma-separated list of usernames in the budget  
- `get_total_transactions(user)` – Calculates total transactions for a given user and budget  

**String representation:** `"{name}({id})"`

---

## 3. `Kategorie`

Represents categories for transactions.

| Field          | Type          | Description                               |
|----------------|--------------|-------------------------------------------|
| id             | AutoField    | Primary key                               |
| category_name  | CharField(100)| Name of the category                      |
| budget         | ForeignKey   | Budget this category belongs to (nullable)|

**String representation:** `category_name`

---

## 4. `Transakcje`

Represents financial transactions.

| Field           | Type          | Description                              |
|-----------------|--------------|------------------------------------------|
| id              | AutoField    | Primary key                              |
| budget          | ForeignKey   | Related budget (cannot be null)          |
| category        | ForeignKey   | Related category (nullable)              |
| amount          | DecimalField | Transaction amount                        |
| transaction_date| DateField    | Date of transaction (auto now add)       |
| description     | TextField    | Optional description of the transaction |
| user            | ForeignKey   | User who performed the transaction       |

**String representation:** `"{amount} by {user} on {transaction_date}"`

---

## 5. `UzytkownikBudzetPolaczenia`

Intermediate table to define user roles in a budget.

| Field   | Type        | Description                    |
|---------|------------|--------------------------------|
| id      | AutoField  | Primary key                    |
| user    | ForeignKey | Linked user                    |
| budget  | ForeignKey | Linked budget                  |
| role    | CharField  | User role: "owner", "editor", "viewer" |

**Meta:** Unique together constraint on `(user, budget)`

**String representation:** `"{user} - {budget} as {role}"`

---

## 6. `BudgetInvitation`

Represents invitations to join a budget.

| Field       | Type         | Description                               |
|------------|-------------|-------------------------------------------|
| budget     | ForeignKey  | Budget the invitation is for               |
| token      | CharField(64)| Unique invitation token                   |
| created_at | DateTimeField| Timestamp of creation                      |
| accepted   | BooleanField | Whether the invitation has been accepted |

---

This model documentation helps developers understand the database schema, relationships, and purpose of each model in the project.
