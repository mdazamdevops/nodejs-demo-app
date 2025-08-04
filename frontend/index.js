const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const app = express();

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: false }));

const API_URL = 'http://localhost:5000/api/todos';

app.get('/', async (req, res) => {
  const response = await axios.get(API_URL);
  res.render('index', { todos: response.data });
});

app.post('/add', async (req, res) => {
  await axios.post(API_URL, { task: req.body.task });
  res.redirect('/');
});

app.get('/delete/:id', async (req, res) => {
  await axios.delete(`${API_URL}/${req.params.id}`);
  res.redirect('/');
});

app.listen(3000, () => console.log('Frontend running at http://localhost:3000'));