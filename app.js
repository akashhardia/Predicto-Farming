var express = require("express");
var app = express();
var bodyParser = require("body-parser");


app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static("startbootstrap-sb-admin-gh-pages"));
app.set("view engine", 'ejs');
app.set("views","startbootstrap-sb-admin-gh-pages");

app.get("/",function(req,res){
   res.render("index");
});

app.get("/predict",function(req,res){
    res.render("predict"); 
});

app.post("/predict",function(req,res){
    var Unnamed = req.body.Unnamed;
    var year = req.body.year;
    var quarter = req.body.quarter;
    var delay = req.body.delay;
    var dud = req.body.dud;
    var time = req.body.time;
    
    let obj = {
        "Unnamed: 0" : Unnamed ,
        "year": year,
        "quarter": quarter,
        "delay": delay,
        "dud": dud,
        "time": time
    } 
    var spawn = require("child_process").spawn,
        py = spawn('python', ['./predict_rain.py']),
        dataString = '';
    
    py.stdout.on('data', function(data){
      dataString += data.toString();
    });

    py.stdout.on('end', function(){
        res.render('result',{data:dataString});
    });
    
    py.stdin.write(JSON.stringify(obj));
    py.stdin.end(); 
    
});

app.listen(5000, function(err){
   console.log("server started"); 
});