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
                primary: {
                    50: "#eff6ff",
                    100: "#dbeafe",
                    200: "#bfdbfe",
                    300: "#93c5fd",
                    400: "#60a5fa",
                    500: "#3b82f6",
                    600: "#2563eb",
                    700: "#1d4ed8",
                    800: "#1e40af",
                    900: "#1e3a8a",
                },
                "kuning-100": "#fff1dd",
                "kuning-200": "#ffebcd",
                "kuning-300": "#ffe4bc",
                "kuning-400": "#ffdeac",
                "kuning-500": "#ffd79b",
                "kuning-600": "#ffd08a",
                "kuning-700": "#ffca7a",
                "kuning-800": "#ffc369",
                "kuning-900": "#ffbd59",
                // ?? warna pelengkap
                biru: "#599bff",
                salmon: "#ff6a59",
                insignia: "#32435a",
                "steel-blue": "#4682B4",
            },
            fontFamily: {
                poppins: ["Poppins"],
                inter: ["Inter"],
            },
        },
    },
    plugins: [require("flowbite/plugin")],
};
