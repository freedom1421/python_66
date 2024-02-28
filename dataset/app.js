// const LineNotify = require("src/client");
const express = require('express')
const bodyParser = require('body-parser')
const app = express()
const port = 7002
const expressFileupload = require('express-fileupload')
const knex = require('knex')({
  client: 'mysql',
  connection: {
    host: 'localhost',
    port: 3306,
    user: 'root',
    password: '',
    database: 'webcam'
  }
})

app.get('/', (req, res) => {
  res.send({ ok: 1 })
})

app.use(bodyParser.json())
app.use(expressFileupload())

app.post('/face-check', async (req, res) => {
 
  res.send({
    ok: 1,
    result,
  })
})

app.post('/face-register', async (req, res) => {
  console.log(req.files.photo)
  console.log("send  photo")
  if (!req.body.username) {
    return res.send({ ok: 0, error: 'username is required' })
  }
  if (!req.files.photo) {
    return res.send({ ok: 0, error: 'photo is required' })
  }
    // console.log("person=",person.name)

  console.log('update ok')
  res.send({
    ok: 1,
  })
})




app.post('/python', (req, res) => {
  console.log(req.body.classNamest);
  console.log(req.body.classNamest.person);
  res.send({
    ok: 1,
  });
});
app.listen(port, () => console.log(`Example app listening on port ${port}!`))