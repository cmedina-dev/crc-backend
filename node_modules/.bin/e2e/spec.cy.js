describe('Get counter API', () => {
	it('Returns response code 200', () => {
		cy.request({
		  url: '/counter/get',
		  followRedirect: false,
		}).then((resp) => {
		  expect(resp.status).to.eq(200)
		})
	})
})

describe('Increment counter API', () => {
	it('Returns response code 200', () => {
		cy.request({
		  url: '/counter/increment',
		  followRedirect: false,
		}).then((resp) => {
		  expect(resp.status).to.eq(200)
		})
	})
})
