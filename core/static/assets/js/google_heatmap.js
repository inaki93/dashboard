// This example requires the Visualization library. Include the libraries=visualization
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyB41DRUbKWJHPxaFjMAwdrzWzbVKartNGg&libraries=visualization">

let map, heatmap;

const gradient = [
  "rgba(0, 255, 255, 0)",
  "rgba(0, 255, 255, 1)",
  "rgba(0, 191, 255, 1)",
  "rgba(0, 127, 255, 1)",
  "rgba(0, 63, 255, 1)",
  "rgba(0, 0, 255, 1)",
  "rgba(0, 0, 223, 1)",
  "rgba(0, 0, 191, 1)",
  "rgba(0, 0, 159, 1)",
  "rgba(0, 0, 127, 1)",
  "rgba(63, 0, 91, 1)",
  "rgba(127, 0, 63, 1)",
  "rgba(191, 0, 31, 1)",
  "rgba(255, 0, 0, 1)",
];



function initMap() {

  var heatmapData = [];
  //loop para introducir cada uno de las coordenadas del JSON a la variable heatmap
  for (let i = 0; i < latitud_longitud.length; i++) {

  var item = latitud_longitud[i];
  var item_lat = item.lat;
  var item_lng = item.lng;


  var key = new google.maps.LatLng({ lat: item_lat, lng: item_lng});


  heatmapData.push(key);
  
  }

    console.log(heatmapData)


  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 11,
    center: centro_coordinates,
    mapTypeId: "roadmap"

  });

heatmap = new google.maps.visualization.HeatmapLayer({
    data: heatmapData,
    radius: 20,
    gradient: gradient
  });

  heatmap.setMap(map);
  heatmap.set('gradient', gradient);
  
}

function toggleHeatmap() {
  heatmap.setMap(heatmap.getMap() ? null : map);
}

function changeGradient() {
 
  heatmap.set("gradient", heatmap.get("gradient") ? null : gradient);
}

function changeRadius() {
  heatmap.set("radius", heatmap.get("radius") ? null : 20);
}

function changeOpacity() {
  heatmap.set("opacity", heatmap.get("opacity") ? null : 0.2);
}

