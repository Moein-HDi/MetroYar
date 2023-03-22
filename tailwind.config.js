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
    themes: [
      {
        light: {
          ...require("daisyui/src/colors/themes")["[data-theme=light]"],
          primary: "#FBBD23",
        },
      },
      {
        dark: {
          ...require("daisyui/src/colors/themes")["[data-theme=dark]"],
          primary: "#FBBD23",
        },
      },
    ],
    base: true,
    utils: true,
    logs: true,
    rtl: true,
    prefix: "",
    darkTheme: "mydark",
  },
}


