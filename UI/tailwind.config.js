/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./public/**/*.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors:{
        primary:{
          100:"#C1EDC6",
          200:"#DEE8DF",
          300:"#467B55",
          400:"#95B89F",
          500:"#9DBDA5",
          600:"#255231",
          700:"#FDFDFD"}

    
          

      }
    },
  },
  plugins: [],
}
