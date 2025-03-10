import App from "./app"

class ErrorApp extends App {
	private err: Error
	private p_error: HTMLParagraphElement

	private header_color: string = "#aa2222"
	private content_color: string = "#dd4444"

	constructor(err:Error) {
		super("erro")
		this.err = err

		this.p_error = document.createElement("p")
		this.p_error.style.fontSize = "14px"
		this.p_error.style.maxWidth = "200px"
		this.appendToContent(this.p_error)
	}

	protected Render(): void {
		this.div_header.style.backgroundColor = this.header_color
		this.div_content.style.backgroundColor = this.content_color

		console.error(this.err)
		this.p_error.textContent = this.err.message
	}
}

export default ErrorApp