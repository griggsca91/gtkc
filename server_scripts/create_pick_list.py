frappe.msgprint("testing");
#frappe.msgprint(json.dumps(frappe.form_dict))

doc_string = frappe.form_dict["doc"]

doc = json.loads(doc_string)

gifts = []

frappe.msgprint(json.dumps(doc["gifts"]))

for raw_gift in doc["gifts"]:
    gift = {
      "item_code": raw_gift["item_code"],
      "qty": raw_gift["qty"],
      "warehouse": raw_gift["warehouse"],
    }
    frappe.msgprint(gift["item_code"])
    frappe.msgprint(gift["qty"])
    frappe.msgprint(gift["warehouse"])


customer = doc["customer"]

frappe.msgprint(doc["order_type"])

frappe()()
