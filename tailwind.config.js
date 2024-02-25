/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ["./templates/**/*.html", "./static/js/*.js"],
  theme: {
    extend: {
      colors: {
        pri: "#212529",
        secondary: "#343a40",
        main: "#bddb39",
        sub: "#0f151c",
        light: "#83d2c0",
      },
      fontFamily: {
        workSans: ["Work Sans", "sans-serif"],
        lato: ["Lato", "sans-serif"],
      },
    },
    screens: {
      xs: "480px",
      ss: "620px",
      sm: "768px",
      md: "1060px",
      lg: "1200px",
      xl: "1700px",
      xss: "360px",
    },
  },
  plugins: [],
};
