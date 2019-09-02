
#!/usr/bin/env node

const express = require("express");
var bodyParser = require("body-parser");
const { PythonShell } = require("python-shell");
const app = express();
const port = 3000;

app.get("/", (req, res) => res.send("Hello World!"));

let options = {
  mode: "text",
  args: ["value1"]
};

app.get("/nextBuy", (req, res) => {
  PythonShell.run("./dummy.py", options, function(err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    let dataResponse = JSON.parse(results);
    return res.send(dataResponse);
  });
});

var jsonParser = bodyParser.json();

app.post("/nextBuy", jsonParser, (req, res) => {
  PythonShell.run(
    "./dummy.py",
    {
      mode: "text",
      args: [req.body.buy]
    },
    function(err, results) {
      if (err) throw err;
      // results is an array consisting of messages collected during execution
      let dataResponse = JSON.parse(results);
      return res.send(dataResponse);
    }
  );

  // console.log(req); // your JSON
  // return res.send(req.body); // echo the result back
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`));

// var myPythonScriptPath = './dummy.py';

// // Use python shell
// var PythonShell = require('python-shell');
// var pyshell = new PythonShell(myPythonScriptPath);

// pyshell.on('message', function (message) {
//     // received a message sent from the Python script (a simple "print" statement)
//     console.log(message);
// });

// // end the input stream and allow the process to exit
// pyshell.end(function (err) {
//     if (err){
//         throw err;
//     };

//     console.log('finished');
// });
