import './style.css'

import PeriodicTableApp from './app/periodicTableApp'
import Icon from './widgets/icon'

new Icon("Tabela Periódica", "icon_periodic_table.svg", () => {
	const a = new PeriodicTableApp()
	a.Start()
})