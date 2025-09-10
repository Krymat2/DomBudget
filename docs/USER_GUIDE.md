# 📝 Home Budget App – User Guide

This guide explains how to use the **Home Budget App** step by step.

---

## 1. Registration and Login

### Register
1. Go to the **Register** page: `/register/`
2. Fill in your **username**, **email**, and **password**.
3. Click **Register**.
4. If registration is successful, you can log in.

### Login
1. Go to the **Login** page: `/login/`
2. Enter your **username** and **password**.
3. Click **Login**.
4. You will be redirected to the **Main Panel**.

### Logout
1. Click **Log out** in the user menu (top-right corner).
2. Session will be cleared.

> **Note:** Users who are not logged in will be automatically redirected to the login page, where they can either log in or register.


---

## 2. Main Panel

The **Main Panel** (`/`) shows:
- Your budget
- Recent transactions of selected budget
- Total income and expenses
- Users in the selected budget
- Expense breakdown by category

You can:
- Switch between budgets using the budget dropdown
- View paginated transactions
- Navigate to budget, category, and transaction management pages

---

## 3. Budget Management

### Create Budget
1. Go to **Create Budgets**: `/create_budget/`
2. Fill in the **budget name** and **amount**.
3. Click **Save**.
4. Three default categories are automatically added:
   - Daily Expenses
   - Personal
   - Subscriptions

### View Budgets
1. Go to **Show Budgets**: `/budget_list/`
2. See all budgets you belong to, remaining amounts, and users.

### Add Users to Budget
1. Go to **Add User to Budget**: `/add_user_to_budget/`
2. Select a budget.
3. Generate invitation link and send it to a user.
4. Users can click the link to join the budget.

### Leave Budget
1. On the **Show Budgets** page, click **Leave Budget**.
2. You will be removed from the budget. If no users remain, the budget is deleted.

---

## 4. Category Management

### Create Category
1. Go to **Create Category**: `/create_category/`
2. Select a budget you belong to.
3. Enter **category name** and click **Save**.

### View Categories
1. Go to **Show Categories**: `/category_list/`
2. See all categories for the selected budget.

### Edit Category
1. Click **Edit** next to a category.
2. Modify the name or budget assignment (only budgets you belong to).
3. Click **Save**.

### Delete Category
1. Click **Delete** next to a category.
2. Confirm deletion.

---

## 5. Transaction Management

### Add Transaction
1. Go to **Add Transactions**: `/add_transaction/`
2. Select a budget and category.
3. Enter **amount** (positive for income, negative for expenses) and **description**.
4. Click **Save**.

### View Transaction Details
1. Click on a transaction in **Main Panel** or **Budget List**.
2. View full details including user, date, category, and amount.

### Delete Transaction
1. On the transaction detail page, click **Delete**.
2. Confirm deletion.

---

## 6. Export & PDF Reports

### Export Data
1. Go to **Export Data**: `/export_data/`
2. Select a budget.
3. Click **Generate PDF**.
4. Download the PDF report containing:
   - Transactions
   - Users in the budget
   - Expense breakdown by category

### PDF Preview
1. Go to **PDF Temp**: `/pdf_temp/`  
2. View the PDF in the browser before exporting.

---

## 7. Profile Management

### Edit Profile
1. Go to **Edit Profile**: `/edit_profile/`
2. Change **username**, **email**, or **password**.
3. Click **Save Changes**.
4. Confirmation message will appear if successful.

---

## Tips
- Only budgets you belong to are visible and editable.
- Categories must belong to a budget.
- Passwords must be at least 6 characters long.
- Users cannot access transactions of budgets they do not belong to.
