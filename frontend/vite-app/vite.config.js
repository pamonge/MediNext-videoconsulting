import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  server: {
    host: '0.0.0.0', // Permite acceso desde fuera del contenedor
    port: 3000,
    watch: {
      usePolling: true, // Necesario para hot-reload en Docker
    },
  },
  plugins: [
    react(),
    tailwindcss()
  ],
})
