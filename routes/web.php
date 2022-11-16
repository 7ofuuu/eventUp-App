<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('home',[
        "title"=>"Home"
    ]);
});

Route::get('/event', function () {
    return view('event', [
        "title"=>"Event"
    ]);
});

Route::get('/about', function () {
    return view('about', [
        "title"=>"About"
    ]);
});

Route::get('/signin', function () {
    return view('loginpage', [
        "title"=>"SignIn"
    ]);
});

Route::get('/signup', function () {
    return view('signuppage', [
        "title"=>"SignUp"
    ]);
});