import re

path = r'c:\Users\Rettung\.gemini\antigravity\scratch\pixellight-preview\index.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Inject HTML for modal before </body>
modal_html = """
<!-- VIDEO MODAL -->
<div class="video-modal" id="videoModal" aria-hidden="true">
  <div class="video-modal-backdrop" id="videoModalClose"></div>
  <div class="video-modal-content">
    <button class="video-modal-close-btn" id="videoModalCloseBtn">✕</button>
    <video id="modalVideoPlayer" controls playsinline></video>
  </div>
</div>
"""
text = text.replace('</body>', modal_html + '\n</body>')

# 2. Inject CSS before </style>
modal_css = """
  /* VIDEO MODAL */
  .video-modal {
    position: fixed;
    inset: 0;
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.4s ease;
  }
  .video-modal.open {
    opacity: 1;
    pointer-events: auto;
  }
  .video-modal-backdrop {
    position: absolute;
    inset: 0;
    background: rgba(8, 6, 8, 0.9);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    cursor: pointer;
  }
  .video-modal-content {
    position: relative;
    width: 90%;
    max-width: 1200px;
    border-radius: 12px;
    overflow: hidden;
    background: #000;
    box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    transform: scale(0.95);
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .video-modal.open .video-modal-content {
    transform: scale(1);
  }
  .video-modal-content video {
    width: 100%;
    height: auto;
    max-height: 85vh;
    display: block;
    outline: none;
  }
  .video-modal-close-btn {
    position: absolute;
    top: 20px;
    right: 20px;
    z-index: 10;
    background: rgba(0,0,0,0.5);
    border: 1px solid rgba(255,255,255,0.2);
    color: #fff;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 18px;
    backdrop-filter: blur(4px);
    transition: background 0.3s, transform 0.3s;
  }
  .video-modal-close-btn:hover {
    background: var(--signal);
    transform: scale(1.1);
  }
"""
text = text.replace('</style>', modal_css + '\n</style>')

# 3. Inject JS before </script>
modal_js = """
/* ============== VIDEO MODAL ============== */
(function initVideoModal() {
  const modal = document.getElementById('videoModal');
  const backdrop = document.getElementById('videoModalClose');
  const closeBtn = document.getElementById('videoModalCloseBtn');
  const player = document.getElementById('modalVideoPlayer');
  
  if(!modal || !player) return;

  function closeModal() {
    modal.classList.remove('open');
    modal.setAttribute('aria-hidden', 'true');
    setTimeout(() => {
      player.pause();
      player.removeAttribute('src');
      player.load();
    }, 400); // wait for fade out
  }

  backdrop.addEventListener('click', closeModal);
  closeBtn.addEventListener('click', closeModal);
  
  document.addEventListener('keydown', (e) => {
    if(e.key === 'Escape' && modal.classList.contains('open')) {
      closeModal();
    }
  });

  const cards = document.querySelectorAll('.work-card:not(.work-card--soon)');
  cards.forEach(card => {
    card.addEventListener('click', (e) => {
      e.preventDefault();
      const video = card.querySelector('video source');
      if (video) {
        player.src = video.src;
        modal.classList.add('open');
        modal.setAttribute('aria-hidden', 'false');
        player.play().catch(err => console.warn('Autoplay prevented:', err));
      }
    });
  });
})();
"""
text = text.replace('</script>\n</body>', modal_js + '\n</script>\n</body>')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Injected video modal successfully!")
