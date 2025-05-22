/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        casino: {
          red: '#D4145A',
          gold: '#FFD700',
          dark: '#1A1A2E',
        }
      },
      keyframes: {
        spin: {
          '0%': { transform: 'translateY(0)' },
          '100%': { transform: 'translateY(-100%)' }
        }
      },
      animation: {
        'spin-reel': 'spin 0.5s linear infinite',
      }
    },
  },
  plugins: [],
}