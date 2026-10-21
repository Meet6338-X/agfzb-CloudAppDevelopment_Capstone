import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// The React frontend is built with Vite. The `static` folder is mounted as the
// public directory so that the standalone About Us / Contact Us pages
// (static/About.html, static/Contact.html) are served as-is.
export default defineConfig({
  plugins: [react()],
  publicDir: 'static',
  server: {
    host: '0.0.0.0',
    port: 3000,
  },
  preview: {
    host: '0.0.0.0',
    port: 3000,
  },
  build: {
    outDir: 'dist',
  },
})
