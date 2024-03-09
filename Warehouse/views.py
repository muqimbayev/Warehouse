from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from django.db.models import Sum

# Create your views here.

class MahsulotView(ModelViewSet):
    queryset =Mahsulot.objects.all()
    serializer_class = MahsulotSerializer

class XomashyoView(ModelViewSet):
    queryset = Omborxona.objects.all()
    serializer_class = OmborxonaSerializer

class Mahsulot_XomashyoView(ModelViewSet):
    queryset = Mahsulot_Xomashyo.objects.all()
    serializer_class = Mahsulot_XomashyoSerializer

class OmborxonaView(ModelViewSet):
    queryset = Omborxona.objects.all()
    serializer_class = OmborxonaSerializer

from django.shortcuts import render
from django.http import JsonResponse
from .models import Mahsulot, Mahsulot_Xomashyo, Omborxona


@api_view(['GET'])
def get_product_info(request, name, name_qty):
    mahsulot = Mahsulot.objects.get(mahsulot_nomi=name.lower())
    natijalar = []
    mahsulot_info = {
            "product_name": name,
            "product_qty": name_qty,
            "product_materials": []
    }

    mahsulot_xomashyolar = Mahsulot_Xomashyo.objects.filter(product_id=mahsulot.id)
    for mx in mahsulot_xomashyolar:
            xomashyo = mx.material_id
            qty = mx.quantity

            omborxonalar = Omborxona.objects.filter(material_id=xomashyo).values('material_id').annotate(total_remainder=Sum('remainder'))
            qty_sum = qty * name_qty
            omborxonalar_r = omborxonalar[0]['total_remainder']



            omborxona_malumotlari = Omborxona.objects.filter(material_id=xomashyo).first()
            omborxona_remainder = omborxona_malumotlari.remainder

            remainder_sum = True if omborxonalar_r > qty_sum else False
            qty_sum = qty * name_qty

            omborxona_malumotlari = Omborxona.objects.filter(material_id=xomashyo).first()
            omborxona_remainder = omborxona_malumotlari.remainder
            xomashyo_info = {
                "warehouse_id": xomashyo.id,
                "material_name": xomashyo.xomashyo_nomi,
                "qty": qty_sum,
                "price": omborxona_malumotlari.price if remainder_sum else None
            }
            mahsulot_info["product_materials"].append(xomashyo_info)
    natijalar.append(mahsulot_info)

    return JsonResponse({"result": natijalar})
