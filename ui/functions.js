var map;

function postOnFB() {

    let encodedMessage = encodeURI($('#fbMessage').val());

    $.ajax('/post?message=' + encodedMessage , {
        method: 'GET',
        async: 'true'
    }).done(function(e){

        // Show snackbar on completion of training
        // Get the snackbar DIV
        // var x = document.getElementById("snackbar");

        // x.innerText = "Successfully shared on Facebook";

        // // Add the "show" class to DIV
        // x.className = "show";

        // // After 3 seconds, remove the show class from DIV
        // setTimeout(function () { x.className = x.className.replace("show", ""); }, 3000);

        $('.message-toast').text("Successfully shared on Facebook").fadeIn(400).delay(3000).fadeOut(400);

    });

}

function openFBModal() {

    let sMag = $("#prediction-modal .magnitude").text();
    let sArea = $("#area").val();
    let sAccuracy = $("#prediction-modal #accuracy").text();

    $("#fbMessage").val("Earthquake Alert! An earthquake of magnitude " + sMag +
    " has been predicted in the " + sArea + " area with " + sAccuracy + "% accuracy.");

    $('.post-fb-modal').modal('show');

}

function trainModel() {

    let sRegion = $("#area").val();
    let sEpochs = $("#epochs").val();

    $("#epochs").val("");

    // Show the training model image
    $("#training-overlay").show();

    // Send ajax request to train image
    $.ajax('/train-model?area=' + sRegion + '&epochs=' + sEpochs, {
        method: 'GET',
        async: true
    }).done(function (data) {

        // Show the training model image
        $("#training-overlay").hide();

        // Show snackbar on completion of training
        // // Get the snackbar DIV
        // var x = document.getElementById("snackbar");

        // // Add the "show" class to DIV
        // x.className = "show";

        // // After 3 seconds, remove the show class from DIV
        // setTimeout(function () { x.className = x.className.replace("show", ""); }, 3000);

        $('.message-toast').text("Training complete").fadeIn(400).delay(3000).fadeOut(400);

    });

}


function retrainModel() {

    $('.retrain-modal').modal('show');

}


function onPolygonClick(event) {

    let sRegionName = this.objInfo.name;

    // Set the modal title to the region name
    $('.modal-body .place-name').text(sRegionName);

    // Get the forecasted value
    $.ajax('/get-prediction?area=' + sRegionName, {
        method: 'GET',
        async: true
    }).done(function (data) {

        data = data.trim();
        data = data.split(":");

        $("#prediction-modal .magnitude").text(data[0]);
        $("#prediction-modal #accuracy").text(data[1]);
        $('#prediction-accuracy').css('width', data[1]+'%')

        $('.prediction-modal').modal('show');

    });

}

function drawSeismicRegions() {

    let aSeismicRegions = [
        {
            name: 'Santiago',
            coords: [
                { lat: -33, lng: -71 },
                { lat: -34, lng: -71 },
                { lat: -34, lng: -70 },
                { lat: -33, lng: -70 }
            ]
        }, {
            name: 'Talca',
            coords: [
                { lat: -35, lng: -72 },
                { lat: -36, lng: -72 },
                { lat: -36, lng: -71 },
                { lat: -35, lng: -71 }
            ]
        }, {
            name: 'Valparaiso',
            coords: [
                { lat: -32.5, lng: -72 },
                { lat: -33.5, lng: -72 },
                { lat: -33.5, lng: -71 },
                { lat: -32.5, lng: -71 }
            ]
        }, {
            name: 'Pichilemu',
            coords: [
                { lat: -34, lng: -72.5 },
                { lat: -34.5, lng: -72.5 },
                { lat: -34.5, lng: -72 },
                { lat: -34, lng: -72 }
            ]
        }
    ];

    aSeismicRegions.map(function (e) {

        return {
            polygon: new google.maps.Polygon({
                paths: e.coords,
                strokeColor: '#FF0000',
                strokeOpacity: 0.5,
                strokeWeight: 1,
                fillColor: '#FF0000',
                fillOpacity: 0.15
            }),
            name: e.name
        };

    }).map(function (e) {

        e.polygon.objInfo = {
            name: e.name
        }

        e.polygon.addListener('click', onPolygonClick);

        e.polygon.setMap(map);

    });



}

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: -34, lng: -71.5 },
        zoom: 7,
        // draggable: false,
        // panControl: false,
        // scrollwheel: false,
        mapTypeControlOptions: {
            mapTypeIds: []
        }
    });


    // Draw the seismic regions
    drawSeismicRegions();

}