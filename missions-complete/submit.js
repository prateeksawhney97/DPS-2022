const axios = require('axios')
const hotpTotpGenerator = require('hotp-totp-generator')

const URL = 'https://dps-challenge.netlify.app/.netlify/functions/api/challenge';

const jsonBody = {
  github: 'https://github.com/prateeksawhney97/DPS-2022',
  email: 'Prateek.sawhney97@gmail.com',
  url: 'https://accidentdps.herokuapp.com/',
  notes:
    'In the GitHub repo, I have included the ML models, the endpoints (3 endpoints each for a particular accident category), visualization and code for the frontend app using Flask and ML code used for training and prediction from the model.'
};

const password = hotpTotpGenerator.totp({
  key: 'Prateek.sawhney97@gmail.comDPSCHALLENGE',
  X: 120,
  T0: 0,
  algorithm: 'sha512',
  digits: 10
});

const headers = {
  'Content-Type': 'application/json',
  'Authorization': `Basic ${password}`
};

axios
  .post(URL, jsonBody, { headers })
  .then((response) => console.log('Response', response))
  .catch((error) => console.log('Error', error));