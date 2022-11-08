@extends('layouts.main')

@section('container')

<div id="default-carousel" class="relative  md:mt-28" data-carousel="static">
      <!-- Carousel wrapper -->
      <div class="relative h-64 overflow-hidden rounded-3xl mx-auto drop-shadow-md md:drop-shadow-lg  md:w-11/12 md:h-[360px]">
          <!-- Item 1 -->
          <div class="carousel-image duration-700 ease-in-out absolute inset-0 transition-all transform translate-x-0 z-20" data-carousel-item="">
              <span class="absolute text-2xl font-semibold text-white -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2 sm:text-3xl dark:text-gray-800">First Slide</span>
              <img src="{{ asset("img/banner-carousel-5.jpg") }}" class="absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2" alt="...">
          </div>
          <!-- Item 2 -->
          <div class="carousel-image duration-700 ease-in-out absolute inset-0 transition-all transform translate-x-full z-10" data-carousel-item="">
              <img src="{{ asset("img/banner-carousel-4.jpg") }}" class="absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2 object-scale-down md:object-scale-down" alt="...">
          </div>
          <!-- Item 3 -->
          <div class="carousel-image duration-700 ease-in-out absolute inset-0 transition-all transform -translate-x-full z-10" data-carousel-item="">
              <img src="{{ asset("img/banner-carousel-5.jpg") }}" class="absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2 object-scale-down md:object-scale-down" alt="...">
          </div>
      </div>
      <!-- Slider indicators -->
      <div class="absolute z-30 flex space-x-3 -translate-x-1/2 bottom-3 left-1/2">
          <button type="button" class="w-3 h-3 rounded-full bg-white dark:bg-gray-800" aria-current="true" aria-label="Slide 1" data-carousel-slide-to="0"></button>
          <button type="button" class="w-3 h-3 rounded-full bg-white/50 dark:bg-gray-800/50 hover:bg-white dark:hover:bg-gray-800" aria-current="false" aria-label="Slide 2" data-carousel-slide-to="1"></button>
          <button type="button" class="w-3 h-3 rounded-full bg-white/50 dark:bg-gray-800/50 hover:bg-white dark:hover:bg-gray-800" aria-current="false" aria-label="Slide 3" data-carousel-slide-to="2"></button>
      </div>
      <!-- Slider controls -->
      <button type="button" class="absolute top-0 left-12 z-30 flex items-center justify-center h-2 px-4 cursor-pointer group focus:outline-none md:h-full" data-carousel-prev="">
          <span class="inline-flex items-center justify-center w-8 h-8 rounded-full sm:w-10 sm:h-10 bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none">
              <svg aria-hidden="true" class="w-5 h-5 text-white sm:w-6 sm:h-6 dark:text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
              <span class="sr-only">Previous</span>
          </span>
      </button>
      <button type="button" class="absolute top-0 right-12 z-30 flex items-center justify-center h-2 px-4 cursor-pointer group focus:outline-none md:h-full" data-carousel-next="">
          <span class="inline-flex items-center justify-center w-8 h-8 rounded-full sm:w-10 sm:h-10 bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none">
              <svg aria-hidden="true" class="w-5 h-5 text-white sm:w-6 sm:h-6 dark:text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
              <span class="sr-only">Next</span>
          </span>
      </button>
</div>



{{--?? Card --}}

<div class="grid grid-rows-1 gap-2 mt-2 w-full  p-1 mx-auto md:w-11/12 md:grid-cols-5 md:gap-5 md:mt-10 ">
    {{-- ?? card desktop view --}}
    
    <div class="max-w-sm bg-white rounded-lg border border-gray-200 shadow-md hidden md:inline dark:bg-gray-800 dark:border-gray-700">
        <a href="#">
            <img class="rounded-t-lg" src="{{ asset("img/banner-1.jpeg") }}" alt="">
        </a>
        <div class="p-5">
            <a href="#">
                <h5 class="mb-2 text-base font-inter font-bold tracking-tight text-gray-900 md:text-xl dark:text-white">Summer Night Party</h5>
            </a>
            <p class="mb-3 font-normal text-gray-700 text-sm md:text-base dark:text-gray-400">Card desktop view</p>

            <a href="" class="relative inline-flex items-center justify-center px-[3px] py-[3px] overflow-hidden font-medium text-indigo-600 transition duration-300 ease-out border-2 border-indigo-700 rounded-lg shadow-md group">
                <span class="absolute inset-0 flex items-center justify-center w-full h-full text-white duration-300 -translate-x-full bg-indigo-700 group-hover:translate-x-0 ease">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                </span>
                <span class="absolute flex items-center justify-center text-sm w-full h-full text-indigo-700 transition-all duration-300 transform group-hover:translate-x-full ease">Read more</span>
                <span class="relative invisible">Read more</span>
                </a>
        </div>
    </div>

    <div class="max-w-sm bg-white rounded-lg border border-gray-200 shadow-md hidden md:inline dark:bg-gray-800 dark:border-gray-700">
        <a href="#">
            <img class="rounded-t-lg" src="{{ asset("img/banner-1.jpeg") }}" alt="">
        </a>
        <div class="p-5">
            <a href="#">
                <h5 class="mb-2 text-base font-inter font-bold tracking-tight text-gray-900 md:text-xl dark:text-white">Summer Night Party</h5>
            </a>
            <p class="mb-3 font-normal text-gray-700 text-sm md:text-base dark:text-gray-400">Card desktop view</p>

            <a href="" class="relative inline-flex items-center justify-center px-[3px] py-[3px] overflow-hidden font-medium text-indigo-600 transition duration-300 ease-out border-2 border-indigo-700 rounded-lg shadow-md group">
                <span class="absolute inset-0 flex items-center justify-center w-full h-full text-white duration-300 -translate-x-full bg-indigo-700 group-hover:translate-x-0 ease">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                </span>
                <span class="absolute flex items-center justify-center text-sm w-full h-full text-indigo-700 transition-all duration-300 transform group-hover:translate-x-full ease">Read more</span>
                <span class="relative invisible">Read more</span>
                </a>
        </div>
    </div>

    <div class="max-w-sm bg-white rounded-lg border border-gray-200 shadow-md hidden md:inline dark:bg-gray-800 dark:border-gray-700">
        <a href="#">
            <img class="rounded-t-lg" src="{{ asset("img/banner-1.jpeg") }}" alt="">
        </a>
        <div class="p-5">
            <a href="#">
                <h5 class="mb-2 text-base font-inter font-bold tracking-tight text-gray-900 md:text-xl dark:text-white">Summer Night Party</h5>
            </a>
            <p class="mb-3 font-normal text-gray-700 text-sm md:text-base dark:text-gray-400">Card desktop view</p>

            <a href="" class="relative inline-flex items-center justify-center px-[3px] py-[3px] overflow-hidden font-medium text-indigo-600 transition duration-300 ease-out border-2 border-indigo-700 rounded-lg shadow-md group">
                <span class="absolute inset-0 flex items-center justify-center w-full h-full text-white duration-300 -translate-x-full bg-indigo-700 group-hover:translate-x-0 ease">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                </span>
                <span class="absolute flex items-center justify-center text-sm w-full h-full text-indigo-700 transition-all duration-300 transform group-hover:translate-x-full ease">Read more</span>
                <span class="relative invisible">Read more</span>
                </a>
        </div>
    </div>

    <div class="max-w-sm bg-white rounded-lg border border-gray-200 shadow-md hidden md:inline dark:bg-gray-800 dark:border-gray-700">
        <a href="#">
            <img class="rounded-t-lg" src="{{ asset("img/banner-1.jpeg") }}" alt="">
        </a>
        <div class="p-5">
            <a href="#">
                <h5 class="mb-2 text-base font-inter font-bold tracking-tight text-gray-900 md:text-xl dark:text-white">Summer Night Party</h5>
            </a>
            <p class="mb-3 font-normal text-gray-700 text-sm md:text-base dark:text-gray-400">Card desktop view</p>

            <a href="" class="relative inline-flex items-center justify-center px-[3px] py-[3px] overflow-hidden font-medium text-indigo-600 transition duration-300 ease-out border-2 border-indigo-700 rounded-lg shadow-md group">
                <span class="absolute inset-0 flex items-center justify-center w-full h-full text-white duration-300 -translate-x-full bg-indigo-700 group-hover:translate-x-0 ease">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                </span>
                <span class="absolute flex items-center justify-center text-sm w-full h-full text-indigo-700 transition-all duration-300 transform group-hover:translate-x-full ease">Read more</span>
                <span class="relative invisible">Read more</span>
                </a>
        </div>
    </div>

    <div class="max-w-sm bg-white rounded-lg border border-gray-200 shadow-md hidden md:inline dark:bg-gray-800 dark:border-gray-700">
        <a href="#">
            <img class="rounded-t-lg" src="{{ asset("img/banner-1.jpeg") }}" alt="">
        </a>
        <div class="p-5">
            <a href="#">
                <h5 class="mb-2 text-base font-inter font-bold tracking-tight text-gray-900 md:text-xl dark:text-white">Summer Night Party</h5>
            </a>
            <p class="mb-3 font-normal text-gray-700 text-sm md:text-base dark:text-gray-400">Card desktop view</p>

            <a href="" class="relative inline-flex items-center justify-center px-[3px] py-[3px] overflow-hidden font-medium text-indigo-600 transition duration-300 ease-out border-2 border-indigo-700 rounded-lg shadow-md group">
                <span class="absolute inset-0 flex items-center justify-center w-full h-full text-white duration-300 -translate-x-full bg-indigo-700 group-hover:translate-x-0 ease">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                </span>
                <span class="absolute flex items-center justify-center text-sm w-full h-full text-indigo-700 transition-all duration-300 transform group-hover:translate-x-full ease">Read more</span>
                <span class="relative invisible">Read more</span>
                </a>
        </div>
    </div>

    <div class="max-w-sm bg-white rounded-lg border border-gray-200 shadow-md hidden md:inline dark:bg-gray-800 dark:border-gray-700">
        <a href="#">
            <img class="rounded-t-lg" src="{{ asset("img/banner-1.jpeg") }}" alt="">
        </a>
        <div class="p-5">
            <a href="#">
                <h5 class="mb-2 text-base font-inter font-bold tracking-tight text-gray-900 md:text-xl dark:text-white">Summer Night Party</h5>
            </a>
            <p class="mb-3 font-normal text-gray-700 text-sm md:text-base dark:text-gray-400">Card desktop view</p>

            <a href="" class="relative inline-flex items-center justify-center px-[3px] py-[3px] overflow-hidden font-medium text-indigo-600 transition duration-300 ease-out border-2 border-indigo-700 rounded-lg shadow-md group">
                <span class="absolute inset-0 flex items-center justify-center w-full h-full text-white duration-300 -translate-x-full bg-indigo-700 group-hover:translate-x-0 ease">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                </span>
                <span class="absolute flex items-center justify-center text-sm w-full h-full text-indigo-700 transition-all duration-300 transform group-hover:translate-x-full ease">Read more</span>
                <span class="relative invisible">Read more</span>
                </a>
        </div>
    </div>  

    


    
    {{--?? Card mobile view --}}
    <a href="#" class="flex flex-row items-center bg-white rounded-lg border shadow-md drop-shadow-lg md:hidden  md:flex-col md:max-w-xl hover:bg-gray-100 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700">
        <img class="object-cover w-32 h-32 ml-1 rounded-lg md:h-auto md:w-48 md:rounded-none md:rounded-l-lg" src="{{ asset("img/banner-1.jpeg") }}" alt="">
        <div class="flex flex-col justify-between p-4 leading-normal">
            <h5 class="mb-2 text-sm font-bold tracking-tight text-gray-900 dark:text-white">Noteworthy technology acquisitions 2021</h5>
            <p class="mb-3 font-normal text-xs text-gray-700 dark:text-gray-400">Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.</p>
        </div>
    </a>  
</div>
@endsection

