
var pg = require('pg');
//or native libpq bindings
//var pg = require('pg').native

var conString = "postgres://ryfqjoce:Hedb1a0pf8vXhlFyupdacVfIZcUGRMCn@baasu.db.elephantsql.com:5432/ryfqjoce" //Can be found in the Details page
var client = new pg.Client(conString);
client.connect(function(err) {
  if(err) {
    return console.error('could not connect to postgres', err);
  }
  client.query('SELECT * FROM "users"', function(err, result) {
    if(err) {
      return console.error('error running query', err);
    }
    console.log(result.rows);
    // >> output: 2018-08-23T14:02:57.117Z
   
  });
  client.query('SELECT * FROM "resturants"', function(err, result) {
    if(err) {
      return console.error('error running query', err);
    }
    console.log(result.rows);
    // >> output: 2018-08-23T14:02:57.117Z
    
  });
  client.query('INSERT INTO users (name, username, password, resturants) VALUES ($1, $2, $3, $4)', ["Henry", "username", "Password", ["some","resutr","ant"]], function(err, result) {
    if(err) {
      return console.error('error running query', err);
    }
    console.log(result.rows);
    // >> output: 2018-08-23T14:02:57.117Z
   
  });
  client.query('SELECT * FROM "users"', function(err, result) {
    if(err) {
      return console.error('error running query', err);
    }
    console.log(result.rows);
    // >> output: 2018-08-23T14:02:57.117Z
   client.end;
  });

});

