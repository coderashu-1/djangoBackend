from django.shortcuts import render
import uuid
# from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from common_fun.models import LoginIdCred
import json
import os
from datetime import datetime
# Create your views here.
from common_fun.models import ImportRegister

class ImportRegisterForm(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)

            with open(os.path.join(os.path.dirname(__file__), "import_register.json"), 'w+') as fl:
                json.dump(data, fl, indent=4)
            
            
            imporRegistertData = {
                "month_year": "",
                "budget_rate": data["budgetRate"],
                "exposure_type": data["exposureType"],
                "exposure_input_date": data["exposureInputDate"],
                "po_date": data["poDate"],
                "bl_date": data["blDate"],
                "due_date": "",
                "priority": "",
                "collection_date": data["collectionDate"],
                "amount": data["amount"],
                "currency": data["currency"],
                "hedged_amount": data["hedgedAmount"],
                "po_no": data["poNo"],
                "party_name": data["partyName"],
                "payment_terms": data["paymentTerms"],
                "booked_forward_rate": data["bookedForwardRate"],
                "bank": data["bank"],
                "forward_contract_no": data["forwardContractNo"],
                "invoice_no": data["invoiceNo"],
                "cretated_date_time": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }
            
            ImportRegister.objects.create(**imporRegistertData)

            return JsonResponse({"message": "Import Register Data saved successfully", "status": "success"}, status=200)
                    
            
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON", "status": "fail"}, status=400)
        except Exception as e:
            return JsonResponse({"message": str(e), "status": "fail"}, status=500)


class ImportRegisterView(APIView):
    def post(self, request):
        try:
            data1 = json.loads(request.body)

            # with open(os.path.join(os.path.dirname(__file__), "export_register_.json"), 'w+') as fl:
            #     json.dump(data, fl, indent=4)
            condition = data1['condition']

            if condition == '':
                importData = ImportRegister.objects.all()
                importDataList = []
                if importData:
                    for row in importData:
                        imporRegistertData = {
                            "budgetRate": row.budget_rate,
                            "exposureType": row.exposure_type,
                            "exposureInputDate": row.exposure_input_date,
                            "poDate": row.po_date,
                            "blDate": row.bl_date,
                            "dueDate": row.due_date,
                            "priority": row.priority,
                            "collectionDate": row.collection_date,
                            "amount": row.amount,
                            "currency": row.currency,
                            "hedgedAmount": row.hedged_amount,
                            "poNo": row.po_no,
                            "partyName": row.party_name,
                            "paymentTerms": row.payment_terms,
                            "bookedForwardRate": row.booked_forward_rate,
                            "bank": row.bank,
                            "forwardContractNo": row.forward_contract_no,
                            "invoiceNo": row.invoice_no
                        }
                        importDataList.append(imporRegistertData)

                    return JsonResponse({"message": "Import Register Data fetched successfully", "status": "success", "data": importDataList}, status=200)
                
                else:
                    return JsonResponse({"message": "Import Register Data fetched successfully", "status": "success", "data": importDataList}, status=200)

            else:
                return JsonResponse({"message": "Invalid condition", "status": "fail"}, status=400)


        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON", "status": "fail"}, status=400)
        except Exception as e:
            return JsonResponse({"message": str(e), "status": "fail"}, status=500)
        