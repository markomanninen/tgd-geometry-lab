window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,
    processEnvironments: true,
  },
  options: { skipHtmlTags: ["script", "noscript", "style", "textarea", "pre", "code"] },
  chtml: { scale: 1.18, minScale: 0.8, matchFontHeight: false },
};
