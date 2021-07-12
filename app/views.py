# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import json
import itertools
import mysql.connector
from app.filters import *
from app.query import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from pymongo import MongoClient
from datetime import date, datetime, timedelta
import numpy as np
import random
from geopy.geocoders import GoogleV3, Nominatim





conn = MongoClient('mongodb+srv://inaki:123aA456@cluster0.qli5i.mongodb.net/d3_data?retryWrites=true&w=majority')

mydb = mysql.connector.connect(
    host="bpyzbzunzrblg9epu4fq-mysql.services.clever-cloud.com",
    user="umkpqgglbv86bt2b",
    password="Z4ywID6qw12VvND6F54T",
    database="bpyzbzunzrblg9epu4fq"
    )

#funcion para abrir un cursor y realizar una query
def query_db(query, args=(), one=False):
    cur = mydb.cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    
    return (r[0] if r else None) if one else r

#funcion para conseguir un array con todos los dias entre las fechas señaladas.
def range_dates(date_inicio, date_fin):
    date_format = "%Y-%m-%d"
    a = datetime.strptime(date_inicio, date_format)
    b = datetime.strptime(date_fin, date_format)
    delta = b - a
    days_array = []
    json_array_days = []
    for i in range(delta.days + 1):
        day = a + timedelta(days=i)
        day_format = datetime.strptime(str(day), '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y')
        #crear un array para introducir los dias 
        days_array.append(day_format)
    return days_array



@login_required(login_url="/login/")
def index(request):

    if request.method == 'POST':

        categories = request.POST.getlist('categories[]')
        poblations = request.POST.getlist('poblations[]')
        aforo = request.POST.get('aforo')
        date_inicio = request.POST.get('date_inicio')
        date_fin = request.POST.get('date_fin')

        value_precio_gratuito = request.POST.get('Gratuito')
        value_precio_20 = request.POST.get('Hasta 20 euros')
        value_precio_50 = request.POST.get('Hasta 50 euros')
        value_precio_100 = request.POST.get('Hasta 100 euros')

        value_audiencia_todos = request.POST.get('Todos los publicos')
        value_audiencia_16 = request.POST.get('Mayores de 16 años')
        value_audiencia_18 = request.POST.get('Mayores de 18 años')
        #hacer las variables globales en toda la app.
        request.session['selected_categories'] = categories
        request.session['poblations'] = poblations
        request.session['aforo'] = aforo
        request.session['date_inicio'] = date_inicio
        request.session['date_fin'] = date_fin
        request.session['selected_value_precio_gratuito'] = value_precio_gratuito
        request.session['selected_value_precio_20'] = value_precio_20
        request.session['selected_value_precio_50'] = value_precio_50
        request.session['selected_value_precio_100'] = value_precio_100
        request.session['selected_value_audiencia_todos'] = value_audiencia_todos
        request.session['selected_value_audiencia_16'] = value_audiencia_16
        request.session['selected_value_audiencia_18'] = value_audiencia_18
        
        #rango entre dias 
        array_days = range_dates(date_inicio, date_fin );
        request.session['array_days'] = array_days

        #rango de aforo
        if aforo != '':
            array_aforo = aforo.split(",")
            array_aforo = list(map(int, array_aforo))
        else:
            array_aforo = None

        
        #lista de audiencia
        array_audiencia = []
        if value_audiencia_todos != None:
            array_audiencia.append(value_audiencia_todos)
        if value_audiencia_16 != None:
            array_audiencia.append(value_audiencia_16)
        if value_audiencia_18 != None:
            array_audiencia.append(value_audiencia_18)

        request.session['array_audiencia'] = array_audiencia

        #lista de precios
        array_precio = []
        if value_precio_gratuito != None:
            array_precio.append(value_precio_gratuito)
        if value_precio_20 != None:
            array_precio.append(value_precio_20)
        if value_precio_50 != None:
            array_precio.append(value_precio_50)
        if value_precio_100 != None:
            array_precio.append(value_precio_100)

        request.session['array_precio'] = array_precio
        

        translated_categories = General.translate_categories(categories); 
        request.session['translated_categories'] = translated_categories
   
        #------------------- QUERIES ----------------------------------#
        total_data = Query.query_general(poblations,array_days, translated_categories, array_audiencia, array_precio, array_aforo);
        my_query_count_events = Query.query_number_events(poblations,array_days, translated_categories, array_audiencia, array_precio, array_aforo);
        my_query_count_places = Query.query_number_places(poblations,array_days, translated_categories, array_audiencia, array_precio, array_aforo);
        my_query_aforo = Query.query_total_aforo(poblations,array_days, translated_categories, array_audiencia, array_precio, array_aforo);
        my_query_days_aforo = Query.query_sum_aforo_days(poblations,array_days, translated_categories, array_audiencia, array_precio, array_aforo);
        aforo_total = Query.query_sum_aforos_poblations(poblations,array_days, translated_categories, array_audiencia, array_precio, array_aforo);
        my_query_categories_events = Query.query_categories_events(poblations,array_days, translated_categories, array_audiencia, array_precio, array_aforo);
        my_query_categories_places = Query.query_categories_places_aforo(poblations,array_days, translated_categories, array_audiencia, array_precio, array_aforo);
    
        #---------------------------------------------------------------#

        #print(total_data)
        #funcion para traducir las direcciones en coordenadas.
        latitud_longitud , centro_coordinates = General.adress_to_coordinates(total_data);
 
        
        #funcion para estructurar el JSON de las categorias con los numeros de eventos.
        array_categories = []
        array_categories_legend = []
        array_categorie_color = []
        count = 0
        for element in my_query_categories_events:
            
            cat_total = element['total']
            cat_categoria = element['Categoría']
            cat_categoria_translated = General.translate_categorie_inverse(str(cat_categoria))
            categoria_json = {'value': cat_total,  'name': cat_categoria_translated}
            array_categories.append(categoria_json)
            array_categories_legend.append(cat_categoria_translated)
            color = General.link_categorie_color(cat_categoria)
            array_categorie_color.append(color)

        #funcion para estructurar el JSON de los lugares con el aforo y su color correspondiente.
        array_place_aforo = []
        array_colores = []
        count = 0
        for element in my_query_categories_places:
            place_lugar = element['lugar']
            place_categoria = element['Categoría']
            place_aforo = element['Aforo']
            place_json = {'value': place_aforo, 'name': place_lugar }
            array_place_aforo.append(place_json)
           
            
            color = General.link_categorie_color(place_categoria)
            
            array_colores.append(color)


        count_events = my_query_count_events[0]
        count_places = my_query_count_places[0]
        total_aforo = my_query_aforo[0]
        

        array_data_fgraph = [{'name':c, 'type':'line', 'step':'start', 'data': aforo_total[i::len(poblations)]}  for i,c in enumerate(poblations)]

        # {
        #     name: 'Fuenlabrada',
        #     type: 'line',
        #     step: 'start',
        #     data: [1200, 1320, 1010, 1340, 900, 2300, 2100],
        #     lineStyle: {color: '#d5ceeb'}
        # }
        #print(array_data_fgraph)
        count_events = int(count_events['total'])
        count_places = int(count_places['total'])
        total_aforo = int(total_aforo['total'])
        
        media_aforo = ( total_aforo / int(len(array_days)) )
       

        request.session['count_events'] = count_events
        request.session['count_places'] = count_places
        request.session['media_aforo'] = media_aforo
        request.session['total_aforo'] = total_aforo
        request.session['array_days'] = array_days
        request.session['my_query_days_aforo'] = my_query_days_aforo
        request.session['array_data_fgraph'] = array_data_fgraph
        request.session['latitud_longitud'] = latitud_longitud
        request.session['centro_coordinates'] = centro_coordinates
        request.session['array_categories'] = array_categories
        request.session['array_place_aforo'] = array_place_aforo
        request.session['array_categorie_color'] = array_categorie_color
        request.session['array_categories_legend'] = array_categories_legend
        request.session['array_colores'] = array_colores
        request.session['total_data'] = total_data
 
        audiencia = ['Todos los publicos','Mayores de 18 años','Mayores de 16 años']
        
        context = {
            'count_days': len(array_days),
            'count_events': count_events,
            'count_places': count_places,
            'total_aforo': total_aforo,
            'media_aforo': str(round(media_aforo)),
            'day_first': date_inicio,
            'day_last': date_fin,
            'days': array_days,
            'poblations': poblations,
            'audiencia': audiencia,
            'aforo': aforo,
            'array_data_fgraph': array_data_fgraph,
            'my_query_days_aforo' : my_query_days_aforo,
            'latitud_longitud': latitud_longitud,
            'centro_coordinates': json.dumps(centro_coordinates),
            'array_categories': json.dumps(array_categories),
            'array_place_aforo': json.dumps(array_place_aforo),
            'array_categorie_color': array_categorie_color,
            'array_categories_legend':array_categories_legend,
            'array_colores': array_colores,
            'total_data': json.dumps(total_data),
        }
    
        return render(request, "index.html", context)

    poblations = request.session.get('poblations')
    date_inicio = request.session.get('date_inicio')
    date_fin = request.session.get('date_fin')
    array_days = request.session.get('array_days')
    translated_categories = request.session.get('translated_categories')
    aforo = request.session.get('aforo')
    array_audiencia = request.session.get('array_audiencia')
    precio = request.session.get('precio')


    #valores por defecto para el dashboard
    if not poblations and (date_inicio is None or date_fin is None):
        poblations = ['Madrid','San Fernando De Henares', 'Arganda Del Rey']
        date_inicio = '2018-09-07'
        date_fin = '2018-09-09'
        
        array_days = range_dates(date_inicio, date_fin);
    
        #------------------- QUERIES ----------------------------------#
        total_data = Query.query_general(poblations,array_days, translated_categories, array_audiencia, precio, aforo);
        my_query_count_events = Query.query_number_events(poblations,array_days, translated_categories, array_audiencia, precio, aforo);
        my_query_count_places = Query.query_number_places(poblations,array_days, translated_categories, array_audiencia, precio, aforo);
        my_query_aforo = Query.query_total_aforo(poblations,array_days, translated_categories, array_audiencia, precio, aforo);
        my_query_days_aforo = Query.query_sum_aforo_days(poblations,array_days, translated_categories, array_audiencia, precio, aforo);
        aforo_total = Query.query_sum_aforos_poblations(poblations,array_days, translated_categories, array_audiencia, precio, aforo);
        my_query_categories_events = Query.query_categories_events(poblations,array_days, translated_categories, array_audiencia, precio, aforo);
        my_query_categories_places = Query.query_categories_places_aforo(poblations,array_days, translated_categories, array_audiencia, precio, aforo);
        #---------------------------------------------------------------#

        count_events = my_query_count_events[0]
        count_places = my_query_count_places[0]
        total_aforo = my_query_aforo[0]


        count_events = int(count_events['total'])
        count_places = int(count_places['total'])
        total_aforo = int(total_aforo['total'])


    
        media_aforo = ( total_aforo / int(len(array_days)) )

        array_data_fgraph = [{'name':c, 'type':'line', 'step':'start', 'data': aforo_total[i::len(poblations)]}  for i,c in enumerate(poblations)]

        #funcion para traducir las direcciones en coordenadas.
        latitud_longitud , centro_coordinates = General.adress_to_coordinates(total_data);

        request.session['count_events'] = count_events
        request.session['count_places'] = count_places
        request.session['media_aforo'] = media_aforo
        request.session['total_aforo'] = total_aforo
        request.session['poblations'] = poblations
        request.session['array_days'] = array_days
        request.session['date_inicio'] = date_inicio
        request.session['date_fin'] = date_fin
        request.session['my_query_days_aforo'] = my_query_days_aforo
        request.session['array_data_fgraph'] = array_data_fgraph
        request.session['total_data'] = total_data

    array_days = request.session.get('array_days')
    date_inicio = request.session.get('date_inicio')
    date_fin = request.session.get('date_fin')
    count_events = request.session.get('count_events')
    count_places = request.session.get('count_places')
    total_aforo = request.session.get('total_aforo')
    media_aforo = request.session.get('media_aforo')
    poblations = request.session.get('poblations')
    aforo = request.session.get('aforo')
    my_query_days_aforo = request.session.get('my_query_days_aforo')
    array_data_fgraph = request.session.get('array_data_fgraph')
    latitud_longitud = request.session.get('latitud_longitud')
    centro_coordinates = request.session.get('centro_coordinates')
    array_categories = request.session.get('array_categories')
    array_place_aforo = request.session.get('array_place_aforo')
    array_categorie_color = request.session.get('array_categorie_color')
    array_categories_legend = request.session.get('array_categories_legend')
    array_colores = request.session.get('array_colores')
    total_data = request.session.get('total_data')

    audiencia = ['Todos los publicos','Mayores de 18 años','Mayores de 16 años']
    
    context = {
             'count_days': len(array_days),
            'count_events': count_events,
            'count_places': count_places,
            'total_aforo': total_aforo,
            'media_aforo': str(round(media_aforo)),
            'day_first': date_inicio,
            'day_last': date_fin,
            'days': array_days,
            'poblations': poblations,
            'aforo': aforo,
            'audiencia': audiencia,
            'total_aforo': total_aforo,
            'array_data_fgraph': array_data_fgraph,
            'my_query_days_aforo' : my_query_days_aforo,
            'latitud_longitud': latitud_longitud,
            'centro_coordinates': json.dumps(centro_coordinates),
            'array_categories': json.dumps(array_categories),
            'array_place_aforo': json.dumps(array_place_aforo),
            'array_categorie_color': array_categorie_color,
            'array_categories_legend':array_categories_legend,
            'array_colores': array_colores,
            'total_data': json.dumps(total_data),
        }

    
    
    return render(request, "index.html", context)

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.

    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def data_table(request):


    array_days = request.session.get('array_days')
    date_inicio = request.session.get('date_inicio')
    date_fin = request.session.get('date_fin')
    count_events = request.session.get('count_events')
    count_places = request.session.get('count_places')
    total_aforo = request.session.get('total_aforo')
    media_aforo = request.session.get('media_aforo')
    poblations = request.session.get('poblations')
    my_query_days_aforo = request.session.get('my_query_days_aforo')
    total_data = request.session.get('total_data')



    context = {
        'count_days': len(array_days),
        'days': array_days,
        'day_first': date_inicio,
        'day_last': date_fin,
        'count_events': count_events,
        'count_places': count_places,
        'aforo_total': total_aforo,
        'media_aforo': str(round(media_aforo)),
        'poblations': poblations,
        'my_query_days_aforo' : my_query_days_aforo,
        'total_data': total_data,
        }
    
    return render(request, "data-table.html", context)


@login_required(login_url="/login/")
def more_filters(request):

    categorias = ['Infantiles','Musicales','Naturaleza','Espectáculos','Teatro','Audiovisual','Congreso y conferencias','Exposiciones','Mercados','Visita guiada','Otros','Deportes','Curso o taller']
    poblaciones = ['Alcalá de Henares','Alcobendas','Arganda Del Rey','Buitrago De Lozoya','Cabrera, La','Casarrubuelos','Chapineria','Chinchon','Colmenarejo','Combos, Los (arroyomolinos)','Cortijo De San Isidro, El','Daganzo de Arriba','Dehesa De Santillana','Fresnedilla De La Oliva','Fuenlabrada','Galapagar','Guadalix de la Sierra','Hoyo De Manzanares','Madrid','Majadahonda','Méntrida','Mostoles','Navacerrada, Pueblo','Navalagamella','Nuevo Baztan','Pardo, El','Poligono Industrial Alcobendas','Rascafría','Residencia Nuestra Señora Del Pilar (boadilla)','Rivas-Vaciamadrid','Robregordo','San Fernando De Henares','San Martin De La Vega','San Martin De Valdeiglesias','San Sebastián de los Reyes','Serna Del Monte, La','Serranilla, La (guadarrama)','Torrejon De Ardoz','Valdemaqueda','Villa Del Prado','Villalba De Guadarrama','Villarejo De Salvanes','Villavieja De Lozoya']
    precio = ['Gratuito','Hasta 20 euros','Hasta 50 euros','Hasta 100 euros']
    audiencia = ['Todos los publicos','Mayores de 18 años','Mayores de 16 años']

    tipos_aforo = ['Seleccionar aforo','Menos de 150 personas','De 150 a 300 personas','De 300 a 800 personas','De 800 a 1400 personas','De 1400 a 4800 personas','Mayor de 4800 personas']


    count_events = request.session.get('count_events')
    count_places = request.session.get('count_places')
    total_aforo = request.session.get('total_aforo')
    media_aforo = request.session.get('media_aforo')
    date_inicio = request.session.get('date_inicio')
    date_fin = request.session.get('date_fin')
    aforo = request.session.get('aforo')
    array_precio = request.session.get('array_precio')
    array_audiencia = request.session.get('array_audiencia')
    categories = request.session.get('selected_categories')
    poblations = request.session.get('poblations')
 
    aforo_translated = General.translate_aforo(aforo) 
    print(array_audiencia)
    print(array_precio)
    #Eliminar las categorias ya seleccionadas.
    if categories is not None:
        for element in categories:
            if element in categorias:
                categorias.remove(element)

    #Eliminar las poblaciones ya seleccionadas.
    if poblations is not None:
        for element in poblations:
            if element in poblaciones:
                poblaciones.remove(element)

    #Eliminar los aforos ya seleccionadas.
    if aforo_translated is not None:
        for element in tipos_aforo:
            if aforo_translated in tipos_aforo:
                tipos_aforo.remove(aforo_translated)



    translate_aforo = General.translate_aforo(aforo)

    context = {
           
            'count_events': count_events,
            'count_places': count_places,
            'total_aforo': total_aforo,
            'media_aforo': str(round(media_aforo)),
            'day_first': date_inicio,
            'day_last': date_fin,
            'categories': categories,
            'categorias':categorias,
            'aforo': aforo_translated,
            'tipos_aforo': tipos_aforo,
            'translate_aforo': translate_aforo,
            'precio': precio,
            'array_precio': array_precio,
            'audiencia':audiencia,
            'array_audiencia': array_audiencia,
            'poblations': poblations,
            'poblaciones': poblaciones,
        }
        
    return render(request, "more-filters.html", context)



