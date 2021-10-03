import { createClient } from 'redis';

(async () => {
  const client = createClient();

  client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

  await client.connect();

  console.log('Redis client connected to the server');

  /* await client.set('key', 'value');
  const value = await client.get('key'); */
})();
