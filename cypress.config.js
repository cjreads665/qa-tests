const { defineConfig } = require("cypress");
require('dotenv').config()
module.exports = defineConfig({
  env:{
    vars : {...process.env} //FOR OTHER VALUES IF ANY
  },
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    baseUrl: process.env.CYPRESS_BASE_URL
  },
});
