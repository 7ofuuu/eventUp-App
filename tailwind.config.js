/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
  },
  prefix: 'tw-',
  corePlugins: {
    preflight: false,},
  plugins: [
    require('flowbite/plugin')
  ],
}
