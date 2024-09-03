# Copyright (c) 2024, Mohsan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Attendee(Document):
    # after insert to make sure we have already inserted the attendee in our database
	def after_insert(self):
		eventlog = frappe.get_doc({
			"doctype": "EventLog",
			"action": "Attendee Added",
			"event": self.event,
			"description": f"{self.customer} is attending the {self.event}"
		})
		eventlog.insert()
		event = frappe.get_doc("Events", self.event)
		event.total_attendees += 1
		event.save()
	
	def after_delete(self):
		eventlog = frappe.get_doc({
			"doctype": "EventLog",
			"action": "Attendee Removed",
			"event": self.event,
			"description": f"{self.customer} is removed from this event: {self.event}"
		})
		eventlog.insert()
		event = frappe.get_doc("Events", self.event)
		event.total_attendees -= 1
		event.save()
