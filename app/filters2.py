import json
import itertools
import mysql.connector
from geopy.geocoders import GoogleV3, Nominatim


mydb = mysql.connector.connect(
    host="bpyzbzunzrblg9epu4fq-mysql.services.clever-cloud.com",
    user="umkpqgglbv86bt2b",
    password="Z4ywID6qw12VvND6F54T",
    database="bpyzbzunzrblg9epu4fq"
    )

class General:
    #funcion para traducir una categoria
    def translate_categorie(categorie):
        categorie_translate = ''
        if categorie == 'Infantiles' :
            categorie_translate = 'CHILDREN_ACTIVITIES'
        elif categorie == 'Musicales' :
            categorie_translate = 'MUSIC'
        elif categorie == 'Naturaleza' :
            categorie_translate = 'NATURE'
        elif categorie == 'Espectáculos' :
            categorie_translate = 'SHOW'
        elif categorie == 'Teatro' :
            categorie_translate = 'THEATRE'
        elif categorie == 'Audiovisual' :
            categorie_translate = 'AUDIOVISUAL'
        elif categorie == 'Congreso y conferencias' :
            categorie_translate = 'CONGRESS_CONFERENCE'
        elif categorie == 'Exposiciones' :
            categorie_translate = 'EXHIBITIONS'
        elif categorie == 'Mercados' :
            categorie_translate = 'FAIR_MARKET'
        elif categorie == 'Visita guiada' :
            categorie_translate = 'GUIDED_VISIT'
        elif categorie == 'Otros' :
            categorie_translate = 'OTHERS'
        elif categorie == 'Deportes' :
            categorie_translate = 'SPORTS'
        elif categorie == 'Curso o taller' :
            categorie_translate = 'WORKSHOP_COURSE'

            return categorie_translate

  #funcion para traducir una categoria inversa
    def translate_categorie_inverse(categorie_translate):

        if categorie_translate == 'CHILDREN_ACTIVITIES' :
            return  'Infantiles' 
        elif categorie_translate == 'MUSIC' :
            return  'Musicales'
        elif categorie_translate == 'NATURE' :
            return  'Naturaleza'
        elif categorie_translate == 'SHOW' :
            return  'Espectáculos'    
        elif categorie_translate == 'THEATRE' :
            return  'Teatro'   
        elif categorie_translate == 'AUDIOVISUAL' :
            return  'Audiovisual'       
        elif categorie_translate == 'CONGRESS_CONFERENCE' :
            return  'Congreso y conferencias'   
        elif categorie_translate == 'EXHIBITIONS':
            return  'Exposiciones'
        elif categorie_translate == 'FAIR_MARKET' :
            return  'Mercados'     
        elif categorie_translate == 'GUIDED_VISIT' :
            return  'Visita guiada'     
        elif categorie_translate == 'OTHERS' :
            return 'Otros'
        elif categorie_translate == 'SPORTS':
            return  'Deportes' 
        elif categorie_translate == 'WORKSHOP_COURSE' :
            return  'Curso o taller'


    #funcion para traducir los diferentes tipos de categorias.
    def translate_categories(args=[]):
        categories_translate_array = []
        for categorie in args:
            if categorie == 'Infantiles' :
                categorie_translate = 'CHILDREN_ACTIVITIES'
                categories_translate_array.append(categorie_translate)
            elif categorie == 'Musicales' :
                categorie_translate = 'MUSIC'
                categories_translate_array.append(categorie_translate)
            elif categorie == 'Naturaleza' :
                categorie_translate = 'NATURE'
                categories_translate_array.append(categorie_translate)
            elif categorie == 'Espectáculos' :
                categorie_translate = 'SHOW'
                categories_translate_array.append(categorie_translate)
            elif categorie == 'Teatro' :
                categorie_translate = 'THEATRE'
                categories_translate_array.append(categorie_translate)
            elif categorie == 'Audiovisual' :
                categorie_translate = 'AUDIOVISUAL'
                categories_translate_array.append(categorie_translate)
            elif categorie == 'Congreso y conferencias' :
                categorie_translate = 'CONGRESS_CONFERENCE'
                categories_translate_array.append(categorie_translate)
            elif categorie == 'Exposiciones' :
                categorie_translate = 'EXHIBITIONS'
                categories_translate_array.append(categorie_translate)
            elif categorie == 'Mercados' :
                categorie_translate = 'FAIR_MARKET'
                categories_translate_array.append(categorie_translate)
            elif categorie == 'Visita guiada' :
                categorie_translate = 'GUIDED_VISIT'
                categories_translate_array.append(categorie_translate)
            elif categorie == 'Otros' :
                categorie_translate = 'OTHERS'
                categories_translate_array.append(categorie_translate)
            elif categorie == 'Deportes' :
                categorie_translate = 'SPORTS'
                categories_translate_array.append(categorie_translate)
            elif categorie == 'Curso o taller' :
                categorie_translate = 'WORKSHOP_COURSE'
                categories_translate_array.append(categorie_translate)

        return categories_translate_array

    def translate_aforo(aforo):

            if aforo == '150' :
                aforo_translate = 'Menos de 150 personas'
               
            elif aforo == '150,300' :
                aforo_translate = 'De 150 a 300 personas'
               
            elif aforo == '300,800' :
                aforo_translate = 'De 300 a 800 personas'
              
            elif aforo == '800,1400' :
                aforo_translate = 'De 800 a 1400 personas'
                
            elif aforo == '1400,4800' :
                aforo_translate = 'De 1400 a 4800 personas'
                
            elif aforo == '4800' :
                aforo_translate = 'Mayor de 4800 personas'
           
            return aforo_translate

#funcion para asignar cada categoria a un color.
    def link_categorie_color(categorie):
        if categorie == 'CHILDREN_ACTIVITIES' :
            return  '#5E61FF' 
        elif categorie == 'MUSIC' :
            return  '#F56969'
        elif categorie == 'NATURE' :
            return  '#85E06E'
        elif categorie == 'SHOW' :
            return  '#DE62E3'    
        elif categorie == 'THEATRE' :
            return  '#F4FA2A'   
        elif categorie == 'AUDIOVISUAL' :
            return  '#9AF3CF'       
        elif categorie == 'CONGRESS_CONFERENCE' :
            return  '#AD70FA'   
        elif categorie == 'EXHIBITIONS':
            return  '#F4CC95'
        elif categorie == 'FAIR_MARKET' :
            return  '#48C9F9'     
        elif categorie == 'GUIDED_VISIT' :
            return '#964B00'     
        elif categorie == 'OTHERS' :
            return '#88897E'
        elif categorie == 'SPORTS':
            return  '#030202' 
        elif categorie == 'WORKSHOP_COURSE' :
            return  '#200DF5'

#funcion para traducir las direcciones a coordenadas.
    def adress_to_coordinates(total_data):
        latitud_longitud = []
        lat = 0
        lng = 0

        for element in total_data:
            event_Dirección = element['Dirección']
            event_Población = element['Población']

            #geolocator = Nominatim(user_agent="optimizadata")
            geolocator = GoogleV3(api_key='AIzaSyA1EWrHdaa1UaJw3U8VuXKKucoqqp58ipo')
            direccion = event_Dirección + ' ' + event_Población
            location = geolocator.geocode(direccion, timeout=None)
            direccion = ''
            if location is not None:
                #averiguar el centro de las coordinadas
                lat = lat + location.latitude
                lng = lng + location.longitude
        
                event_coordinates = { 'lat': location.latitude, 'lng': location.longitude }
                latitud_longitud.append(event_coordinates)

        if len(latitud_longitud) != 0:
            centro_coordinates = { 'lat': (lat/(len(latitud_longitud))) , 'lng': (lng/(len(latitud_longitud))) }
        else:
             centro_coordinates = { 'lat': 40.41831 , 'lng':  -3.70275 }

        return latitud_longitud, centro_coordinates


 
#funcion para abrir un cursor y realizar una query
def query_db(query, args=(), one=False):
    cur = mydb.cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    #cur.close()
    return (r[0] if r else None) if one else r

#clase para query con todos los filtros.
class Filter_poblations_days_categories_aforo:
    
    #query general 
    def query_general(categories,poblations,days, aforo):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))

        params = ()
        params += (aforo[0], )
        params += (aforo[1], )

        sql = "SELECT * FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({})  AND Categoría IN ({}) AND Aforo BETWEEN %s AND %s".format(cond_poblations, cond_days ,cond_categories)
        total_data = query_db(sql, tuple(itertools.chain(poblations, days,categories )) + params)
        return total_data

    #query para el circulo de numero de eventos
    def query_number_event(categories,poblations,days, aforo):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))

        params = ()
        params += (aforo[0], )
        params += (aforo[1], )

        sql_events = "SELECT COUNT(*) as total FROM optimizadata WHERE Fecha IN ({}) AND Categoría IN ({}) AND Población IN ({}) AND Aforo BETWEEN %s AND %s".format(cond_days,cond_categories, cond_poblations )
        my_query_count_places = query_db(sql_events, tuple(itertools.chain(days,categories, poblations ))  + params)
        return my_query_count_places

    #query para el circulo de numero de lugares
    def query_number_places(categories,poblations,days, aforo):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))

        params = ()
        params += (aforo[0], )
        params += (aforo[1], )
  
        sql_places = "SELECT COUNT(*) as total FROM ( SELECT DISTINCT (lugar) FROM optimizadata WHERE Fecha IN ({})  AND Categoría IN ({}) AND Población IN ({}) AND Aforo BETWEEN %s AND %s GROUP BY Lugar ) as x".format(cond_days,cond_categories, cond_poblations ) 
        my_query_count_places = query_db(sql_places, tuple(itertools.chain(days,categories, poblations ))  + params)
        return my_query_count_places

    #query para sacar el total del aforo.
    def query_total_aforo(categories,poblations,days, aforo):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))  

        params = ()
        params += (aforo[0], )
        params += (aforo[1], )  

        sql_aforo = "SELECT IFNULL( SUM(Aforo), 0 ) as total FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({}) AND Categoría IN ({}) AND Aforo BETWEEN %s AND %s".format(cond_poblations, cond_days, cond_categories)
        my_query_aforo = query_db(sql_aforo, tuple(itertools.chain(poblations, days, categories)) + params )
        return my_query_aforo

    #query para sacar las categorias con sus respectivos eventos.
    def query_categories_events(categories,poblations,days, aforo):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))  

        params = ()
        params += (aforo[0], )
        params += (aforo[1], )  

        sql_categories = "SELECT COUNT(*) as total , Categoría FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({}) AND Categoría IN ({}) AND Aforo BETWEEN %s AND %s GROUP BY Categoría ORDER BY Categoría ASC".format(cond_poblations, cond_days, cond_categories)
        my_query_categories = query_db(sql_categories, tuple(itertools.chain(poblations, days, categories)) + params )
        return my_query_categories

    #query para sacar los lugares, su categoria y el aforo.
    def query_categories_places_aforo(categories,poblations,days, aforo):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))  

        params = ()
        params += (aforo[0], )
        params += (aforo[1], )  

        sql_categories_places = "SELECT DISTINCT (lugar) , Categoría, Aforo FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({}) AND Categoría IN ({}) AND Aforo BETWEEN %s AND %s GROUP BY Lugar ORDER BY Categoría ASC".format(cond_poblations, cond_days, cond_categories)
        my_query_categories_places = query_db(sql_categories_places, tuple(itertools.chain(poblations, days, categories)) + params )
        return my_query_categories_places

   #query para sacar la suma de los aforos para cada dia.
    def query_sum_aforo_days(categories,poblations,days, aforo):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        days_sum_aforo_array = []

        for day in days:
            params = ()
            params += (day, )
            params += (aforo[0], )
            params += (aforo[1], )
            sql_aforo = "SELECT IFNULL( SUM(Aforo), 0 ) as total FROM optimizadata WHERE Población IN ({})  AND Categoría IN ({}) AND Fecha = %s AND Aforo BETWEEN %s AND %s".format( cond_poblations, cond_categories)
            my_query_aforo = query_db(sql_aforo, tuple(itertools.chain(poblations,categories)) + params)
            days_aforo = my_query_aforo[0]
            days_sum_aforo_array.append(int(days_aforo['total']))
        #devolver un array con la suma del aforo para cada uno de los dias.
        return days_sum_aforo_array

    #Una unica select que se ejecutara en loop con los distintos dias seleccionados, la población no varia.
    def query_sum_graph_aforos(categories,poblations_array, days_array, aforo):
        days_sum_total_array = []
        cond_categories = ', '.join(['%s']*len(categories))


        for idx , day in enumerate(days_array): 
            for idx , poblation in enumerate(poblations_array):
                params = ()
                params += (poblation, )
                params += (day, )
                params += (aforo[0], )
                params += (aforo[1], )
                sql = "SELECT IFNULL (SUM(Aforo), 0 ) as Total_aforo FROM optimizadata WHERE Población = %s AND Fecha = %s  AND Aforo BETWEEN %s AND %s AND Categoría IN ({})".format(cond_categories)
                my_query = query_db(sql, params + tuple(itertools.chain(categories)))
                    
                json_element = my_query[0]
                days_sum_total_array.append(int(json_element['Total_aforo']))
            #json_days_sum_total_array = json.dumps(days_sum_total_array)
    
        return days_sum_total_array


#clase para query con poblaciones , dias, categorias, aforo y audiencia.
class Filter:
    
    #query general 
    def query_general(categories,poblations,days, aforo, audiencia):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))

        params = ()
        params += (aforo[0], )
        params += (aforo[1], )

        sql = "SELECT * FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({})  AND Categoría IN ({}) AND Aforo BETWEEN %s AND %s".format(cond_poblations, cond_days ,cond_categories)
        total_data = query_db(sql, tuple(itertools.chain(poblations, days,categories )) + params)
        return total_data

    #query para el circulo de numero de eventos
    def query_number_event(categories,poblations,days, aforo, audiencia):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))

        params = ()
        params += (aforo[0], )
        params += (aforo[1], )

        sql_events = "SELECT COUNT(*) as total FROM optimizadata WHERE Fecha IN ({}) AND Categoría IN ({}) AND Población IN ({}) AND Aforo BETWEEN %s AND %s".format(cond_days,cond_categories, cond_poblations )
        my_query_count_places = query_db(sql_events, tuple(itertools.chain(days,categories, poblations ))  + params)
        return my_query_count_places

    #query para el circulo de numero de lugares
    def query_number_places(categories,poblations,days, aforo, audiencia):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))

        params = ()
        params += (aforo[0], )
        params += (aforo[1], )
  
        sql_places = "SELECT COUNT(*) as total FROM ( SELECT DISTINCT (lugar) FROM optimizadata WHERE Fecha IN ({})  AND Categoría IN ({}) AND Población IN ({}) AND Aforo BETWEEN %s AND %s GROUP BY Lugar ) as x".format(cond_days,cond_categories, cond_poblations ) 
        my_query_count_places = query_db(sql_places, tuple(itertools.chain(days,categories, poblations ))  + params)
        return my_query_count_places

    #query para sacar el total del aforo.
    def query_total_aforo(categories,poblations,days, aforo, audiencia):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))  

        params = ()
        params += (aforo[0], )
        params += (aforo[1], )  

        sql_aforo = "SELECT IFNULL( SUM(Aforo), 0 ) as total FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({}) AND Categoría IN ({}) AND Aforo BETWEEN %s AND %s".format(cond_poblations, cond_days, cond_categories)
        my_query_aforo = query_db(sql_aforo, tuple(itertools.chain(poblations, days, categories)) + params )
        return my_query_aforo

    #query para sacar las categorias con sus respectivos eventos.
    def query_categories_events(categories,poblations,days, aforo, audiencia):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))  

        params = ()
        params += (aforo[0], )
        params += (aforo[1], )  

        sql_categories = "SELECT COUNT(*) as total , Categoría FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({}) AND Categoría IN ({}) AND Aforo BETWEEN %s AND %s GROUP BY Categoría ORDER BY Categoría ASC".format(cond_poblations, cond_days, cond_categories)
        my_query_categories = query_db(sql_categories, tuple(itertools.chain(poblations, days, categories)) + params )
        return my_query_categories

    #query para sacar los lugares, su categoria y el aforo.
    def query_categories_places_aforo(categories,poblations,days, aforo, audiencia):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))  

        params = ()
        params += (aforo[0], )
        params += (aforo[1], )  

        sql_categories_places = "SELECT DISTINCT (lugar) , Categoría, Aforo FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({}) AND Categoría IN ({}) AND Aforo BETWEEN %s AND %s GROUP BY Lugar ORDER BY Categoría ASC".format(cond_poblations, cond_days, cond_categories)
        my_query_categories_places = query_db(sql_categories_places, tuple(itertools.chain(poblations, days, categories)) + params )
        return my_query_categories_places

   #query para sacar la suma de los aforos para cada dia.
    def query_sum_aforo_days(categories,poblations,days, aforo, audiencia):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        days_sum_aforo_array = []

        for day in days:
            params = ()
            params += (day, )
            params += (aforo[0], )
            params += (aforo[1], )
            sql_aforo = "SELECT IFNULL( SUM(Aforo), 0 ) as total FROM optimizadata WHERE Población IN ({})  AND Categoría IN ({}) AND Fecha = %s AND Aforo BETWEEN %s AND %s".format( cond_poblations, cond_categories)
            my_query_aforo = query_db(sql_aforo, tuple(itertools.chain(poblations,categories)) + params)
            days_aforo = my_query_aforo[0]
            days_sum_aforo_array.append(int(days_aforo['total']))
        #devolver un array con la suma del aforo para cada uno de los dias.
        return days_sum_aforo_array

    #Una unica select que se ejecutara en loop con los distintos dias seleccionados, la población no varia.
    def query_sum_graph_aforos(categories,poblations_array, days_array, aforo, audiencia):
        days_sum_total_array = []
        cond_categories = ', '.join(['%s']*len(categories))


        for idx , day in enumerate(days_array): 
            for idx , poblation in enumerate(poblations_array):
                params = ()
                params += (poblation, )
                params += (day, )
                params += (aforo[0], )
                params += (aforo[1], )
                sql = "SELECT IFNULL (SUM(Aforo), 0 ) as Total_aforo FROM optimizadata WHERE Población = %s AND Fecha = %s  AND Aforo BETWEEN %s AND %s AND Categoría IN ({})".format(cond_categories)
                my_query = query_db(sql, params + tuple(itertools.chain(categories)))
                    
                json_element = my_query[0]
                days_sum_total_array.append(int(json_element['Total_aforo']))
            #json_days_sum_total_array = json.dumps(days_sum_total_array)
    
        return days_sum_total_array




#clase para query con los filtros de poblaciones, dias y categorias.
class Filter_poblations_days_categories:
    
    #query general 
    def query_general(categories,poblations,days):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))

        sql = "SELECT * FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({})  AND Categoría IN ({})".format(cond_poblations, cond_days ,cond_categories)
        total_data = query_db(sql, tuple(itertools.chain(poblations, days,categories )))
        return total_data

    #query para el circulo de numero de eventos
    def query_number_event(categories,poblations,days):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))

        sql_events = "SELECT COUNT(*) as total FROM optimizadata WHERE Fecha IN ({}) AND Categoría IN ({}) AND Población IN ({})".format(cond_days,cond_categories, cond_poblations )
        my_query_count_places = query_db(sql_events, tuple(itertools.chain(days,categories, poblations )))
        return my_query_count_places

    #query para el circulo de numero de lugares
    def query_number_places(categories,poblations,days):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))
        print(categories)
        print(poblations)
        print(days)
        sql_places = "SELECT COUNT(*) as total FROM ( SELECT DISTINCT (lugar) FROM optimizadata WHERE Fecha IN ({})  AND Categoría IN ({}) AND Población IN ({}) GROUP BY Lugar ) as x".format(cond_days,cond_categories, cond_poblations ) 
        my_query_count_places = query_db(sql_places, tuple(itertools.chain(days,categories, poblations )))
        return my_query_count_places

    #query para sacar el total del aforo.
    def query_total_aforo(categories,poblations,days):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))    

        sql_aforo = "SELECT IFNULL( SUM(Aforo), 0 ) as total FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({}) AND Categoría IN ({})".format(cond_poblations, cond_days, cond_categories)
        my_query_aforo = query_db(sql_aforo, tuple(itertools.chain(poblations, days, categories)))
        return my_query_aforo

    #query para sacar las categorias con sus respectivos eventos.
    def query_categories_events(categories,poblations,days):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))  

        sql_categories = "SELECT COUNT(*) as total , Categoría FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({}) AND Categoría IN ({}) GROUP BY Categoría ORDER BY Categoría ASC".format(cond_poblations, cond_days, cond_categories)
        my_query_categories = query_db(sql_categories, tuple(itertools.chain(poblations, days, categories)) )
        return my_query_categories

    #query para sacar los lugares, su categoria y el aforo.
    def query_categories_places_aforo(categories,poblations,days):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        cond_days = ', '.join(['%s']*len(days))  

        sql_categories_places = "SELECT DISTINCT (lugar) , Categoría, Aforo FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({}) AND Categoría IN ({}) GROUP BY Lugar ORDER BY Categoría ASC".format(cond_poblations, cond_days, cond_categories)
        my_query_categories_places = query_db(sql_categories_places, tuple(itertools.chain(poblations, days, categories)))
        return my_query_categories_places

   #query para sacar la suma de los aforos para cada dia.
    def query_sum_aforo_days(categories,poblations,days):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_categories = ', '.join(['%s']*len(categories))
        days_sum_aforo_array = []
        for day in days:
            params = ()
            params += (day, )
            sql_aforo = "SELECT IFNULL( SUM(Aforo), 0 ) as total FROM optimizadata WHERE Población IN ({})  AND Categoría IN ({}) AND Fecha = %s".format( cond_poblations, cond_categories)
            my_query_aforo = query_db(sql_aforo, tuple(itertools.chain(poblations,categories)) + params)
            days_aforo = my_query_aforo[0]
            days_sum_aforo_array.append(int(days_aforo['total']))
        #devolver un array con la suma del aforo para cada uno de los dias.
        return days_sum_aforo_array

    #Una unica select que se ejecutara en loop con los distintos dias seleccionados, la población no varia.
    def query_sum_graph_aforos(categories, days_array, poblations_array):
        days_sum_total_array = []
        cond_categories = ', '.join(['%s']*len(categories))
        for idx , day in enumerate(days_array): 
            for idx , poblation in enumerate(poblations_array):
                params = ()
                params += (poblation, )
                params += (day, )
                sql = "SELECT IFNULL (SUM(Aforo), 0 ) as Total_aforo FROM optimizadata WHERE Población = %s AND Fecha = %s AND Categoría IN ({})".format(cond_categories)
                my_query = query_db(sql, params + tuple(itertools.chain(categories)))
                    
                json_element = my_query[0]
                days_sum_total_array.append(int(json_element['Total_aforo']))
            #json_days_sum_total_array = json.dumps(days_sum_total_array)
    
        return days_sum_total_array



#clase para query con poblaciones y dias.
class Filter_poblations_days:   
    #query general 
    def query_general(poblations,days):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_days = ', '.join(['%s']*len(days))

        sql = "SELECT * FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({})".format(cond_poblations, cond_days)
        total_data = query_db(sql, tuple(itertools.chain(poblations, days )))
        return total_data

    #query para sacar las categorias con sus respectivos eventos.
    def query_categories_events(poblations,days):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_days = ', '.join(['%s']*len(days)) 

        sql_categories = "SELECT COUNT(*) as total , Categoría FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({}) GROUP BY Categoría ORDER BY Categoría ASC".format(cond_poblations, cond_days)
        my_query_categories = query_db(sql_categories, tuple(itertools.chain(poblations, days)) )
        return my_query_categories

    #query para sacar los lugares, su categoria y el aforo.
    def query_categories_places_aforo(poblations,days):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_days = ', '.join(['%s']*len(days))  

        sql_categories_places = "SELECT DISTINCT (lugar) , Categoría, Aforo FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({}) GROUP BY Lugar ORDER BY Categoría ASC".format(cond_poblations, cond_days)
        my_query_categories_places = query_db(sql_categories_places, tuple(itertools.chain(poblations, days)))
        return my_query_categories_places

    #query para el circulo de numero de eventos
    def query_number_event(poblations,days):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_days = ', '.join(['%s']*len(days))

        sql_events = "SELECT COUNT(*) as total FROM optimizadata WHERE Fecha IN ({}) AND Población IN ({})".format(cond_days, cond_poblations )
        my_query_count_places = query_db(sql_events, tuple(itertools.chain(days, poblations)))
        return my_query_count_places

    #query para el circulo de numero de lugares
    def query_number_places(poblations,days):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_days = ', '.join(['%s']*len(days))

        sql_places = "SELECT COUNT(*) as total FROM ( SELECT DISTINCT (lugar) FROM optimizadata WHERE Fecha IN ({})  AND Población IN ({}) GROUP BY Lugar ) as x".format(cond_days, cond_poblations ) 
        my_query_count_places = query_db(sql_places, tuple(itertools.chain(days, poblations )))
        return my_query_count_places

    #query para sacar el total del aforo.
    def query_total_aforo(poblations,days):
        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_days = ', '.join(['%s']*len(days))    

        sql_aforo = "SELECT IFNULL( SUM(Aforo), 0 ) as total FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({})".format(cond_poblations, cond_days)
        my_query_aforo = query_db(sql_aforo, tuple(itertools.chain(poblations, days)))
        return my_query_aforo

    #query para sacar la suma de los aforos para cada dia.
    def query_sum_aforo_days(poblations,days):
        cond_poblations = ', '.join(['%s']*len(poblations))
        days_sum_aforo_array = []
        for day in days:
            params = ()
            params += (day, )
            sql_aforo = "SELECT IFNULL( SUM(Aforo), 0 ) as total FROM optimizadata WHERE Población IN ({}) AND Fecha = %s".format(cond_poblations)
            my_query_aforo = query_db(sql_aforo, tuple(itertools.chain(poblations)) + params)
            days_aforo = my_query_aforo[0]
            days_sum_aforo_array.append(int(days_aforo['total']))
        #devolver un array con la suma del aforo para cada uno de los dias.
        return days_sum_aforo_array

    #Una unica select que se ejecutara en loop con los distintos dias seleccionados, la población no varia.
    def query_sum_graph_aforos(days_array, poblations_array):
        days_sum_total_array = []
        for idx , day in enumerate(days_array): 
            for idx , poblation in enumerate(poblations_array):
                sql = "SELECT IFNULL (SUM(Aforo), 0 ) as Total_aforo FROM optimizadata WHERE Población = %(value_poblation)s AND Fecha =  %(value_date)s"
                params = {'value_poblation':poblation,
                                'value_date':day}

                my_query = query_db(sql, params)
                    
                json_element = my_query[0]
                days_sum_total_array.append(int(json_element['Total_aforo']))
            #json_days_sum_total_array = json.dumps(days_sum_total_array)
    
        return days_sum_total_array

    

