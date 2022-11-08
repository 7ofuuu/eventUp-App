<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
        <link rel="icon" href="{{ url('img/favicon-16x16.png') }}">
        <link rel="stylesheet" href="css/app.css">
        <link rel="stylesheet" href="{{ asset("css/slick.css") }}">
        <link rel="stylesheet" href="{{ asset("css/slick-theme.css") }}">
        <link rel="stylesheet" href="css/style.css">
        <title>EventUp | {{ $title }}</title>
    </head>
<body>

    @include('partials.navbar')
    @yield('container')


    @include('partials.footer')


    <script type="text/javascript" src="//code.jquery.com/jquery-1.11.0.min.js"></script>
    <script type="text/javascript" src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
    <script src="{{ asset("js/slick.js") }}"></script>
    <script src="{{ asset("js/script.js") }}"></script>
</body>
</html>