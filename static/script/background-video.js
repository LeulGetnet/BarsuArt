// Safari (especially on macOS) can be strict about autoplay.
// We keep the video muted + playsinline and attempt to start it
// after a few lifecycle events. If it still fails, we start it on
// the first user gesture.

(function () {
  function attemptPlay(video) {
    if (!video) return;

    // These attributes are required for autoplay on iOS and help on macOS.
    video.muted = true;
    video.setAttribute('muted', '');
    video.setAttribute('playsinline', '');
    video.setAttribute('webkit-playsinline', '');

    var p;
    try {
      p = video.play();
    } catch (e) {
      p = null;
    }

    if (p && typeof p.then === 'function') {
      p.catch(function () {
        // Fall back to the first user interaction.
        var once = { once: true, passive: true };
        var handler = function () {
          attemptPlay(video);
        };
        document.addEventListener('pointerdown', handler, once);
        document.addEventListener('touchstart', handler, once);
        document.addEventListener('click', handler, once);
      });
    }
  }

  function init() {
    attemptPlay(document.getElementById('backgroundVideo'));
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // WebKit sometimes needs another kick after page show/bfcache restore.
  window.addEventListener('pageshow', function () {
    init();
  });
})();
