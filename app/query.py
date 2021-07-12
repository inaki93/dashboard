import json
import itertools
import mysql.connector
from geopy.geocoders import GoogleV3, Nominatim
from app.filters import *

# select * from optimizadata
# where Precio = 'Gratuito'
# AND ( Aforo BETWEEN 1400 and 4800 )
# OR  (REGEXP_SUBSTR(`Precio`,"[0-9]+") BETWEEN 1 and 20)



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
    #cur.close()
    return (r[0] if r else None) if one else r


class Query:
#query general
    def query_general(poblations,days, categories, audiencia, precio, aforo):

        #solo con los elementos de poblacion y dias.
        sql = "SELECT * FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({}) "

        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_days = ', '.join(['%s']*len(days))
        
        formato = ()
        formato += (cond_poblations, )
        formato += (cond_days, )
        
        tuple_parametres = ()
        tuple_parametres += (poblations, )
        tuple_parametres += (days, )
        params = None

        if categories:
            sql, formato, tuple_parametres = Filter.categories( categories, sql ,formato, tuple_parametres);
        if audiencia:
            sql, formato, tuple_parametres = Filter.audiencia( audiencia, sql ,formato , tuple_parametres);
        if precio:
            sql, formato, tuple_parametres, params = Filter.precio( precio, sql ,formato , tuple_parametres, params);
        if aforo:
            sql, formato,tuple_parametres, params = Filter.aforo(aforo, sql ,formato , tuple_parametres, params );
        
        
        if params:
            total_data = query_db( sql.format( * formato), tuple(itertools.chain( * tuple_parametres )) + params )
        else:
            total_data = query_db( sql.format( * formato), tuple(itertools.chain( * tuple_parametres )) )

        return total_data

#query para el numero de eventos (circulo)
    def query_number_events(poblations ,days, categories, audiencia, precio, aforo):

        #solo con los elementos de poblacion y dias.
        sql = "SELECT COUNT(*) as total FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({}) "

        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_days = ', '.join(['%s']*len(days))

        formato = ()
        formato += (cond_poblations, )
        formato += (cond_days, )
        
        tuple_parametres = ()
        tuple_parametres += (poblations, )
        tuple_parametres += (days, )
        params = None

        if categories:
            sql, formato, tuple_parametres = Filter.categories(categories, sql ,formato, tuple_parametres);
        if audiencia:
            sql, formato, tuple_parametres = Filter.audiencia( audiencia, sql ,formato , tuple_parametres);
        if precio:
            sql, formato, tuple_parametres, params = Filter.precio( precio, sql ,formato , tuple_parametres, params);
        if aforo:
            sql, formato, tuple_parametres, params = Filter.aforo( aforo, sql ,formato , tuple_parametres, params);
        
        if params:
            total_data = query_db( sql.format( * formato), tuple(itertools.chain( * tuple_parametres )) + params )
        else:
            total_data = query_db( sql.format( * formato), tuple(itertools.chain( * tuple_parametres )) )

        return total_data

#query para el numero de lugares (circulo)
    def query_number_places(poblations ,days, categories, audiencia, precio, aforo):

        #solo con los elementos de poblacion y dias.
        sql = "SELECT COUNT(*) as total FROM ( SELECT DISTINCT (lugar) FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({}) "

        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_days = ', '.join(['%s']*len(days))

        formato = ()
        formato += (cond_poblations, )
        formato += (cond_days, )
        
        tuple_parametres = ()
        tuple_parametres += (poblations, )
        tuple_parametres += (days, )
        params = None

        if categories:
            sql, formato, tuple_parametres = Filter.categories( categories, sql ,formato, tuple_parametres);
        if audiencia:
            sql, formato, tuple_parametres = Filter.audiencia( audiencia, sql ,formato , tuple_parametres);
        if precio:
            sql, formato, tuple_parametres, params = Filter.precio( precio, sql ,formato , tuple_parametres, params);
        if aforo:
            sql, formato, tuple_parametres, params = Filter.aforo( aforo, sql ,formato , tuple_parametres, params);
        
        sql = sql + ' GROUP BY Lugar ) as x'
        if params:
            total_data = query_db( sql.format( * formato), tuple(itertools.chain( * tuple_parametres )) + params )
        else:
            total_data = query_db( sql.format( * formato), tuple(itertools.chain( * tuple_parametres )) )

        return total_data

#query para sacar el total del aforo para los dias seleccionados.
    def query_total_aforo(poblations ,days, categories, audiencia, precio, aforo):

        #solo con los elementos de poblacion y dias.
        sql = "SELECT IFNULL( SUM(Aforo), 0 ) as total FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({})"

        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_days = ', '.join(['%s']*len(days))

        formato = ()
        formato += (cond_poblations, )
        formato += (cond_days, )
        
        tuple_parametres = ()
        tuple_parametres += (poblations, )
        tuple_parametres += (days, )
        params = None

        if categories:
            sql, formato, tuple_parametres = Filter.categories( categories, sql ,formato, tuple_parametres);
        if audiencia:
            sql, formato, tuple_parametres = Filter.audiencia( audiencia, sql ,formato , tuple_parametres);
        if precio:
            sql, formato, tuple_parametres, params = Filter.precio( precio, sql ,formato , tuple_parametres, params);
        if aforo:
            sql, formato, tuple_parametres, params = Filter.aforo( aforo, sql ,formato , tuple_parametres, params);
        
        if params:
            total_data = query_db( sql.format( * formato), tuple(itertools.chain( * tuple_parametres )) + params )
        else:
            total_data = query_db( sql.format( * formato), tuple(itertools.chain( * tuple_parametres )) )

        return total_data

 #query para sacar la suma de los aforos para cada dia. (grafica de barras)
    def query_sum_aforo_days(poblations ,days, categories, audiencia, precio, aforo):

        #solo con los elementos de poblacion y dias.
        sql = "SELECT IFNULL( SUM(Aforo), 0 ) as total FROM optimizadata WHERE Población IN ({}) "

        cond_poblations = ', '.join(['%s']*len(poblations))

        formato = ()
        formato += (cond_poblations, )

        tuple_parametres = ()
        tuple_parametres += (poblations, )
        params = None

        if categories:
            sql, formato, tuple_parametres = Filter.categories( categories, sql ,formato, tuple_parametres);
        if audiencia:
            sql, formato, tuple_parametres = Filter.audiencia( audiencia, sql ,formato , tuple_parametres);
        if precio:
            sql, formato, tuple_parametres, params = Filter.precio( precio, sql ,formato , tuple_parametres, params);
        if aforo:
            sql, formato, tuple_parametres, params = Filter.aforo( aforo, sql ,formato , tuple_parametres, params);
        
        days_sum_aforo_array = []
        if params:
            sql = sql + ' AND Fecha = %s '
            for day in days:
                if params == None:
                    params = ()
                params += (day, )
                
                total_data = query_db( sql.format( * formato), tuple(itertools.chain( * tuple_parametres )) + params )
                params = params[:-1]
                days_aforo = total_data[0]
                days_sum_aforo_array.append(int(days_aforo['total']))
            return days_sum_aforo_array
        else:
            sql = sql + ' AND Fecha = %s '
            for day in days:
                if params == None:
                    params = ()
                parametros = ()
                parametros += (day, )
                params += parametros
                total_data = query_db( sql.format( * formato), tuple(itertools.chain( * tuple_parametres )) + params )
                params = params[:-1]
                days_aforo = total_data[0]
                days_sum_aforo_array.append(int(days_aforo['total']))
            return days_sum_aforo_array

#query para sacar el aforo de las poblaciones para cada uno de los dias (primera grafica de la primera fila)
    def query_sum_aforos_poblations(poblations ,days, categories, audiencia, precio, aforo):

        sql = "SELECT IFNULL (SUM(Aforo), 0 ) as Total_aforo FROM optimizadata WHERE Categoría = Categoría "
 
        formato = ()
        tuple_parametres = ()
        params = None

        if categories:
            sql, formato, tuple_parametres = Filter.categories( categories, sql ,formato, tuple_parametres);
        if audiencia:
            sql, formato, tuple_parametres = Filter.audiencia( audiencia, sql ,formato , tuple_parametres);
        if precio:
            sql, formato, tuple_parametres, params = Filter.precio( precio, sql ,formato , tuple_parametres,params);
        if aforo:
            sql, formato, tuple_parametres, params = Filter.aforo( aforo, sql ,formato , tuple_parametres,params);
        
        days_sum_total_array = []
        if params:
            sql = sql + ' AND Población = %s AND Fecha = %s'
            for idx , day in enumerate(days): 
                for idx , poblation in enumerate(poblations):
                    params += (poblation, )
                    params += (day, )
                    if formato is None and tuple_parametres is None:
                        my_query = query_db( sql , params )
                        params = params[:-1]
                        params = params[:-1]
                        json_element = my_query[0]
                        days_sum_total_array.append(int(json_element['Total_aforo']))
                    else:
                        my_query = query_db( sql.format( * formato), tuple(itertools.chain( * tuple_parametres )) + params )
                        params = params[:-1]
                        params = params[:-1]
                        json_element = my_query[0]
                        days_sum_total_array.append(int(json_element['Total_aforo']))
                    
        else:
            sql = sql + ' AND Población = %s AND Fecha = %s'
            for idx , day in enumerate(days): 
                for idx , poblation in enumerate(poblations):
                    params = ()
                    params += (poblation, )
                    params += (day, )
                    if formato is None and tuple_parametres is None:
                        my_query = query_db( sql , params )
                        json_element = my_query[0]
                        days_sum_total_array.append(int(json_element['Total_aforo']))
                    else:
                        my_query = query_db( sql.format( * formato), tuple(itertools.chain( * tuple_parametres )) + params )
                        json_element = my_query[0]
                        days_sum_total_array.append(int(json_element['Total_aforo']))
            
        return days_sum_total_array

#query para sacar las categorias con sus respectivos eventos.(primera grafica segunda fila)
    def query_categories_events(poblations ,days, categories, audiencia, precio, aforo):

        #solo con los elementos de poblacion y dias.
        sql = "SELECT COUNT(*) as total , Categoría FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({}) "

        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_days = ', '.join(['%s']*len(days))

        formato = ()
        formato += (cond_poblations, )
        formato += (cond_days, )
        
        tuple_parametres = ()
        tuple_parametres += (poblations, )
        tuple_parametres += (days, )
        params = None

        if categories:
            sql, formato, tuple_parametres = Filter.categories(categories, sql ,formato, tuple_parametres);
        if audiencia:
            sql, formato, tuple_parametres = Filter.audiencia(audiencia, sql ,formato , tuple_parametres);
        if precio:
            sql, formato, tuple_parametres,params = Filter.precio(precio, sql ,formato , tuple_parametres,params);
        if aforo:
            sql, formato, tuple_parametres, params = Filter.aforo(aforo, sql ,formato , tuple_parametres,params);
        
        sql = sql + ' GROUP BY Categoría ORDER BY Categoría'
        if params:
            total_data = query_db( sql.format( * formato), tuple(itertools.chain( * tuple_parametres )) + params )
        else:
            total_data = query_db( sql.format( * formato), tuple(itertools.chain( * tuple_parametres )) )

        return total_data

#query para sacar los lugares, su categoria y el aforo.(primera grafica segunda fila)
    def query_categories_places_aforo(poblations ,days, categories, audiencia, precio, aforo):

        #solo con los elementos de poblacion y dias.
        sql = "SELECT DISTINCT (lugar) , Categoría, Aforo FROM optimizadata WHERE Población IN ({}) AND Fecha IN ({}) "

        cond_poblations = ', '.join(['%s']*len(poblations))
        cond_days = ', '.join(['%s']*len(days))

        formato = ()
        formato += (cond_poblations, )
        formato += (cond_days, )
        
        tuple_parametres = ()
        tuple_parametres += (poblations, )
        tuple_parametres += (days, )
        params = None

        if categories:
            sql, formato, tuple_parametres = Filter.categories(categories, sql ,formato, tuple_parametres);
        if audiencia:
            sql, formato, tuple_parametres = Filter.audiencia(audiencia, sql ,formato , tuple_parametres);
        if precio:
            sql, formato, tuple_parametres,params = Filter.precio(precio, sql ,formato , tuple_parametres,params);
        if aforo:
            sql, formato, tuple_parametres, params = Filter.aforo(aforo, sql ,formato , tuple_parametres,params);
        
        sql = sql + 'GROUP BY Lugar ORDER BY Categoría'
        if params:
            total_data = query_db( sql.format( * formato), tuple(itertools.chain( * tuple_parametres )) + params )
        else:
            total_data = query_db( sql.format( * formato), tuple(itertools.chain( * tuple_parametres )) )

        return total_data

