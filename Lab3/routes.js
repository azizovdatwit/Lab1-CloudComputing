const express = require('express');
const app = express();

app.use(express.json());

const houses = {
  gryffindor: { founder: "Godric Gryffindor", mascot: "Lion", colors: ["Red", "Gold"], head: "Professor McGonagall" },
  hufflepuff: { founder: "Helga Hufflepuff", mascot: "Badger", colors: ["Yellow", "Black"], head: "Professor Sprout" },
  ravenclaw: { founder: "Rowena Ravenclaw", mascot: "Eagle", colors: ["Blue", "Bronze"], head: "Professor Flitwick" },
  slytherin: { founder: "Salazar Slytherin", mascot: "Serpent", colors: ["Green", "Silver"], head: "Professor Snape" }
};

app.get('/', (req,res) => {
    res.send('<h1>Welcome to the HP world!</h1>');
});

app.get('/houses', (req,res) =>{
    res.json(houses);
});

app.get('/house', (req,res) =>{
    const name=req.query.name;
    const house=houses[name];
    res.send(`<h2>${name} House Details</h2>
    <p>${house.founder}, ${house.mascot}</p>`);


});
app.get('/sortingHat', (req, res) => {
  const student = req.query.student;
  res.json({ message: `The sorting hat is not sure about what house to place ${student}` });
});

app.get('/house/head', (req, res) => {
  const name = req.query.name;
  const house = houses[name];
  res.send(`<h2>Head of ${name}: ${house.head}</h2>`);
});

app.get('/spells', (req, res) => {
  const spell = req.query.spell;
  res.json({ message: `We need to learn how to do ${spell}` });
});

app.get('/house/mascot', (req, res) => {
  const name = req.query.name;
  const house = houses[name];
  res.send(`<h2>Mascot of ${name}: ${house.mascot}</h2>`);
});
app.get('/bestCharacter', (req,res) => {
    const name=req.query.name;
    res.json({ message: `${name} is indeed a great character` });
});

app.get('/verify-house', (req, res) => {
  const house = req.headers['house'];
  if (house === 'Hufflepuff') {
    res.send('Hufflepuff');
  } else {
    res.send('Not Hufflepuff');
  }
});

app.post('/welcome', (req, res) => {
  const { name, house } = req.body;
  res.send(`${name}, welcome to ${house}`);
});




app.listen(8080, () => {
  console.log('Server running on http://localhost:8080');
});