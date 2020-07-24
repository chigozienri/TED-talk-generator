/* If you're feeling fancy you can add interactivity 
    to your site with Javascript */

// prints "hi" in the browser's dev tools console
// console.log("hi");

require(
    {
      // it makes sense to wait a little bit when you are loading
      // reveal from a cdn in a slow connection environment
      waitSeconds: 15
    },
    [
      "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0/lib/js/head.min.js",
      "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0/js/reveal.js"
    ],

    function(head, Reveal){

        // Full list of configuration options available here: https://github.com/hakimel/reveal.js#configuration
        Reveal.initialize({
            controls: false,
            progress: true,
            history: true,
            keyboard: {
              32: null,
            },

            transition: "slide",

            // Optional libraries used to extend on reveal.js
            dependencies: [
                { src: "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0/lib/js/classList.js",
                  condition: function() { return !document.body.classList; } },
                { src: "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0/plugin/notes/notes.js",
                  async: true,
                  condition: function() { return !!document.body.classList; } }
            ]
        });

        function setScrollingSlide() {
            var scroll = false
            if (scroll === true) {
              var h = $('.reveal').height() * 0.95;
              $('section.present').find('section')
                .filter(function() {
                  return $(this).height() > h;
                })
                .css('height', 'calc(95vh)')
                .css('overflow-y', 'scroll')
                .css('margin-top', '20px');
            }
        }

        // check and set the scrolling slide every time the slide change
        Reveal.addEventListener('slidechanged', setScrollingSlide);

    }

);
