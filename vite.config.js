import dotenv from 'dotenv'

dotenv.config()

export default {
	root: "web",
	build: {
		outDir: "../build",
		emptyOutDir: true
	}
}