let spawn = require('child_process').spawnSync;

let process = spawn('python', ['./hello.py']);

console.log(process.output[1].toString());