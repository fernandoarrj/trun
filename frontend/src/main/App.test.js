import React from 'react'
import { render } from '@testing-library/react'

import App from './App'

describe('App Testing Component', () => {

	it('should render a app component', () => {
		const { container } = render(<App />)
		const app = container.firstChild
	
		expect(app.tagName).toBe('DIV')
	})
})
