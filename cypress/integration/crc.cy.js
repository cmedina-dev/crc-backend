describe('Check Counter API', () => {
	it('Returns response code 200', () => {
		cy.request({
		  url: '/counter/get',
		  followRedirect: false,
		}).then((resp) => {
		  expect(resp.status).to.eq(200)
		})
	})
})
