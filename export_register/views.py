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
from common_fun.models import ExportRegister

class ExportRegisterForm(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)

            with open(os.path.join(os.path.dirname(__file__), "export_register.json"), 'w+') as fl:
                json.dump(data, fl, indent=4)

            
            exporRegistertData = {
                "month_year": "",
                "exposure_type": data["exposureType"],
                "exposure_input_date": data["exposureInputDate"],
                "po_date": data["poDate"],
                "bl_date": data["blDate"],
                "collection_date": data["collectionDate"],
                "amount": data["amount"],
                "adjustment_amount": data["adjustmentAmount"],
                "currency": data["currency"],
                "budget_rate": data["budgetRate"],
                "hedged_amount": data["hedgedAmount"],
                "invoice_no": data["invoiceNo"],
                "po_no": data["poNo"],
                "party_name": data["partyName"],
                "bank": data["bank"],
                "payment_terms": data["paymentTerms"],
                "forward_contract_no": data["forwardContractNo"],
                "priority": data["priority"],
                "booked_forward_rate": data["bookedForwardRate"],
                "remark": data["remark"],
                "cretated_date_time": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }

            ExportRegister.objects.create(**exporRegistertData)

            return JsonResponse({"message": "Export Register Data saved successfully", "status": "success"}, status=200)
                    
            
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON", "status": "fail"}, status=400)
        except Exception as e:
            return JsonResponse({"message": str(e), "status": "fail"}, status=500)


class ExportRegisterView(APIView):
    def post(self, request):
        try:
            data1 = json.loads(request.body)

            # with open(os.path.join(os.path.dirname(__file__), "export_register_.json"), 'w+') as fl:
            #     json.dump(data, fl, indent=4)
            condition = data1['condition']

            if condition == '':
                exportData = ExportRegister.objects.all()
                exportDataList = []
                if exportData:
                    for row in exportData:
                        exporRegistertData = {
                            "exposureType": row.exposure_type,
                            "exposureInputDate": row.exposure_input_date,
                            "poDate": row.po_date,
                            "blDate": row.bl_date,
                            "collectionDate": row.collection_date,
                            "amount": row.amount,
                            "adjustmentAmount": row.adjustment_amount,
                            "currency": row.currency,
                            "budgetRate": row.budget_rate,
                            "hedgedAmount": row.hedged_amount,
                            "invoiceNo": row.invoice_no,
                            "poNo": row.po_no,
                            "partyName": row.party_name,
                            "bank": row.bank,
                            "paymentTerms": row.payment_terms,
                            "forwardContractNo": row.forward_contract_no,
                            "priority": row.priority,
                            "bookedForwardRate": row.booked_forward_rate,
                            "remark": row.remark,
                        }
                        exportDataList.append(exporRegistertData)

                    return JsonResponse({"message": "Export Register fetched successfully", "status": "success", "data": exportDataList}, status=200)
                
                else:
                    return JsonResponse({"message": "Export Register fetched successfully", "status": "success", "data": exportDataList}, status=200)


            else:
                return JsonResponse({"message": "Invalid condition", "status": "fail"}, status=400)


        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON", "status": "fail"}, status=400)
        except Exception as e:
            return JsonResponse({"message": str(e), "status": "fail"}, status=500)
        