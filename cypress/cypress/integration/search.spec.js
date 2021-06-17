/// <reference types="cypress" />

describe('Busca de curso', function() {
  it('Busca de curso por professor', function() {

    cy.visit('https://www.estrategiaconcursos.com.br/')

    cy.get('a*[href="https://www.estrategiaconcursos.com.br/cursos/professor/"]').click({ force: true})

    cy.get('a*[href="https://www.estrategiaconcursos.com.br/cursosPorProfessor/ena-loiola-800/"]')
      .click({force: true, multiple: true})

    cy.get('.js-card-prod-container > section:nth-child(2) > div').as('anmIngles')
    
    cy.get('@anmIngles').invoke('text').then(function($value) {
      var res = $value.split(" ")
      var multiplicador = res[3].slice(0, 2)
      var valorParcelado = res[5].replace(',', '.')
      var valorTotal = Number(multiplicador) * Number(valorParcelado)

      cy.get('a*[href="https://www.estrategiaconcursos.com.br/curso/anm-ingles-2021-pre-edital/"]')
      .click({force: true, multiple: true})
      
      cy.get('div.cur-details-shopping-price > .value').should('contain', valorTotal)
    })    
  })

  it('Busca de curso por concurso', function() {

    cy.visit('https://www.estrategiaconcursos.com.br/')

    cy.get('div.nav-header-links > a:nth-child(2)').click({ force: true})

    cy.get('a*[href="https://www.estrategiaconcursos.com.br/cursosPorConcurso/cursos-para-policia-federal/"]')
      .click({force: true, multiple: true})

    cy.get('div.external-content > div > div:nth-child(5) > em > big > a').click()

    cy.get('div.cur-details-shopping-price > .value').invoke('text').then(function($value) {
      var res = $value.split(" ")
      var valorTotal = Number(res[2].replace(',', '.'))

      cy.get('.cur-details-buy > div.cur-details-shopping-installments').invoke('text').then(function($value) {
        res = $value.split(" ")
        var multiplicador = res[1].slice(0,2)
        var valorParcelado = res[4].replace(',', '.')
        var valorFinal = (Number(multiplicador) * Number(valorParcelado)).toFixed(1)

        expect(valorFinal).to.equals(valorTotal.toString())
      })
    })
  })    
  

  it('Busca de curso por matéria', function() {

    cy.visit('https://www.estrategiaconcursos.com.br/')

    cy.get('a*[href="https://www.estrategiaconcursos.com.br/cursos/materia/"]').click({ force: true})

     cy.get('.page-result-list > section:nth-child(58) > h1 > a').click()

     cy.get('.card-prod-price').as('assinaturaBasica')
    
    cy.get('@assinaturaBasica').invoke('text').then(function($value) {
      var res = $value.split(" ")
      var multiplicador = res[3].slice(0, 2)
      var valorParcelado = res[5].replace(',', '.')
      var valorTotal = Number(multiplicador) * Number(valorParcelado)

      cy.get('.js-card-prod-container > section:nth-child(1) > h1 > a').click()

      cy.get('.card-price > div:nth-child(2) > div.payment-details > div.detalhes').as('descontoAVista')

      cy.get('@descontoAVista').invoke('text').then(function($value) {
        res = $value.split(" ")
        var desconto = Number(res[0].slice(0, 2))

        var valorComDesconto = valorTotal * ((100 - desconto)/100)
        valorComDesconto = valorComDesconto.toFixed(2).replace(".", ",")

        cy.get('div:nth-child(6) > div.card-wrapper > div > div.card-price > div:nth-child(2) > div.payment-details > div.price').as('precoDesconto')
        cy.get('@precoDesconto').should('contain', valorComDesconto)
      })
      
    })    
  })
})