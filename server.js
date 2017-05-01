let spawn = require('child_process').spawnSync;

var graph = require('fbgraph');

function getPrediction(sArea) {

    if (sArea == 'Santiago') {
        let process = spawn('python', ['./pystuff/get_prediction_santiago.py']);
        let mag = process.output[1].toString();
        if (mag) {
            return mag;
        } else {
            // return 'Error: Model Not Trained';
            return process.output[2].toString();
        }
    } else {
        return 'N/A';
    }

}

function trainModel(sArea, sEpochs) {
    if (sArea === 'Santiago') {
        let process = spawn('python', ['./pystuff/train_santiago.py', sEpochs]);
        return process.output[1].toString();
    }

}

let express = require('express');
let httpProxy = require('http-proxy');

let app = express();

app.use(express.static('ui'));

// let proxy = httpProxy.createProxyServer({
//     target: "https://moonshotp1940934211trial.hanatrial.ondemand.com",
//     changeOrigin: true
// });

// app.route("/earthquake-forecaster*").all((req, res) => {
//     proxy.web(req, res);
// });

app.route("/get-prediction").all((req, res) => {
    res.send(getPrediction(req.query.area));
});

app.route("/train-model").all((req, res) => {
    res.send(trainModel(req.query.area, req.query.epochs));
});

app.route('/post').all((req, res) => {
    graph.setAccessToken('EAACEdEose0cBAHZB06LVnX9IZAZC7vJZARAUAH1iTv3OmL55Qchlk70akigqHfspybXhpIsAfOUhVgGPg5kyZB6Pz1x9TS62PHIoO1yybMYTYoE4sARImdzI8MgLV2Qzeed4ZBwfKYI8ZCYJURhCalj4qeB66FsiwPw3uwgo0qbPZBlNmZB6nylJqVZCTs2VsZCpqAZD');

    let message = req.query.message

    graph.post("/766388870189994/feed", {
        message: message
    }, function(err, resp) {
        if(err)
            return console.error(err);
        
        res.status(200).end();
    });
});

let portNumber = '8000';
app.listen(process.env.PORT || portNumber, () => {
    console.log("Server started on port " + portNumber);
})