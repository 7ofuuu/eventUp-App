<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        {{-- @vite('public/css/app.css') --}}
        <link rel="icon" href="{{ url('img/favicon-16x16.png') }}">
        <link rel="stylesheet" href="css/app.css">
        {{-- <link rel="stylesheet" href="css/style.css"> --}}
        <title>Home</title>
    </head>
<body class="flex flex-col min-h-screen">

    @include('partials.navbar')
    @yield('container')


    @include('partials.footer')
    <script src="{{ asset("js/slick.js") }}"></script>
</body>
</html>