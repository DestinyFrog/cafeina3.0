import './periodicTableApp.css'

import { API_URL } from "../configuration"
import App from "../widgets/app"
import ErrorApp from '../widgets/errorApp'
import ElementApp from './elementApp'
import { CategoryToColor } from '../util'

class PeriodicTableApp extends App {
	private div_periodic_table: HTMLDivElement
	private elements = []

	constructor() {
		super("Tabela Periódica")

		this.div_periodic_table = document.createElement("div")
		this.div_periodic_table.className = 'periodic-table'
		this.appendToContent(this.div_periodic_table)
	}

	private async loadElements() {
		try {
			const res = await fetch(`${API_URL}/element`)
			this.elements = await res.json()
		}
		catch (err) {
			throw err
		}
	}

	protected Render(): void {
		this.loadElements()
		.then( () =>
			this.generatePeriodicTable() )
		.catch(err => {
			const e = new ErrorApp(err)
			e.Start()
			this.Close()
		})
	}

	private generatePeriodicTable() {
		this.elements?.forEach((element:any) => {
			const element_container = this.generateElementContainer(element)
			this.div_periodic_table.appendChild(element_container)
		})
	}

	private generateElementContainer(element:any) {
		const div_element = document.createElement('div')
		div_element.className = 'element'
		div_element.style.backgroundColor = CategoryToColor(element.category)

		div_element.addEventListener('click', () => {
			const w = new ElementApp(element)
			w.Start()
		})

		div_element.style.gridColumn = element.pos.x.toString()
		div_element.style.gridRow = element.pos.y.toString()

		const p_symbol = document.createElement('p')
		p_symbol.textContent = element.symbol
		div_element.appendChild(p_symbol)

		return div_element
	}
}

export default PeriodicTableApp