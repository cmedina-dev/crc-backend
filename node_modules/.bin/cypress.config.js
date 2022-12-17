const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
	supportFile: false,
	specPattern: '**/*.cy.{js,jsx,ts,tsx}',
    baseUrl: 'https://crc-counterapp.azurewebsites.net/api'
  }
})
