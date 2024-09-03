import frappe

@frappe.whitelist(methods=["GET"])
def get_attendees():
    event_name = frappe.request.args.get("event")
    if not event_name:
        return {"status_code": 404, "message": "Please provide event name"}
    
    attendee = frappe.get_list(doctype="Attendee", filters={"event": event_name}, fields=["customer"])
    return attendee

@frappe.whitelist(methods=["GET"])
def attend_event():
    event_name = frappe.request.args.get("event")
    customer_name = frappe.request.args.get("customer")
    if not event_name:
        return {"status_code": 404, "message": "Please provide event name"}
    new_attendee = frappe.get_doc({
        "doctype": "Attendee",
        "event": event_name,
        "customer": customer_name
    })
    try:
        new_attendee.insert()
        return {
            "status_code": 200,
            "message": "Attendee successfully added"
        }
    except:
        return {
            "status_code": 400,
            "message": "Attendee cannot be added"
        }
    
    