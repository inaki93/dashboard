
function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

function link_categorie_color(categorie) {

    if (categorie == 'CHILDREN_ACTIVITIES'){
            return  '#5E61FF' 
    }
    else if (categorie == 'MUSIC'){
            return  '#F56969'
    }
    else if (categorie == 'NATURE'){
            return  '#85E06E'
    }
    else if (categorie == 'SHOW'){
            return  '#DE62E3'  
    }  
    else if (categorie == 'THEATRE'){
            return  '#F4FA2A' 
    }  
    else if (categorie == 'AUDIOVISUAL'){
            return  '#9AF3CF'
    }       
    else if (categorie == 'CONGRESS_CONFERENCE'){
            return  '#AD70FA'
    }   
    else if (categorie == 'EXHIBITIONS'){
            return  '#F4CC95'
    }
    else if (categorie == 'FAIR_MARKET'){
            return  '#48C9F9'  
    }   
    else if (categorie == 'GUIDED_VISIT'){
            return '#964B00' 
    }    
    else if (categorie == 'OTHERS'){
            return '#88897E'
    }
    else if (categorie == 'SPORT'){
            return  '#5732A3'
    }
    else if (categorie == 'WORKSHOP_COURSE'){
            return  '#200DF5'
    }
}


var dom = document.getElementById("container_graph");
var myChart = echarts.init(dom);
var app = {};

var option;

option = {
    title: {
        text: 'Aforo total',
        textStyle: { color: "#FFFFFF" }
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: poblations,
        textStyle: { color: "#FFFFFF" }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        data: days,
        axisLabel: {
            textStyle: {
                color: '#FFFFFF'
            }
        }
    },
    yAxis: {
        type: 'value',
        nameTextStyle: {
            color: "rgba(255, 255, 255)"
          },
        axisLabel: {
            textStyle: {
                color: '#FFFFFF'
            }
        }
    },
    series: array_data_fgraph
   
};

if (option && typeof option === 'object') {
    myChart.setOption(option);
}


// ----------------------------------------------------------

var dom2 = document.getElementById("container_graph2");
var myChart2 = echarts.init(dom2);
var app2 = {};

var option2;

// var data = data.map(function (item) {
//             //formatear el campo precio para que sea
                    
//                 return [item[1], item[4], item[6], item[11] ];
                     
//         });

var data = total_data.map(function (data, index, array) {
 
    return [data.Fecha, data.Lugar, data.Aforo, data.Precio]; 
 
});
    

        var i;
        var datos_array = [];
        datos_filter = [];
        datos_result = [];
    
        for (i = 0; i < data.length; i++) {
          datos = data[[i]]
          
          if(days.includes(datos[0])){
                datos[0] = days.indexOf(datos[0]); 
                datos[2] = parseInt(datos[2]);
                if (datos[3] == 'gratuito' || datos[3] == 'Gratuito'){
                    //La primera posición en el eje X
                    datos[3] = 0;
                    //datos_filter.push(datos);
                }else if (datos[3] == 'A consultar' || datos[3] == 'A Consultar'){
                    //La ultima posición en el eje X
                    //indicar en el campo A consultar
                    datos[3] = 'A consultar';
                    //datos_filter.push(datos);
                }else{ 

                    if(datos[3] == null){
                    //si los datos son nulos no parseamos el numero.
                    datos[3] = datos[3];
                    }else{
                    //tomar solo el primer valor numerico del campo precio 
                    number_price = datos[3].replace( /(^.+)(\w\d+\w)(.+$)/i,'$2');
                    datos[3] = parseInt(number_price); 
                    //console.log(datos[3]);
                    }
                }
        
               datos_filter = [datos[0],datos[3],datos[2],datos[1]];
               datos_array.push(datos_filter);
              
              } 
    }


var itemStyle = {
    opacity: 0.8,
    shadowBlur: 10,
    shadowOffsetX: 0,
    shadowOffsetY: 0,
    shadowColor: 'rgba(0,0,0,0.3)'
};

data = datos_array.map(function (item) {
    return [item[1], item[0], item[2],item[3]];
});
    

myChart2.setOption(option2 = {

    tooltip: {
        position: 'top',
        //position: ['35%', '32%'],
        formatter: function (params) {
            return params.value[2] + ' aforo en ' + params.value[3];
        }
    },
    grid: {
        left: 30,
        bottom: 1,
        right: 80,
        containLabel: true
    },
    xAxis: {
        type: 'category',
        data: price,
        boundaryGap: false,
        splitLine: {
            show: true
        },
        axisLine: {
            interval: 2 //intervalo del eje
        },
        axisLabel: {
            textStyle: {
                color: '#FFFFFF'
            }
        }
    },
    yAxis: {
        
        data: days,
        //position: 'right', cambiar la posicion del eje Y a la derecha
        offset: 30,
        axisLine: {
            left: 20,
            show: false
        },
        axisLabel: {
            textStyle: {
                color: '#FFFFFF'
            }
        }
    },
    visualMap: [  //Eventos mas de 10 mil personas
        {   
            name:'Aforo', //titulo de la leyenda 
            top: 5,
            //right: 30,
            type: "piecewise",
            dimension: 2,
            right: 4,
            min: 0,
            max: 24000,
            itemWidth: 20,
            //range: [2000, 8000],
            //dimension: [[0,100,200]],
            //calculable: false,
            textStyle: {
                color: '#FFFFFF'
            },
            inRange: {
                color: ["#313695", "#4575b4", "#74add1", "#abd9e9", "#e0f3f8", "#ffffbf", "#fee090", "#fdae61", "#f46d43", "#d73027", "#a50026"]
            }
        }
    ],
    series: [{
        name: 'Aforo',
        type: 'scatter',
        itemStyle: itemStyle,
        symbolSize: function (val) {
            if (val[2]<10000){
                 return val[2] * 0.0065;
                
            }else{
                 return val[2] * 0.00032;
            }
        },
        data: data,
        animationDelay: function (idx) {
            return idx * 5;
        },
    }]
});


if (option2 && typeof option2 === 'object') {
    myChart2.setOption(option2);
}

//--------------------------------------------------------------

var dom3 = document.getElementById("container_graph3");
var myChart3 = echarts.init(dom3);
var app3 = {};

var option3;


function renderItem(params, api) {
    var values = [api.value(0), api.value(1)];
    var coord = api.coord(values);
    var size = api.size([1, 1], values);
    return {
        type: 'sector',
        shape: {
            cx: params.coordSys.cx,
            cy: params.coordSys.cy,
            r0: coord[2] - size[0] / 2,
            r: coord[2] + size[0] / 2,
            startAngle: -(coord[3] + size[1] / 2),
            endAngle: -(coord[3] - size[1] / 2)
        },
        style: api.style({
            fill: api.visual('color')
        })
    };
}

var data3 = total_data.map(function (data, index, array) {
 
    return [data.Fecha, data.Horario]; 
         
});


        var i;
        var datos_array = [];
        datos_filter = [];
        datos_result = [];
    
        for (i = 0; i < data3.length; i++) {
          datos = data3[[i]]
          //console.log(datos[1]);
          if(days.includes(datos[0])){
                datos[0] = days.indexOf(datos[0]); 
                number_hour = datos[1].replace(/\D/g, "");
                //number_price = datos[1].match(/\\d+\\.?\\d*/g);
                
                if (number_hour.length == 4 ){
                    //horario de 00:00.
                    //ejemplo 19:00 > sera solo un punto a las 19:00 [0,19,1]
                    hora = number_hour.slice(0,2);
                    datos[1] = parseInt(hora);
                    datos_filter = [datos[0],datos[1],1];
                    datos_array.push(datos_filter);    
                }else if(number_hour.length == 8){
                    //horario de 00:00 - 00:00.
                    //ejemplo 16:30 - 18:00 > sera varios puntos [0,16,1] , [0,17,1],[0,18,1]
                    //ejemplo  00:00 - 6:00 > sera varios puntos [0,0,1] , [0,1,1],[0,2,1] , [0,3,1] , [0,4,1] , [0,5,1] , [0,6,1] 
                    //console.log(number_hour);
                    hora_primera = number_hour.slice(0,2);
                    hora_primera = parseInt(hora_primera);
                    hora_segunda = number_hour.slice(4,6);
                    hora_segunda = parseInt(hora_segunda);
                    //controlar las horas negativas
                    if(hora_segunda > hora_primera){
                       hora = hora_segunda - hora_primera;
                       for(h = hora_primera; h <  hora_primera + hora; h++){
                                //controlar para que cuando pase de 23 , vaya a 00 y 01 
                                datos_filter = [datos[0],h,1];
                                //console.log(datos_filter);
                                datos_array.push(datos_filter);
                            
                                }
                               
                       }else{
                           var hi;
                           if(hora_primera < 24 && hora_segunda < 12 ){
                                hora = ( 24 - hora_primera ) + hora_segunda; 
                                
                                
                                for(h = hora_primera; h < hora_primera + hora; h++){
                                    hour = 0;
                                    if (h == 24){
                                         hour = 00; 
                                      }else if(h == 25){
                                        hour = 01;
                                      }else if(h == 26){
                                        hour = 02;
                                      }else if(h == 27){
                                        hour = 03;
                                      }else if(h == 28){
                                        hour = 04;
                                      }else if(h == 29){
                                        hour = 05;
                                      }else if(h == 30){
                                        hour = 06;
                                      }else if(h == 31){
                                        hour = 07;
                                      }
                                    
                                    if(hour < 0){
                                    datos_filter = [datos[0],h,1];
                                    
                                    datos_array.push(datos_filter);
                                    }else{
                                    datos_filter = [datos[0],hour,1];
                                    
                                    datos_array.push(datos_filter);         
                                    }
                            
                                }
                               
                           }else{
                                hora = hora_primera - hora_segunda; 
                               
                               
                                for(h = hora_segunda; h < hora_primera + hora ; h++){
                                datos_filter = [datos[0],h,1];
                                //console.log(datos_filter);
                                datos_array.push(datos_filter);
                            
                                }
                           }
                       }     
                    
                    //console.log(hora);

                    
                }else if(number_hour.length == 16){
                    //horario de 00:00 - 00:00 y 00:00 - 00:00.
                    //ejemplo L a V: 9:00 - 13:30 16:00 - 21:00 > sera varios puntos
                    //[0,9,1] , [0,10,1] , [0,11,1] , [0,12,1] , [0,13,1] , 
                    //[0,16,1] , ,[0,17,1] , [0,18,1] , [0,19,1] , [0,20,1] , [0,21,1]
                    //2000-1800-2030-1900
                    hora_primera = number_hour.slice(0,2);
                    hora_primera = parseInt(hora_primera);
                    hora_segunda = number_hour.slice(4,6);
                    hora_segunda = parseInt(hora_segunda);
                    hora_tercera = number_hour.slice(8,10);
                    hora_tercera = parseInt(hora_tercera);
                    hora_cuarta = number_hour.slice(10,12);
                    hora_cuarta = parseInt(hora_cuarta);
                    
                    hora_ma = hora_segunda - hora_primera;
                    hora_ta = hora_cuarta - hora_tercera;
                    
                    if (hora_ma > 0){
                        var h;
                        for(h = hora_primera; h < hora_segunda; h++){
                            
                            datos_filter = [datos[0],h,1];
                            datos_array.push(datos_filter);
                            
                        }
                    }
                    
                     if (hora_ta > 0){
                        var h;
                        for(h = hora_tercera; h < hora_cuarta; h++){
                            
                            datos_filter = [datos[0],h,1];
                            datos_array.push(datos_filter);
                            
                        }
                    }

                         
                }
              } 
    }

 
arr  = datos_array;    
 
//pasos para la suma de las mismas horas  
    
const checkedArr = [];
const output = [];

for (let i = 0; i < arr.length; i++) {
  let count = 0;
  if (!isArrayChecked(arr[i])) {
    checkedArr.push(arr[i]);
    for (let j = i; j < arr.length; j++) {
      if (isArraySame(arr[i], arr[j])) {
        count++;
      }
    }
    output.push([arr[i][0], arr[i][1], count]);
  }
}

function isArrayChecked(array) {
  let exist = false;
  for (let k = 0; k < checkedArr.length; k++) {
    if (isArraySame(array, checkedArr[k])) {
      exist = true;
      break;
    }
  }
  return exist;
}

function isArraySame(arr1, arr2) {
  if (arr1[0] !== arr2[0] || arr1[1] !== arr2[1] || arr1[2] !== arr2[2])
    return false;
  return true;
}



//console.log(output);


// ejemplo estructura de los datos                               
//var data = [[0,0,5],[0,1,1],[0,2,0],[0,3,0],[0,4,0],[0,5,0],[0,6,0],[0,7,0],[0,8,0],[0,9,0],[0,10,0],[0,11,2],[0,12,4],[0,13,1],[0,14,1],[0,15,3],[0,16,4],[0,17,6],[0,18,4],[0,19,4],[0,20,3],[0,21,3],[0,22,2],[0,23,5],[1,0,7],[1,1,0],[1,2,0],[1,3,0],[1,4,0],[1,5,0],[1,6,0],[1,7,0],[1,8,0],[1,9,0],[1,10,5],[1,11,2],[1,12,2],[1,13,6],[1,14,9],[1,15,11],[1,16,6],[1,17,7],[1,18,8],[1,19,12],[1,20,5],[1,21,5],[1,22,7],[1,23,2],[2,0,1],[2,1,1],[2,2,0],[2,3,0],[2,4,0],[2,5,0],[2,6,0],[2,7,0],[2,8,0],[2,9,0],[2,10,3],[2,11,2],[2,12,1],[2,13,9],[2,14,8],[2,15,10],[2,16,6],[2,17,5],[2,18,5],[2,19,5],[2,20,7],[2,21,4],[2,22,2],[2,23,4],[3,0,7],[3,1,3],[3,2,0],[3,3,0],[3,4,0],[3,5,0],[3,6,0],[3,7,0],[3,8,1],[3,9,0],[3,10,5],[3,11,4],[3,12,7],[3,13,14],[3,14,13],[3,15,12],[3,16,9],[3,17,5],[3,18,5],[3,19,10],[3,20,6],[3,21,4],[3,22,4],[3,23,1]];
    
    
var maxValue = output.reduce(function (max, item) {
    return Math.max(max, item[2]);
}, -Infinity);

myChart3.setOption(option3 = {
    polar: {},
    tooltip: {
    },
    visualMap: {
        type: 'continuous',
        min: 0,
        max: 20,
        top: 'middle',
        dimension: 2,
        calculable: true,
        textStyle: {
            color: '#FFFFFF'
        }
    },
    angleAxis: {
        type: 'category',
        data: hours,
        boundaryGap: false,
        splitLine: {
            show: true,
            lineStyle: {
                color: '#ddd',
                type: 'dashed'
            }
        },
        axisLine: {
            show: false
        },
        axisLabel: {
            textStyle: {
                color: '#FFFFFF'
            }
        }
    },
    radiusAxis: {
        type: 'category',
        data: days,
        z: 100,
        axisLabel: {
            textStyle: {
                color: '#000000'
            }
        }
    },
    series: [{
        name: 'Eventos',
        type: 'custom',
        coordinateSystem: 'polar',
        itemStyle: {
            color: '#FFFFFF'
        },
        renderItem: renderItem,
        data: output
    }]
});
    


if (option3 && typeof option3 === 'object') {
    myChart3.setOption(option3);
}

//----------------------------------------------------

var dom4 = document.getElementById("container_graph4");
var myChart4 = echarts.init(dom4);
var app4 = {};

var option4;

           
        datos_audiencia1 = {
                            'name': audiencia[0],
                            'itemStyle': {
                                'color': 'rgba(128,155,72,255)',
                                'borderColor': 'rgba(128,155,72,255)'
                            }
                          };

        datos_audiencia2 = {
                            'name': audiencia[1],
                            'itemStyle': {
                              'color': 'rgba(255,120,134,255)',
                              'borderColor': 'rgba(255,120,134,255)'
                          }
                        };


        datos_audiencia3 =  {
                            'name': audiencia[2],
                            'itemStyle': {
                                'color': 'rgba(64,105,157,255)',
                                'borderColor': 'rgba(64,105,157,255)'
                            }
                        };


var data_lugares = total_data.map(function (data, index, array) {
 
    return [data.Fecha, data.Lugar, data.Aforo, data.Audiencia, data.Categoría]; 
                         
});
                                                 
       
        var datos_array_lugares = [];

    
        var datos_array_lugares2 = [];
        var datos_array_links = [];
        for (i = 0; i < data_lugares.length; i++) {
          datos = data_lugares[[i]]
          //console.log(datos[0]);
          datos_filter = [];
          datos_result = [];
          lugar_data = {};
          if(days.includes(datos[0]) && audiencia.includes(datos[3]) ){ 
              //tenemos que eliminar los duplicados 
              datos[2] = parseFloat(datos[2]);
              console.log(datos[4]);
              color_categoria = link_categorie_color (datos[4]);
              console.log(color_categoria);
              color = getRandomColor()
                                 
              lugar_data = {
                    'name': datos[1],
                    'itemStyle': {
                        'color': color_categoria,
                        'borderColor': color_categoria
                    }
                };
                         
              var link = {
                    'source': datos[3],
                    'target': datos[0],
                    'value': datos[2]
                };
              
              var link2 = {
                    'source': datos[0],
                    'target': datos[1],
                    'value': datos[2]
                };
              //datos_filter = [datos[0],datos[3],datos[2],datos[1]]
              
              //nos quedamos con los lugares que tengas mas de una fecha y descartamos el resto.
              if ((!datos_array_lugares.find(o => o.name === datos[1]))) {
              //lugares con solo un evento en los dias seleccionados.
              datos_array_lugares.push(lugar_data);
              }else{
              //lugares con mas un evento.
              datos_array_lugares2.push(lugar_data);  
              }
              //enlaces entre tipo de audiencia - dias , dias - lugares.
              datos_array_links.push(link);
              datos_array_links.push(link2);
              

              } }
        //funcion para eliminar los duplicados 
        function hash(o){
            return o.name;
        }    

        var hashesFound = {};

        datos_array_lugares2.forEach(function(o){
            hashesFound[hash(o)] = o;
        })

        var results = Object.keys(hashesFound).map(function(k){
            return hashesFound[k];
        })

        //loop para introducir los dias en los datos estructurados (capa intermedia).
        var i;
        for (i = 0; i < days.length; i++){
                     color = getRandomColor()

                     datos_dia =  {
                                    'name': days[i],
                                    'itemStyle': {
                                        'color': color ,
                                        'borderColor': color
                                    }
                                };

                    results.push(datos_dia);
         }

        //Esto sera fijo para tener solo tres tipos de audiencia.
        results.push(datos_audiencia1);
        results.push(datos_audiencia2);
        results.push(datos_audiencia3);



myChart4.setOption(option4 = {
    backgroundColor: '#212940',
    series: [
        {
            type: 'sankey',
            left: 50.0,
            top: 30.0,
            right: 150.0,
            bottom: 25.0,
            data: results,
            links: datos_array_links,
            lineStyle: {
                color: 'source',
                curveness: 0.5
            },
            itemStyle: {
                color: '#1f77b4',
                borderColor: '#1f77b4'
            },
            label: {
                color: 'rgba(0,0,0,0.7)',
                fontFamily: 'Arial',
                fontSize: 10,
                textStyle: { color: "#FFFFFF" }
            }
        }],
    tooltip: {
        trigger: 'item',
    }
});

   
if (option4 && typeof option4 === 'object') {
    myChart4.setOption(option4);
}

//----------------------------------------------------
//   GRAFICA CATEGORIAS Y LUGARES
//----------------------------------------------------

var dom5 = document.getElementById("container_graph5");
var myChart5 = echarts.init(dom5 );
var app5 = {};

var option5;



option5 = {
    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)'
    },
    legend: {
        data: array_categories_legend ,
        textStyle: { color: "#FFFFFF" },
        orient: 'vertical', 
        left : 3,

    },
    series: [
        {
            name: 'Categorias',
            type: 'pie',
            selectedMode: 'single',
            radius: [0, '40%'],
            color: array_categorie_color,
            data: array_categories
        },
        {   name: 'Lugares',
            type: 'pie',
            radius: ['60%', '80%'],
            itemStyle : {
                color: '#FFFFFF',
                normal : {
                     label : {
                        show: false,
                    }
                }},
            color: array_colores,
            data: array_place_aforo
                
           
        }
    ]
};

if (option5 && typeof option5 === 'object') {
    myChart5.setOption(option5);
}


