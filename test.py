
from common_fun.models import LoginIdCred

from mongoengine import connect

connect(
    db='stock_dashboard',
    host='localhost',
    port=27017,
    alias='default'  # <--- THIS IS MANDATORY
)


# Create user (only for testing)
# user = LoginIdCred(
#     login_id="customer",
#     login_password="customer123123",
#     login_type="customer"
# )
# user.save()  # This will create the collection in MongoDB

# particular = DynamicField()
# overdue_Exposure_less_than_apr_25 = DynamicField()
# q1_apr_25_jun_25 = DynamicField()
# q2_jul_25_sep_25 = DynamicField()
# q3_oct_25_dec_25 = DynamicField()
# q4_jan_25_mar_26 = DynamicField()
# total = DynamicField()

{
    "exposure_type": "exposureType",
    "exposure_input_date": "exposureInputDate",
    "po_date": "poDate",
    "bl_date": "blDate",
    "collection_date": "collectionDate",
    "amount": "amount",
    "adjustment_amount": "adjustmentAmount",
    "currency": "currency",
    "budget_rate": "budgetRate",
    "hedged_amount": "hedgedAmount",
    "invoice_no": "invoiceNo",
    "po_no": "poNo",
    "party_name": "partyName",
    "bank": "bank",
    "payment_terms": "paymentTerms",
    "forward_contract_no": "forwardContractNo",
    "priority": "priority",
    "booked_forward_rate": "bookedForwardRate",
    "remark": "remark",
}

{
    "budgetRate": 23,
    "exposureType": "shipment",
    "exposureInputDate": "2025-06-07",
    "poDate": "2025-06-12",
    "blDate": "2025-06-25",
    "collectionDate": "2025-06-21",
    "amount": 223,
    "currency": "IND",
    "hedgedAmount": 556,
    "poNo": "234234",
    "partyName": "name",
    "paymentTerms": "terms",
    "bookedForwardRate": 3554,
    "bank": "bank name",
    "forwardContractNo": "3259887478",
    "invoiceNo": "asdqwd34213"
}

{
    "budget_rate": 23,
    "exposure_type": "shipment",
    "exposure_input_date": "2025-06-07",
    "po_date": "2025-06-12",
    "bl_date": "2025-06-25",
    "collection_date": "2025-06-21",
    "amount": 223,
    "currency": "IND",
    "hedged_amount": 556,
    "po_no": "234234",
    "party_name": "name",
    "payment_terms": "terms",
    "booked_forward_rate": 3554,
    "bank": "bank name",
    "forward_contract_no": "3259887478",
    "invoice_no": "asdqwd34213"
}