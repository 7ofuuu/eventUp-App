/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./resources/**/*.blade.php",
        "./resources/**/*.js",
        "./resources/**/*.vue",
    ],
    theme: {
        extend: {
            colors: {
                kuning: "#ffde59",
            },
        },
    },
    plugins: [require("flowbite/plugin")],
};
