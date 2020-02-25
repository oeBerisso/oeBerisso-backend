const mymap = L.map('mapid').setView([-34.889561,-57.9083765], 13);

async function getLocationsAsync() {
    let response = await fetch("/puntos");
    let data = await response.json();

    for(let i = 0; i < data.locations.length; i++){
        let point = data.locations[i];
        L.marker([point.latitude, point.longitude]).bindPopup("<b>" + point.name + "</b>.").addTo(mymap);
    }
}

getLocationsAsync()

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);

L.Control.geocoder().addTo(mymap)

control = L.Routing.control({
    routeWhileDragging: true,
    geocoder: L.Control.Geocoder.nominatim(),
    language: 'es',
}).addTo(mymap);


function createButton(label, container) {
    var btn = L.DomUtil.create('button', '', container);
    btn.setAttribute('type', 'button');
    btn.innerHTML = label;
    return btn;
}

mymap.on('click', function(e) {
    var container = L.DomUtil.create('div'),
        startBtn = createButton('Punto inicial', container),
        destBtn = createButton('Punto final', container);
    
    L.popup().setContent(container).setLatLng(e.latlng).openOn(mymap);
    
    L.DomEvent.on(startBtn, 'click', function() {
        control.spliceWaypoints(0, 1, e.latlng);
        mymap.closePopup();
    });
    L.DomEvent.on(destBtn, 'click', function() {
        control.spliceWaypoints(control.getWaypoints().length - 1, 1, e.latlng);
        mymap.closePopup();
    });
});