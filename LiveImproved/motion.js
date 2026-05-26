(() => {
  const stage = document.getElementById('stage');
  if (!stage) return;

  const style = document.createElement('style');
  style.textContent = `
    .scene {
      opacity: 0;
      transform: translateY(22px) scale(.985);
      filter: blur(8px);
      transition: opacity .7s cubic-bezier(.2,.8,.2,1), transform .7s cubic-bezier(.2,.8,.2,1), filter .7s cubic-bezier(.2,.8,.2,1);
      will-change: transform, opacity, filter;
    }
    .orb {
      display: none;
    }
    .orb:nth-of-type(1) { animation-duration: 18s; }
    .orb:nth-of-type(2) { animation-duration: 24s; animation-direction: alternate-reverse; }
    .cta {
      position: relative;
      overflow: hidden;
      isolation: isolate;
    }
    .cta .cta-label {
      position: relative;
      z-index: 1;
      display: inline-block;
    }
    .cta .cta-sheen {
      position: absolute;
      inset: -40% auto -40% -40%;
      width: 45%;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,.45), transparent);
      transform: skewX(-20deg) translateX(-140%);
      animation: sheen 4.8s ease-in-out infinite;
      z-index: 0;
      pointer-events: none;
      mix-blend-mode: screen;
    }
    .headline {
      text-wrap: balance;
      text-shadow: 0 10px 32px rgba(0,0,0,.24);
    }
    .subhead, .fine, .chip, .card, .mini, .metric-main, .ring, .chart, .coach-box, .formal-shell, .formal-grid, .formal-left, .formal-right, .formal-rail, .formal-card, .formal-meta {
      will-change: transform, opacity;
    }
    .scene::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(255,255,255,.04), transparent 24%, transparent 76%, rgba(0,0,0,.14));
      pointer-events: none;
      mix-blend-mode: soft-light;
    }
    @keyframes drift {
      from { transform: translate3d(-12px, -10px, 0) scale(1); }
      to { transform: translate3d(14px, 12px, 0) scale(1.04); }
    }
    @keyframes sheen {
      0%, 34% { transform: skewX(-20deg) translateX(-160%); opacity: 0; }
      48% { opacity: .75; }
      68% { transform: skewX(-20deg) translateX(280%); opacity: 0; }
      100% { transform: skewX(-20deg) translateX(280%); opacity: 0; }
    }
  `;
  document.head.appendChild(style);

  stage.querySelectorAll('.cta').forEach((cta) => {
    const label = cta.textContent.trim();
    cta.textContent = '';
    const span = document.createElement('span');
    span.className = 'cta-label';
    span.textContent = label;
    const sheen = document.createElement('span');
    sheen.className = 'cta-sheen';
    cta.appendChild(span);
    cta.appendChild(sheen);
  });

  const scenes = [...stage.querySelectorAll('.scene')];
  const items = [...stage.querySelectorAll('.headline, .subhead, .fine, .chip, .card, .mini, .metric-main, .ring, .chart, .coach-box, .status, .logo, .screen-head, .topbar, .overlay, .formal-shell, .formal-meta, .formal-grid, .formal-left, .formal-right, .formal-rail, .formal-card')];
  if (window.gsap) {
    gsap.set(scenes, { opacity: 0, y: 26, scale: 0.985, filter: 'blur(10px)' });
    gsap.set(items, { opacity: 0, y: 16 });
    const tl = gsap.timeline({ delay: 0.05 });
    scenes.forEach((scene, idx) => {
      const start = idx * 5;
      tl.to(scene, { opacity: 1, y: 0, scale: 1, filter: 'blur(0px)', duration: 0.7, ease: 'power3.out' }, start + 0.1);
      tl.fromTo(scene.querySelectorAll('.kicker, .headline, .subhead, .fine, .chip, .card, .mini, .metric-main, .ring, .chart, .coach-box, .status, .logo, .screen-head, .topbar, .overlay, .cta, .formal-card'),
        { opacity: 0, y: 18 },
        { opacity: 1, y: 0, stagger: 0.045, duration: 0.45, ease: 'power2.out' },
        start + 0.18
      );
    });
    gsap.to(stage.querySelectorAll('.orb'), { y: '+=16', x: '+=10', duration: 7, repeat: -1, yoyo: true, ease: 'sine.inOut', stagger: 0.35 });
    gsap.to(stage.querySelectorAll('.cta'), { scale: 1.015, duration: 1.7, repeat: -1, yoyo: true, ease: 'sine.inOut', stagger: 0.18 });
  } else {
    scenes.forEach((scene, idx) => {
      scene.style.opacity = idx === 0 ? 1 : 0.65;
      scene.style.filter = 'blur(0)';
      scene.style.transform = 'translateY(0) scale(1)';
    });
  }
})();
