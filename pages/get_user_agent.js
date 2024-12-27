(function() {
    const userAgent = navigator.userAgent;
    const streamlit = window.streamlit;
    streamlit.setComponentValue(userAgent);
})();