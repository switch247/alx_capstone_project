const bcrypt = require('bcrypt');

async function encryptAndLog(input) {
  try {
    const salt = await bcrypt.genSalt();
    const encrypted = await bcrypt.hash(input, salt);
    console.log('Encrypted:', encrypted);
  } catch (error) {
    console.error('Error encrypting:', error);
  }
}

// Usage example
encryptAndLog('password');
// $2b$10$5euUd/hZl7pX0MDvl/avUuP1Tg8./AaDwb.SWOEqb31hvu5v6KvgC