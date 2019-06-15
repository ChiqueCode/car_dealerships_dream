// Create a map object
var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5
});

// Add a tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

// An array containing each city's name, location, and population
var cities = [{
  location: [40.7128, -74.0059],
  name: "New York",
  population: "8,550,405"
},
{location:[61.3025006,-158.7750198],name:"Alaska",population:"23"},
{location:[32.6010112,-86.6807365],name:"Alabama",population:"147"},
{location:[34.7519275,-92.1313784],name:"Arkansas",population:"138"},
{location:[34.1682185,-111.930907],name:"Arizona",population:"1283"},
{location:[37.2718745,-119.2704153],name:"California",population:"11992"},
{location:[38.9979339,-105.550567],name:"Colorado",population:"559"},
{location:[41.5187835,-72.757507],name:"Connecticut",population:"606"},
{location:[38.8993487,-77.0145666],name:"District of Columbia",population:"81"},
{location:[39.145251,-75.4189206],name:"Delaware",population:"63"},
{location:[27.9757279,-83.8330166],name:"Florida",population:"10613"},
{location:[32.6781248,-83.2229757],name:"Georgia",population:"918"},
{location:[20.46,-157.505],name:"Hawaii",population:"27"},
{location:[41.9383166,-93.389798],name:"Iowa",population:"114"},
{location:[45.4945756,-114.1424303],name:"Idaho",population:"83"},
{location:[39.739318,-89.504139],name:"Illinois",population:"2046"},
{location:[39.7662195,-86.441277],name:"Indiana",population:"267"},
{location:[38.4987789,-98.3200779],name:"Kansas",population:"177"},
{location:[37.8222935,-85.7682399],name:"Kentucky",population:"131"},
{location:[30.9733766,-91.4299097],name:"Louisiana",population:"222"},
{location:[42.0629398,-71.718067],name:"Massachusetts",population:"935"},
{location:[38.8063524,-77.2684162],name:"Maryland",population:"631"},
{location:[45.2185133,-69.0148656],name:"Maine",population:"10"},
{location:[44.9435598,-86.4158049],name:"Michigan",population:"265"},
{location:[46.4418595,-93.3655146],name:"Minnesota",population:"223"},
{location:[38.3046615,-92.437099],name:"Missouri",population:"127"},
{location:[32.5851062,-89.8772196],name:"Mississippi",population:"72"},
{location:[46.6797995,-110.044783],name:"Montana",population:"6"},
{location:[35.2145629,-79.8912675],name:"North Carolina",population:"939"},
{location:[47.4678819,-100.3022655],name:"North Dakota",population:"4"},
{location:[41.5008195,-99.680902],name:"Nebraska",population:"117"},
{location:[44.0012306,-71.5799231],name:"New Hampshire",population:"30"},
{location:[40.1430058,-74.7311156],name:"New Jersey",population:"2263"},
{location:[34.1662325,-106.0260685],name:"New Mexico",population:"315"},
{location:[38.502032,-117.0230604],name:"Nevada",population:"779"},
{location:[40.7056258,-73.97968],name:"New York",population:"4773"},
{location:[40.1903624,-82.6692525],name:"Ohio",population:"227"},
{location:[35.3097654,-98.7165585],name:"Oklahoma",population:"174"},
{location:[44.1419049,-120.5380993],name:"Oregon",population:"286"},
{location:[40.9945928,-77.6046984],name:"Pennsylvania",population:"657"},
{location:[41.5827282,-71.5064508],name:"Rhode Island",population:"169"},
{location:[33.62505,-80.9470381],name:"South Carolina",population:"194"},
{location:[44.2126995,-100.2471641],name:"South Dakota",population:"16"},
{location:[35.830521,-85.9785989],name:"Tennessee",population:"265"},
{location:[31.1693363,-100.0768425],name:"Texas",population:"7868"},
{location:[39.4997605,-111.547028],name:"Utah",population:"309"},
{location:[38.0033855,-79.4587861],name:"Virginia",population:"767"},
{location:[43.8717545,-72.4477828],name:"Vermont",population:"3"},
{location:[38.8993487,-77.0145665],name:"Washington",population:"477"},
{location:[44.7862968,-89.8267049],name:"Wisconsin",population:"234"},
{location:[38.9201705,-80.1816905],name:"West Virginia",population:"9"},
{location:[43.000325,-107.5545669],name:"Wyoming",population:"20"}

];

// Loop through the cities array and create one marker for each city, bind a popup containing its name and population add it to the map
for (var i = 0; i < cities.length; i++) {
  var city = cities[i];
  L.marker(city.location)
    .bindPopup("<h1>" + city.name + "</h1> <hr> <h3>Audience Count " + city.population + "</h3>")
    .addTo(myMap);
}
