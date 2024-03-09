from django.shortcuts import render
from django.http import JsonResponse
from .models import Mahsulot, Mahsulot_Xomashyo, Omborxona

def get_product_info(request):
    mahsulotlar = Mahsulot.objects.all()
    natijalar = []

    for mahsulot in mahsulotlar:
        mahsulot_info = {
            "mahsulot_nomi": mahsulot.mahsulot_nomi,
            "mahsulot_kodi": mahsulot.mahsulot_kodi,
            "xomashyolar": []
        }

        mahsulot_xomashyolar = Mahsulot_Xomashyo.objects.filter(product_id=mahsulot)
        for mx in mahsulot_xomashyolar:
            xomashyo = mx.material_id
            omborxona_malumotlari = Omborxona.objects.filter(material_id=xomashyo).first()
            xomashyo_info = {
                "xomashyo_nomi": xomashyo.xomashyo_nomi,
                "miqdori": mx.quantity,
                "qolgan_miqdori": omborxona_malumotlari.remainder if omborxona_malumotlari else None,
                "narxi": omborxona_malumotlari.price if omborxona_malumotlari else None
            }
            mahsulot_info["xomashyolar"].append(xomashyo_info)

        natijalar.append(mahsulot_info)

    return JsonResponse({"result": natijalar})
