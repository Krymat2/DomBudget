# 🖥️ Views – Home Budget App

This document describes all the views (controllers) used in the **Home Budget App** Django project.

---

## 1. Main Panel

### `index(request)`
- **URL:** `/`
- **Methods:** GET
- **Description:** Main dashboard. Shows budgets, transactions, total income/expenses, categories, and users in the selected budget. Handles pagination.
- **Context:**
  - `budgets` – list of user budgets
  - `selected_budget` – currently selected budget
  - `current_user` – logged-in user
  - `transactions` – paginated transactions
  - `total_income` – total income in selected budget
  - `total_expenses` – total expenses
  - `users_in_budget` – users in the budget
  - `budget_amount` – budget total
  - `category_expenses` – breakdown of expenses per category

---

## 2. User Management

### `login(request)`
- **URL:** `/login/`
- **Methods:** GET, POST
- **Description:** Logs in a user by validating username and password (hashed).

### `register(request)`
- **URL:** `/register/`
- **Methods:** GET, POST
- **Description:** Registers a new user and hashes the password. Redirects to login.

### `logout_view(request)`
- **URL:** `/logout/`
- **Methods:** GET
- **Description:** Logs out the user and clears the session.

### `edit_profile(request)`
- **URL:** `/edit_profile/`
- **Methods:** GET, POST
- **Description:** Allows the user to edit username, email, and password with validation.

---

## 3. Budget Management

### `create_budget(request)`
- **URL:** `/create_budget/`
- **Methods:** GET, POST
- **Description:** Creates a new budget. Assigns current user and adds 3 default categories.

### `budget_list(request)`
- **URL:** `/budget_list/`
- **Methods:** GET
- **Description:** Lists all budgets of the current user with transactions, remaining budget, and users.

### `add_user_to_budget(request)`
- **URL:** `/add_user_to_budget/`
- **Methods:** GET, POST
- **Description:** Adds a user to a budget via invitation link.

### `accept_invitation(request)`
- **URL:** `/accept_invitation/`
- **Methods:** GET
- **Description:** Accepts a budget invitation using a token.

### `leave_budget(request, budget_id)`
- **URL:** `/leave_budget/<budget_id>/`
- **Methods:** GET
- **Description:** Allows a user to leave a budget. Deletes budget if no users remain.

---

## 4. Transactions

### `add_transaction(request)`
- **URL:** `/add_transaction/`
- **Methods:** GET, POST
- **Description:** Adds a transaction to a selected budget.

### `transaction_detail(request, transaction_id)`
- **URL:** `/transaction/<transaction_id>/`
- **Methods:** GET
- **Description:** Shows detailed information about a transaction.

### `transaction_detail_api(request, pk)`
- **URL:** `/api/transaction/<pk>/`
- **Methods:** GET
- **Description:** Returns transaction data in JSON format.

### `delete_transaction(request, transaction_id)`
- **URL:** `/delete_transaction/<transaction_id>/`
- **Methods:** POST
- **Description:** Deletes a transaction if the user has access.

---

## 5. Category Management

### `create_category(request)`
- **URL:** `/create_category/`
- **Methods:** GET, POST
- **Description:** Creates a new category for budgets the user belongs to.

### `category_list(request)`
- **URL:** `/category_list/`
- **Methods:** GET
- **Description:** Lists categories for the currently selected budget.

### `edit_category(request, pk)`
- **URL:** `/edit_category/<pk>/`
- **Methods:** GET, POST
- **Description:** Edits an existing category. Only budgets the user belongs to are selectable.

### `delete_category(request, pk)`
- **URL:** `/delete_category/<pk>/`
- **Methods:** GET, POST
- **Description:** Deletes a category. User must belong to the associated budget.

### `get_budget_categories(request)`
- **URL:** `/get_budget_categories/`
- **Methods:** GET
- **Description:** Returns categories of a selected budget as JSON.

### `get_budget_users(request)`
- **URL:** `/get_budget_users/`
- **Methods:** GET
- **Description:** Returns list of users for a selected budget as JSON.

---

## 6. PDF & Data Export

### `export_data_view(request)`
- **URL:** `/export_data/`
- **Methods:** GET, POST
- **Description:** Prepares data for PDF export. User can select budget.

### `generate_pdf(request)`
- **URL:** `/generate_pdf/`
- **Methods:** POST
- **Description:** Generates a PDF file containing budget data and transactions.

### `pdf_temp(request)`
- **URL:** `/pdf_temp/`
- **Methods:** GET
- **Description:** Renders the PDF template in browser (for preview purposes).
