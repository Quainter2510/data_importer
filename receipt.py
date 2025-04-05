from dataclasses import dataclass

@dataclass 
class Receipt:
    doc_id: str 
    item: str 
    category: str 
    amount: int 
    price: int 
    discount: int 
    
