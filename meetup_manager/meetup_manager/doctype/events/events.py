# Copyright (c) 2024, Mohsan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime

class Events(Document):
	def validate(self):
		event_date = self.event_date
  
		if type(event_date) is 'str':
			event_date = datetime.strptime(self.event_date, "%Y-%m-%d %H:%M:%S")
		if  event_date < datetime.now():
			frappe.throw("Event date should be in the future")
	
	def before_cancel(self):
		eventlog = frappe.get_doc({
			"doctype": "EventLog",
			"event": self.name,
			"action": "Event Canceled",
			"description": f"{self.event_name} Has been cancled and email has been sent to Users"
		})
  
		eventlog.insert()
		
		