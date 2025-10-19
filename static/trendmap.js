(function() {
  // Create the map
  var map = L.map('map', { worldCopyJump: true }).setView([20, 0], 2);

  // Add a base tile layer
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  // Coarse GeoJSON features approximating continental regions (rectangles)
  var continentsGeo = {
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "properties": { "name": "North America" },
        "geometry": {
          "type": "Polygon",
          "coordinates": [[
            [-170, 15], [-50, 15], [-50, 72], [-170, 72], [-170, 15]
          ]]
        }
      },
      {
        "type": "Feature",
        "properties": { "name": "South America" },
        "geometry": {
          "type": "Polygon",
          "coordinates": [[
            [-82, -56], [-34, -56], [-34, 13], [-82, 13], [-82, -56]
          ]]
        }
      },
      {
        "type": "Feature",
        "properties": { "name": "Europe" },
        "geometry": {
          "type": "Polygon",
          "coordinates": [[
            [-25, 34], [45, 34], [45, 72], [-25, 72], [-25, 34]
          ]]
        }
      },
      {
        "type": "Feature",
        "properties": { "name": "Africa" },
        "geometry": {
          "type": "Polygon",
          "coordinates": [[
            [-18, -35], [52, -35], [52, 38], [-18, 38], [-18, -35]
          ]]
        }
      },
      {
        "type": "Feature",
        "properties": { "name": "Asia" },
        "geometry": {
          "type": "Polygon",
          "coordinates": [[
            [26, 1], [180, 1], [180, 81], [26, 81], [26, 1]
          ]]
        }
      },
      {
        "type": "Feature",
        "properties": { "name": "Australia" },
        "geometry": {
          "type": "Polygon",
          "coordinates": [[
            [112, -44], [154, -44], [154, -10], [112, -10], [112, -44]
          ]]
        }
      },
      {
        "type": "Feature",
        "properties": { "name": "Antarctica" },
        "geometry": {
          "type": "Polygon",
          "coordinates": [[
            [-180, -90], [180, -90], [180, -60], [-180, -60], [-180, -90]
          ]]
        }
      }
    ]
  };

  // Default style
  function defaultStyle(feature) {
    return {
      color: '#444',
      weight: 1,
      fillColor: '#3388ff',
      fillOpacity: 0.15
    };
  }

  // Highlight style on hover
  var highlightStyle = {
    weight: 2,
    color: '#ffcc00',
    fillOpacity: 0.35
  };

  // Add GeoJSON layer
  var continentsLayer = L.geoJSON(continentsGeo, {
    style: defaultStyle,
    onEachFeature: function(feature, layer) {
      layer.on({
        mouseover: function(e) {
          e.target.setStyle(highlightStyle);
        },
        mouseout: function(e) {
          continentsLayer.resetStyle(e.target);
        },
        click: function(e) {
          var name = feature.properties && feature.properties.name ? feature.properties.name : 'Region';
          console.log('Continent clicked:', name);
          // Update placeholder area
          var info = document.getElementById('region-info');
          var trending = document.getElementById('trending-placeholder');
          if (info) info.innerText = name;
          if (trending) {
            trending.innerHTML = '<p><strong>Trending movies in ' + name + '</strong></p>' +
              '<ul><li>Placeholder Movie A</li><li>Placeholder Movie B</li><li>Placeholder Movie C</li></ul>';
          }
          // Optionally fit map to this region
          try {
            map.fitBounds(e.target.getBounds(), { maxZoom: 4 });
          } catch (err) { /* ignore */ }
        }
      });
      // Make pointer cursor
      layer.setStyle({ interactive: true });
    }
  }).addTo(map);

  // Add a small legend / instruction control
  var infoControl = L.control({ position: 'bottomleft' });
  infoControl.onAdd = function() {
    var div = L.DomUtil.create('div', 'info-control');
    div.innerHTML = '<strong>Hover</strong> to highlight<br/><strong>Click</strong> to select region';
    return div;
  };
  infoControl.addTo(map);
})();
