from django import template
import calendar
import json
from django.http import HttpResponse
from app.models import *
from app.views import *

register = template.Library()

@register.filter
def checked_parametre(var):
    print(var)
    audiencia = ['Todos los publicos','Mayores de 18 años','Mayores de 16 años']
    if var in audiencia:
        return 'checked'

@register.filter
def translate_aforo(aforo):
    
    aforo_translate = ''
    if aforo == '':
        aforo_translate = 'Seleccionar aforo'

    elif aforo == '0,150' :
        aforo_translate = 'Menos de 150 personas'
               
    elif aforo == '150,300' :
        aforo_translate = 'De 150 a 300 personas'
               
    elif aforo == '300,800' :
        aforo_translate = 'De 300 a 800 personas'
              
    elif aforo == '800,1400' :
        aforo_translate = 'De 800 a 1400 personas'
                
    elif aforo == '1400,4800' :
        aforo_translate = 'De 1400 a 4800 personas'
                
    elif aforo == '4800,999999' :
        aforo_translate = 'Mayor de 4800 personas'
           
    return aforo_translate

@register.filter
def translate_aforo_inverse(aforo_translate):
    
    aforo = ''
    if  aforo_translate == 'Seleccionar aforo':
        aforo = ''

    elif  aforo_translate == 'Menos de 150 personas':
        aforo = '0,150' 
               
    elif aforo_translate == 'De 150 a 300 personas':
        aforo = '150,300'
                      
    elif aforo_translate == 'De 300 a 800 personas':
        aforo = '300,800'    
              
    elif aforo_translate == 'De 800 a 1400 personas':
        aforo = '800,1400'
                
    elif aforo_translate == 'De 1400 a 4800 personas':
        aforo = '1400,4800'        
              
    elif aforo_translate == 'Mayor de 4800 personas':
        aforo = '4800,999999'       
           
    return aforo

 
