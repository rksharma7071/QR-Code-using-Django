from django.shortcuts import render, redirect
import qrcode
import os

def main(request):
    f = os.path.exists("static/QRCode.png")
    if request.method == "POST":
        url = request.POST.get('url')
        qr_code= qrcode.make(url)
        qr_code.save("static/QRCode.png")

    return render(request, 'main.html', locals())

def del_qrcode(request):
    if os.path.exists("static/QRCode.png"):
        os.remove("static/QRCode.png")
    else:
        print("The file does not exist")
    return redirect(main)


