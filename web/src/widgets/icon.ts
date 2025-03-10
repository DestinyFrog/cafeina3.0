import './icon.css'

class Icon {
	private static order: number = 0
	private div_icon: HTMLDivElement
	private img_icon: HTMLImageElement
	private p_title: HTMLParagraphElement

	constructor(title:string, icon:string, callback:Function) {
		const app = document.getElementById('app')!

		this.div_icon = document.createElement('div')
		this.div_icon.className = 'icon'
		this.div_icon.addEventListener('click', () => callback())
		app.appendChild(this.div_icon)

		this.img_icon = document.createElement('img')
		this.img_icon.width = 40
		this.img_icon.alt = `${title} icon`
		this.img_icon.src = icon
		this.div_icon.appendChild(this.img_icon)

		this.p_title = document.createElement('p')
		this.p_title.textContent = title
		this.div_icon.appendChild(this.p_title)
	
		Icon.order++
	}
}

export default Icon