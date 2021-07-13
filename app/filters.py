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
            categorie_translate = 'SPORT'
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
        elif categorie_translate == 'SPORT':
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
                categorie_translate = 'SPORT'
                categories_translate_array.append(categorie_translate)
            elif categorie == 'Curso o taller' :
                categorie_translate = 'WORKSHOP_COURSE'
                categories_translate_array.append(categorie_translate)

        return categories_translate_array

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
        elif categorie == 'SPORT':
            return  '#5732A3' 
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

            geolocator = Nominatim(user_agent="optimizadata")
            #geolocator = GoogleV3(api_key='GOOGLE_API_KEY')
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


#clase para query con poblaciones , dias, categorias, aforo y audiencia.
class Filter:
    
    #filtrar categorias 
    def categories(categories, sql ,formato, tuple_parametres):
        
        cond_categories = ', '.join(['%s']*len(categories))

        formato += (cond_categories, )
        tuple_parametres += (categories, )

        sql = sql + ' AND Categoría IN ({}) '
        return sql, formato, tuple_parametres

    #filtrar audiencia 
    def audiencia( audiencia, sql ,formato , tuple_parametres):
        
        cond_audiencia = ', '.join(['%s']*len(audiencia))

        #formato = formato + cond_audiencia
        #tuple_parametres = tuple_parametres , audiencia
        
        formato += (cond_audiencia, )
        tuple_parametres += (audiencia, )

        sql = sql + 'AND Audiencia IN ({}) '
        return sql, formato, tuple_parametres


    #filtrar precio 
    def precio( precio, sql ,formato , tuple_parametres, params):
        
        count = 0
        sql = sql + ' AND ('
        for x in precio:
            if x == 'Gratuito':
                if params == None:
                    params = ()
                params += (x, )
                count = count + 1
                sql = sql + ' Precio = %s '

            elif x == 'Hasta 20 euros':
                precio_inferior = 1
                precio_superior = 20
                
                if params == None:
                    params = ()
                params += (precio_inferior, )
                params += (precio_superior, )
                
             
                if count == 0:
                    sql = sql + '  REGEXP_SUBSTR(Precio,"[0-9]+") BETWEEN %s and %s '
                else:
                    sql = sql + ' OR  REGEXP_SUBSTR(Precio,"[0-9]+") BETWEEN %s and %s '

            elif x == 'Hasta 50 euros': 
                precio_inferior = 21
                precio_superior = 50
                
                if params == None:
                    params = ()
                params += (precio_inferior, )
                params += (precio_superior, )
                count = count + 1
                
                if count == 0:
                    sql = sql + '  REGEXP_SUBSTR(Precio,"[0-9]+") BETWEEN %s and %s '
                else:
                    sql = sql + ' OR  REGEXP_SUBSTR(Precio,"[0-9]+") BETWEEN %s and %s '

            elif x == 'Hasta 100 euros':
                precio_inferior = 51
                precio_superior = 100
                
                if params == None:
                    params = ()
                params += (precio_inferior, )
                params += (precio_superior, )
                count = count + 1
                
                if count == 0:
                    sql = sql + '  REGEXP_SUBSTR(Precio,"[0-9]+") BETWEEN %s and %s '
                else:
                    sql = sql + ' OR REGEXP_SUBSTR(Precio,"[0-9]+") BETWEEN %s and %s '
        
        sql = sql + ' )'

        return sql, formato, tuple_parametres, params


    #filtrar aforo 
    def aforo( aforo , sql ,formato , tuple_parametres, params):
       
        if params == None:
            params = ()
        params += (aforo[0], )
        params += (aforo[1], )

        sql = sql + ' AND ( Aforo BETWEEN %s AND %s ) '
        return sql, formato,tuple_parametres, params
