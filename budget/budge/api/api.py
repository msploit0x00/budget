import frappe
from frappe import _
#import frappe
#from itertools import groupby
#from operator import itemgetter

@frappe.whitelist()
def get_items_per_department(department):
    item = frappe.qb.DocType("Item")
    item_department = frappe.qb.DocType("Item Department")
    item_default = frappe.qb.DocType("Item Default")
    items = frappe.qb.from_(item).join(item_department).on(
        item_department.parent == item.name).join(item_default).on(
            item.name == item_default.parent).select(
                item.name, item_default.expense_account,item.custom_item_category).where(
                    item_department.department == department).where(
                        item.custom_is_budget == 1).distinct().run(
                            as_dict=True)
    sorted_items = sorted(items, key=lambda x:(x['custom_item_category'] is None, x['custom_item_category']))
    return sorted_items

@frappe.whitelist()
def get_expected_price(item_name, price_list):
    expected = frappe.get_doc("")
