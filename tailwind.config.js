/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./homepage/**/*.{html,js}"],
  theme: {
    fontFamily: {
      'display': ['Spectral', 'sans-serif'],
    },
    extend: {
      colors: {
        blue: "#252750",
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
        }
      }
    },
  },
  plugins: [require('@tailwindcss/forms')],
}