function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
      if(uiBHK[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    //alert(sqft)
    var bhk = getBHKValue();
    //alert(bhk)
    var bathrooms = getBathValue();
    //alert(bathrooms)
    var location = document.getElementById("uiLocations");
    //alert(location)
    var estPrice = document.getElementById("uiEstimatedPrice");
  
     var url = "http://127.0.0.1:5000/predict_home_price"; 
  
    $.post(url, {
        area: parseFloat(sqft.value),
        bedrooms: bhk,
        baths: bathrooms,
        location: location.value
    },function(data, status) {
        console.log(data.Estimated_Price);
        estPrice.innerHTML = "<h3>" + data.Estimated_Price.toString() + "</h2>";
        console.log(status);
    });
  }
  
  function onPageLoad() {
    console.log( "document loaded" );
   var url = "http://127.0.0.1:5000/get_location_name"; 

    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.location;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
  }
  
  window.onload = onPageLoad;