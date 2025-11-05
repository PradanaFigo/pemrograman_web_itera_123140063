/// <reference types="vitest" />
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  test: {
    globals: true, // Ini agar Anda tidak perlu 'import { it, describe }'
    environment: 'jsdom', // Menggunakan "browser palsu"
    setupFiles: './src/setupTests.js', // File setup (akan kita buat di Langkah 4)
  },
})