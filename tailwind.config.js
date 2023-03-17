/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pathfinder/templates/**/*.{html,js}'
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui"), require("tailwindcss-flip")],
  daisyui: {
    styled: true,
    themes: ["night"],
    base: true,
    utils: true,
    logs: true,
    rtl: true,
    prefix: "",
    darkTheme: "night",
  },
}


