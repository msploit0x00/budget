# Copyright (c) 2024, ahmed and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BudgetRequest(Document):
    pass
#     def on_submit(self):
#         # Create a new Monthly Distribution document
#         monthly_distribution = frappe.new_doc("Monthly Distribution")
#         monthly_distribution.distribution_id = f"{self.name}-{self.fiscal_year}"
#         monthly_distribution.fiscal_year = self.fiscal_year
#         monthly_distribution.percentages = self.get_months()
#         monthly_distribution.save()

#         # Create a new Budget document
#         budget = frappe.new_doc("Budget")
#         budget.budget_against = "Cost Center"
#         budget.monthly_distribution = monthly_distribution.name
#         budget.cost_center = self.cost_center
#         budget.fiscal_year = self.fiscal_year
#         budget.applicable_on_material_request = 1
#         budget.applicable_on_purchase_order = 1
#         budget.applicable_on_booking_actual_expenses = 1
#         budget.action_if_annual_budget_exceeded_on_mr = "Stop"
#         budget.action_if_annual_budget_exceeded_on_po = "Stop"
#         budget.action_if_accumulated_monthly_budget_exceeded_on_mr = "Warn"
#         budget.action_if_accumulated_monthly_budget_exceeded_on_po = "Warn"

#         account_budget = self.calculate_account_budget()
#         budget.accounts = account_budget
#         budget.save()

#     def get_months(self):
#         month_list = [
#             "January", "February", "March", "April", "May", "June", "July",
#             "August", "September", "October", "November", "December"
#         ]
#         total = float(self.total) if self.total else 0
#         percentages = [{
#             "percentage_allocation": item.get("custom_ratio_", 0),
#             "month": month_list[m]
#         } for m, item in enumerate(self.item_summary)]
#         return percentages

#     def calculate_account_budget(self):
#         total_per_account = {}
#         for item in self.budget_items_details:
#             if item.status == "Accepted":
#                 total_per_account[item.expense_account] = total_per_account.get(item.expense_account, 0) + item.total

#         return [{
#             "account": account,
#             "budget_amount": amount
#         } for account, amount in total_per_account.items()]





# @frappe.whitelist()
# def create_budget():
#     try:
#         # Load the document using Frappe's API
#         doc = frappe.get_doc("Budget Request", 'f3b9e494e2')

#         # Create a new Monthly Distribution document
#         monthly_distribution = frappe.new_doc("Monthly Distribution")
#         monthly_distribution.distribution_id = f"{doc.name}-{doc.fiscal_year}"
#         monthly_distribution.fiscal_year = doc.fiscal_year
#         monthly_distribution.percentages = doc.get_months()
#         monthly_distribution.save()

#         # Create a new Budget document
#         budget = frappe.new_doc("Budget")
#         budget.budget_against = "Cost Center"
#         budget.monthly_distribution = monthly_distribution.name
#         budget.cost_center = doc.cost_center
#         budget.fiscal_year = doc.fiscal_year
#         budget.applicable_on_material_request = 1
#         budget.applicable_on_purchase_order = 1
#         budget.applicable_on_booking_actual_expenses = 1
#         budget.action_if_annual_budget_exceeded_on_mr = "Stop"
#         budget.action_if_annual_budget_exceeded_on_po = "Stop"
#         budget.action_if_accumulated_monthly_budget_exceeded_on_mr = "Warn"
#         budget.action_if_accumulated_monthly_budget_exceeded_on_po = "Warn"

#         account_budget = doc.calculate_account_budget()
#         budget.accounts = account_budget
#         budget.save()
#     except Exception as e:
#         # Log any errors that occur
#         frappe.log_error(f"Error in create_budget: {e}", "create_budget")
#         print(f"Error in create_budget: {e}")






