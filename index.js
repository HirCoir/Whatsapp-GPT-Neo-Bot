const venom = require('venom-bot');
const { exec } = require('child_process');

venom.create({
  session: 'session-name', // nombre de sesión
  puppeteerOptions: {
    args: ['--no-sandbox']
  },
}).then((client) => start(client))
  .catch((error) => console.log(error));

function start(client) {
  client.onMessage((message) => {
    const prompt = message.body;
    if (prompt) {
      exec(`python3 gpt.py "${prompt}"`, (error, stdout, stderr) => {
        if (error) {
          console.error(`exec error: ${error}`);
          return;
        }
        const response = stdout.trim();
        client.sendText(message.from, response);
      });
    }
  });
}
