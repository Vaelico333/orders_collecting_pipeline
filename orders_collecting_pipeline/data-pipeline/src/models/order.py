class Order:
    def __init__(self, customer_name, clothing_model, color, size):
        self.customer_name = customer_name
        self.clothing_model = clothing_model
        self.color = color
        self.size = size

    def to_dict(self):
        return {
            "customer_name": self.customer_name,
            "clothing_model": self.clothing_model,
            "color": self.color,
            "size": self.size
        }