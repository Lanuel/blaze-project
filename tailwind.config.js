/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './**/templates/**/*.html',
    './static/**/*.css',
    './src/**/*.css',
  ],
  theme: {
    extend: {
      fontFamily: {
        'moderniz': ['moderniz', 'sans-serif'],
        'futura-medium': ['Futura-medium', 'sans-serif'],
        'futura-book': ['Futura-book', 'sans-serif'],
      },
    },
  },
  corePlugins: {
    fontFamily: true, // Ensure this is enabled
  },
  plugins: [],
}