from typing import Any, Dict

class CRMTool:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer_id: str, customer_data: Dict[str, Any]) -> str:
        self.customers[customer_id] = customer_data
        return f"Customer {customer_id} added successfully."

    def get_customer(self, customer_id: str) -> Dict[str, Any]:
        return self.customers.get(customer_id, "Customer not found.")

    def update_customer(self, customer_id: str, customer_data: Dict[str, Any]) -> str:
        if customer_id in self.customers:
            self.customers[customer_id].update(customer_data)
            return f"Customer {customer_id} updated successfully."
        return "Customer not found."

    def delete_customer(self, customer_id: str) -> str:
        if customer_id in self.customers:
            del self.customers[customer_id]
            return f"Customer {customer_id} deleted successfully."
        return "Customer not found."