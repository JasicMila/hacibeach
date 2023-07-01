/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./homepage/**/*.{html,js}"],
  theme: {
    fontFamily: {
      'display': ['Spectral', 'sans-serif'],
      'special': ['Bayshore', 'sans-serif'],
    },
    extend: {
      colors: {
        blue: {
          DEFAULT: "#252750",
          light: "#afb3ff",
          baby: '#76A1FF',
        },
        white: {
          DEFAULT: "#FFFFFF",
          floral: '#FEFBF4',
          old: '#F8F0E0',
          light: '#FFFCF5',
          cream: '#FDFBEC'
        },
        yellow: {
          DEFAULT: '#FFD476',
          light: '#FDFBEC',
          kaki: '#997628',
        }
      }
    },
  },
  plugins: [require('@tailwindcss/forms')],
}