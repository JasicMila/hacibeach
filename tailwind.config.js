/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./homepage/**/*.{html,js}"],
  safelist: [
    'font-special',
    'md:text-7xl',
    'text-5xl',
    'text-blue-light',
    'inline-block',
    'text-center',
    'md:text-left',
    'text-center',
    'text-xl',
    'text-blue',
    'text-blue-light',
    'w-full',
    'mb-5', 
    'text-3xl', 
    'font-bold', 
    'tracking-tight', 
    'text-gray-900', 
    'sm:text-4xl', 
    'sm:leading-none',
    'pr-5',
    'mb-5',
    'text-base',
    'text-gray-700',
    'md:text-lg',
    'order-0',
    'order-1',
    'md:order-0',
    'md:order-1',
  ],
  theme: {
    fontFamily: {
      'display': ['Spectral', 'sans-serif'],
      'special': ['Inspiration', 'handwriting'],
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