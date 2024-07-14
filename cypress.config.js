const { defineConfig } = require("cypress");

module.exports = defineConfig({
  baseUrl: "http://127.0.0.1:42733",
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
