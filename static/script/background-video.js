// Safari (especially on macOS) can be strict about autoplay.
// We keep the video muted + playsinline and attempt to start it
// after a few lifecycle events. If it still fails, we start it on
// the first user gesture.

(function () {
  var boundGesture = false;

  function configure(video) {
    if (!video) return;

    // Make autoplay eligibility as explicit as possible for WebKit.
    video.muted = true;
    video.defaultMuted = true;
    video.volume = 0;
    video.autoplay = true;
    video.loop = true;
    video.playsInline = true;

    video.setAttribute('muted', '');
    video.setAttribute('autoplay', '');
    video.setAttribute('loop', '');
    video.setAttribute('playsinline', '');
    video.setAttribute('webkit-playsinline', '');
    video.setAttribute('disablepictureinpicture', '');
  }

  function bindGestureFallback(video) {
    if (boundGesture) return;
    boundGesture = true;

    var once = { once: true, passive: true };
    var handler = function () {
      attemptPlay(video);
    };

    document.addEventListener('pointerdown', handler, once);
    document.addEventListener('touchstart', handler, once);
    document.addEventListener('click', handler, once);
    document.addEventListener('keydown', handler, once);
  }

  function attemptPlay(video) {
    if (!video) return;

    configure(video);

    var p;
    try {
      p = video.play();
    } catch (e) {
      p = null;
    }

    if (p && typeof p.then === 'function') {
      p.catch(function () {
        bindGestureFallback(video);
      });
    }
  }

  function init() {
    var video = document.getElementById('backgroundVideo');
    if (!video) return;

    configure(video);

    // Kick playback across a few lifecycle moments; WebKit can be finicky.
    if (typeof requestAnimationFrame === 'function') {
      requestAnimationFrame(function () {
        attemptPlay(video);
      });
    } else {
      attemptPlay(video);
    }

    setTimeout(function () {
      if (video.paused) attemptPlay(video);
    }, 300);

    video.addEventListener(
      'loadedmetadata',
      function () {
        if (video.paused) attemptPlay(video);
      },
      { once: true }
    );

    video.addEventListener(
      'canplay',
      function () {
        if (video.paused) attemptPlay(video);
      },
      { once: true }
    );

    document.addEventListener('visibilitychange', function () {
      if (!document.hidden && video.paused) attemptPlay(video);
    });
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
