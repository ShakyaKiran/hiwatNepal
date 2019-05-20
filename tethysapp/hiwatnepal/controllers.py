from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from tethys_sdk.gizmos import Button
import decimal
from chartUtils import getForecastData, get_forecastpercent
import requests

# @login_required()
def home(request):
    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text='',
        name='save-button',
        icon='glyphicon glyphicon-floppy-disk',
        style='success',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Save'
        }
    )

    edit_button = Button(
        display_text='',
        name='edit-button',
        icon='glyphicon glyphicon-edit',
        style='warning',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Edit'
        }
    )

    remove_button = Button(
        display_text='',
        name='remove-button',
        icon='glyphicon glyphicon-remove',
        style='danger',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Remove'
        }
    )

    previous_button = Button(
        display_text='Previous',
        name='previous-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Previous'
        }
    )

    next_button = Button(
        display_text='Next',
        name='next-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Next'
        }
    )

    context = {
        'save_button': save_button,
        'edit_button': edit_button,
        'remove_button': remove_button,
        'previous_button': previous_button,
        'next_button': next_button
    }

    return render(request, 'hiwatnepal/home.html', context)

def check_for_decimals(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError

def getGeoJson():
    request_params = dict(cty='nepaRiver')
    request_headers = dict(Authorization='Token 93eae5155d3c551cd5d449e896cf707869b63eb2')
    res = requests.get('http://tethys.icimod.org/apps/apicenter/hiwatAPI/getFeaturesHIWAT', params=request_params,headers=request_headers)
    # print (res.text)
    return(res.text)

def chartHiwat(request):
    return_obj = {}
    try:
        comid =int(request.GET.get('stID'))
    except:
        comid = 57465
    return_obj = getForecastData(comid)
    # print (return_obj)
    return HttpResponse(return_obj, content_type= 'application/json')

def forecastpercent(request):
    if request.is_ajax() and request.method == 'GET':
        comid = request.GET.get('comid')
        return JsonResponse(get_forecastpercent(comid))

def index(request):
    getjson = getGeoJson()
#    print(getjson)
    context = {
        'myJson': getjson
    }
    return render(request, 'hiwatnepal/main.html', context)

