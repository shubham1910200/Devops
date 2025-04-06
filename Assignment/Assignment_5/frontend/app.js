const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const app = express();
const PORT = 3000;

app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.send(`
    <form method="POST" action="/submit">
      <label>Name:</label><br/>
      <input name="name" required/><br/>
      <label>Email:</label><br/>
      <input name="email" required/><br/>
      <button type="submit">Submit</button>
    </form>
  `);
});

app.post('/submit', async (req, res) => {
  const { name, email } = req.body;

  try {
    const response = await axios.post('http://backend:5000/submit', { name, email });
    res.send(`Backend Response: ${response.data}`);
  } catch (err) {
    res.status(500).send('Error sending data to Flask backend');
  }
});

app.listen(PORT, () => {
  console.log(`Frontend running on port ${PORT}`);
});
