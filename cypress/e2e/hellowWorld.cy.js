describe('template spec', () => {
  it('passes', () => {
    cy.visit('/')
    cy.get('h1').contains("Hello from the Backend!")
  })
})