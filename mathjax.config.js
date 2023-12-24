    window.MathJax = {
      tex2jax: {
        inlineMath:  [ ['$','$'], ['\\(','\\)'] ], # Double backslashes because backslash is an escape character in JavaScript strings
        displayMath: [ ['$$','$$'], ['\\[','\\]'] ],
        processEscapes: true
      },
      TeX: { extensions: ["autoload-all.js"] }
    };