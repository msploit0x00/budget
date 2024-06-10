// // Copyright (c) 2024, ahmed and contributors
// // For license information, please see license.txt

// frappe.ui.form.on("Budget Request", {
//   department(frm) {
//     frappe.call({
//       method: "budget.budge.api.api.get_items_per_department",
//       args: {
//         department: frm.doc.department,
//       },
//       callback(r) {
//         frm.doc.budget_items_details = [];
//         let items = r.message;
//         items.forEach((item) => {
//           frm.add_child("budget_items_details", {
//             item_name: item.name,
//             expense_account: item.expense_account,
//           });
//         });
//         frm.refresh_fields();
//       },
//     });
//   },
//   price_list(frm) {
//     frm.doc.budget_items_details.forEach((item) => {
//       frappe.db
//         .get_value(
//           "Item Price",
//           { item_code: item.item_name, price_list: frm.doc.price_list },
//           "price_list_rate",
//         )
//         .then((r) => {
//           item.expected_price = r.message?.price_list_rate;
//           frm.refresh_field("budget_items_details");
//         });
//     });
//   },
//   before_save(frm) {
//     let months = {
//         january: { quantity: 0, amount: 0 },
//         february: { quantity: 0, amount: 0 },
//         march: { quantity: 0, amount: 0 },
//         april: { quantity: 0, amount: 0 },
//         may: { quantity: 0, amount: 0 },
//         june: { quantity: 0, amount: 0 },
//         july: { quantity: 0, amount: 0 },
//         august: { quantity: 0, amount: 0 },
//         september: { quantity: 0, amount: 0 },
//         october: { quantity: 0, amount: 0 },
//         november: { quantity: 0, amount: 0 },
//         december: { quantity: 0, amount: 0 },
//     };
//     let total_quantity = 0;
//     let total_amount = 0;
    
//     frm.doc.budget_items_details.forEach((item) => {
//         let item_total_quantity = 0;
//         let item_total_amount = 0;

//         for (let month of Object.keys(months)) {
//             item_total_quantity += item[month];
//             item_total_amount += item[month] * item.expected_price;
//             months[month].quantity += item[month];
//             months[month].amount += item[month] * item.expected_price;
//         }

//         item.total = item_total_amount;
//         item.total_quantity = item_total_quantity;

//         if (item.status == "Accepted") {
//             total_quantity += item_total_quantity;
//             total_amount += item_total_amount;
//         }
//     });

//     frm.doc.item_summary = [];
//     for (let month of Object.keys(months)) {
//         frm.add_child("item_summary", {
//             month: month,
//             total: months[month].amount,
//             total_quantity: months[month].quantity,
//         });
//     }

//     frm.doc.total = total_amount;
//     frm.doc.total_quantity = total_quantity;
//     frm.refresh_fields();
// }

