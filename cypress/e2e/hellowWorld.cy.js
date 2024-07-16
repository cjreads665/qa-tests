describe('template spec', () => {
  it('passes', () => {
    cy.visit('/')
    console.log(Cypress.env('vars'));
  })
})