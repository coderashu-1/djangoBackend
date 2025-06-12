from django.db import models
# from mongoengine import Document, DynamicField, ListField

# Create your models here.

# class LoginIdCred(Document):
#     login_id = DynamicField()
#     login_password = DynamicField()
#     login_type = DynamicField()

#     def __str__(self):
#         return f"Invoice {self.login_id} - {self.login_password}"
    
#     meta = {
#         'collection': 'login_id_cred'
#     }

# class Dashboard(Document):
#     particular = DynamicField()
#     overdue_Exposure_less_than_apr_25 = DynamicField()
#     q1_apr_25_jun_25 = DynamicField()
#     q2_jul_25_sep_25 = DynamicField()
#     q3_oct_25_dec_25 = DynamicField()
#     q4_jan_25_mar_26 = DynamicField()
#     total = DynamicField()
    


class LoginIdCred(models.Model):
    id = models.AutoField(primary_key=True)
    login_id = models.TextField(null=True, blank=True)
    login_password = models.TextField(null=True, blank=True)
    login_type = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Invoice {self.login_id} - {self.login_password}"
    
    class Meta:
        db_table = "login_id_cred"

class ExportRegister(models.Model):
    id = models.AutoField(primary_key=True)
    month_year = models.TextField(null=True, blank=True)
    exposure_type = models.TextField(null=True, blank=True)
    exposure_input_date = models.TextField(null=True, blank=True)
    po_date = models.TextField(null=True, blank=True)
    bl_date = models.TextField(null=True, blank=True)
    collection_date = models.TextField(null=True, blank=True)
    amount = models.TextField(null=True, blank=True)
    adjustment_amount = models.TextField(null=True, blank=True)
    currency = models.TextField(null=True, blank=True)
    budget_rate = models.TextField(null=True, blank=True)
    hedged_amount = models.TextField(null=True, blank=True)
    invoice_no = models.TextField(null=True, blank=True)
    po_no = models.TextField(null=True, blank=True)
    party_name = models.TextField(null=True, blank=True)
    bank = models.TextField(null=True, blank=True)
    payment_terms = models.TextField(null=True, blank=True)
    forward_contract_no = models.TextField(null=True, blank=True)
    priority = models.TextField(null=True, blank=True)
    booked_forward_rate = models.TextField(null=True, blank=True)
    remark = models.TextField(null=True, blank=True)
    cretated_date_time = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "export_register"



class ImportRegister(models.Model):
    id = models.AutoField(primary_key=True)
    month_year = models.TextField(null=True, blank=True)
    budget_rate = models.TextField(null=True, blank=True)
    exposure_type = models.TextField(null=True, blank=True)
    exposure_input_date = models.TextField(null=True, blank=True)
    po_date = models.TextField(null=True, blank=True)
    bl_date = models.TextField(null=True, blank=True)
    due_date = models.TextField(null=True, blank=True)
    collection_date = models.TextField(null=True, blank=True)
    amount = models.TextField(null=True, blank=True)
    currency = models.TextField(null=True, blank=True)
    hedged_amount = models.TextField(null=True, blank=True)
    po_no = models.TextField(null=True, blank=True)
    party_name = models.TextField(null=True, blank=True)
    payment_terms = models.TextField(null=True, blank=True)
    booked_forward_rate = models.TextField(null=True, blank=True)
    bank = models.TextField(null=True, blank=True)
    forward_contract_no = models.TextField(null=True, blank=True)
    invoice_no = models.TextField(null=True, blank=True)
    priority = models.TextField(null=True, blank=True)
    cretated_date_time = models.TextField(null=True, blank=True)
    

    class Meta:
        db_table = "import_register"



    