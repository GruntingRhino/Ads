(() => {
  const stage = document.getElementById('stage');
  if (!stage) return;

  const style = document.createElement('style');
  style.textContent = `
    .scene {
      padding: 28px 30px;
      box-sizing: border-box;
    }
    .scene-inner {
      position: relative;
      width: 100%;
      height: 100%;
      padding: 0;
      display: block;
    }
    .formal-shell {
      position: relative;
      height: 100%;
      border-radius: 28px;
      overflow: hidden;
      border: 1px solid rgba(255,255,255,.10);
      background:
        linear-gradient(180deg, rgba(255,255,255,.035), rgba(255,255,255,.018)),
        linear-gradient(180deg, rgba(7,11,16,.96), rgba(9,13,19,.99));
      box-shadow: 0 24px 64px rgba(0,0,0,.32);
    }
    .formal-shell::before {
      content: '';
      position: absolute;
      inset: 0;
      background:
        radial-gradient(circle at 12% 8%, rgba(95,124,255,.12), transparent 22%),
        radial-gradient(circle at 86% 18%, rgba(255,77,77,.08), transparent 18%),
        linear-gradient(180deg, rgba(255,255,255,.04), transparent 26%, transparent 74%, rgba(0,0,0,.10));
      pointer-events: none;
      mix-blend-mode: screen;
    }
    .formal-meta {
      position: relative;
      z-index: 1;
      display: grid;
      grid-template-columns: 1fr 1.4fr auto;
      gap: 16px;
      align-items: center;
      padding: 18px 24px;
      border-bottom: 1px solid rgba(255,255,255,.08);
      background: rgba(255,255,255,.025);
      text-transform: uppercase;
      letter-spacing: .18em;
      font-weight: 900;
      font-size: 12px;
      color: rgba(238,243,250,.72);
    }
    .formal-meta .brand {
      color: var(--text);
      letter-spacing: .22em;
    }
    .formal-meta .chapter {
      text-align: center;
      color: rgba(238,243,250,.62);
    }
    .formal-meta .timing {
      text-align: right;
      color: var(--success);
      letter-spacing: .14em;
    }
    .formal-grid {
      position: relative;
      z-index: 1;
      display: grid;
      grid-template-columns: minmax(0, 1.08fr) minmax(330px, .92fr);
      gap: 20px;
      height: calc(100% - 61px);
      padding: 22px;
      box-sizing: border-box;
    }
    .formal-left,
    .formal-right {
      min-width: 0;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .formal-left {
      justify-content: space-between;
    }
    .formal-right {
      border-radius: 24px;
      padding: 18px;
      border: 1px solid rgba(255,255,255,.12);
      background: rgba(10,14,20,.82);
      backdrop-filter: blur(12px);
      overflow: hidden;
    }
    .formal-rail {
      display: grid;
      gap: 12px;
      margin-bottom: 12px;
    }
    .formal-card {
      border-radius: 18px;
      padding: 16px 16px 15px;
      background: rgba(255,255,255,.05);
      border: 1px solid rgba(255,255,255,.10);
      border-left: 3px solid rgba(95,124,255,.86);
      box-shadow: inset 0 0 0 1px rgba(255,255,255,.02);
    }
    .formal-card .label {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: .2em;
      font-weight: 900;
      color: rgba(238,243,250,.56);
    }
    .formal-card .value {
      margin-top: 8px;
      font-size: 18px;
      line-height: 1.28;
      font-weight: 800;
      color: var(--text);
    }
    .formal-card .value strong {
      color: var(--success);
    }
    .formal-card .meta {
      margin-top: 10px;
      font-size: 13px;
      line-height: 1.4;
      color: rgba(238,243,250,.70);
      font-weight: 650;
    }
    .formal-note {
      margin-top: auto;
      padding-top: 10px;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: .18em;
      color: rgba(238,243,250,.42);
      font-weight: 900;
    }
    .formal-summary {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 10px;
      margin-top: 12px;
    }
    .summary-tile {
      border-radius: 16px;
      padding: 12px 12px 11px;
      background: rgba(255,255,255,.04);
      border: 1px solid rgba(255,255,255,.08);
    }
    .summary-tile .label {
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: .2em;
      color: rgba(238,243,250,.48);
      font-weight: 900;
    }
    .summary-tile .value {
      margin-top: 7px;
      font-size: 13px;
      line-height: 1.35;
      color: var(--text);
      font-weight: 700;
    }
    .formal-right .phone,
    .formal-right .chart,
    .formal-right .feed,
    .formal-right .coach-box,
    .formal-right .chip-row {
      margin-top: 0;
    }
    .formal-right .phone {
      flex: 1;
      min-height: 0;
    }
    .formal-right .phone-shell {
      width: 100%;
      height: 100%;
      min-height: 0;
      border-radius: 28px;
      box-sizing: border-box;
    }
    .formal-right .screen {
      padding: 22px;
      border-radius: 22px;
      box-sizing: border-box;
    }
    .formal-right .hero-metrics {
      grid-template-columns: 1.15fr .85fr;
    }
    .formal-right .metric-main .value {
      font-size: 68px;
    }
    .formal-right .feed {
      grid-template-columns: 1fr;
    }
    .formal-right .coach-box {
      border-radius: 18px;
    }
    .formal-right .chart,
    .formal-right .card,
    .formal-right .mini,
    .formal-right .metric-main,
    .formal-right .ring {
      border-radius: 18px;
    }
    .formal-right .mini-grid {
      grid-template-columns: repeat(3, 1fr);
    }
    .formal-right .chip-row {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
    .scene .headline {
      font-size: clamp(56px, 4.9vw, 82px);
      line-height: .92;
      max-width: 9.2ch;
      text-wrap: balance;
      letter-spacing: -.02em;
    }
    .scene .subhead {
      max-width: 44ch;
      font-size: 24px;
      line-height: 1.26;
    }
    .scene .cta {
      border-radius: 18px;
      padding: 16px 20px;
      font-size: 18px;
      letter-spacing: .08em;
      box-shadow: 0 18px 36px rgba(0,0,0,.26);
    }
    .scene .fine {
      max-width: 42ch;
    }
    .scene .topbar {
      padding: 2px 0 4px;
      border-bottom: 1px solid rgba(255,255,255,.08);
      margin-bottom: 6px;
    }
    .scene .logo {
      font-size: 18px;
    }
    .scene .status {
      padding: 10px 14px;
      font-size: 12px;
      border-radius: 999px;
    }
    @media (max-width: 960px) {
      .scene { padding: 18px; }
      .formal-grid { grid-template-columns: 1fr; height: calc(100% - 61px); }
      .formal-right { order: 2; }
      .formal-left { order: 1; }
      .scene .headline { max-width: none; }
      .scene .subhead { max-width: none; }
    }
  `;
  document.head.appendChild(style);

  const asText = (node) => (node?.textContent || '').replace(/\s+/g, ' ').trim();
  const sceneNodes = [...stage.querySelectorAll('.scene')];

  sceneNodes.forEach((scene, index) => {
    const inner = scene.querySelector('.scene-inner');
    if (!inner || inner.dataset.formalized === '1') return;
    inner.dataset.formalized = '1';

    const nodes = [...inner.children];
    const headline = inner.querySelector('.headline');
    const subhead = inner.querySelector('.subhead');
    const cta = inner.querySelector('.cta');
    const fine = inner.querySelector('.fine');
    const kicker = inner.querySelector('.kicker');
    const topbar = inner.querySelector('.topbar');
    const phone = inner.querySelector('.phone');
    const chart = inner.querySelector('.chart');
    const feed = inner.querySelector('.feed');
    const coachBoxes = [...inner.querySelectorAll('.coach-box')];
    const chips = inner.querySelector('.chip-row');
    const metrics = inner.querySelector('.hero-metrics');
    const status = inner.querySelector('.status');

    const shell = document.createElement('div');
    shell.className = 'formal-shell';

    const meta = document.createElement('div');
    meta.className = 'formal-meta';
    const label = (kicker && asText(kicker)) || (topbar && asText(topbar)) || 'LIVEIMPROVED';
    const chapter = (headline && asText(headline)) ? asText(headline).slice(0, 42) : scene.getAttribute('data-composition-id') || `SCENE ${String(index + 1).padStart(2, '0')}`;
    const timing = `${String(index + 1).padStart(2, '0')} / ${scene.getAttribute('data-start') || '0'}s`;
    meta.innerHTML = `<div class="brand">${label}</div><div class="chapter">${chapter}</div><div class="timing">${timing}</div>`;

    const grid = document.createElement('div');
    grid.className = 'formal-grid';
    const left = document.createElement('div');
    left.className = 'formal-left';
    const right = document.createElement('div');
    right.className = 'formal-right';

    const rail = document.createElement('div');
    rail.className = 'formal-rail';
    const cards = [
      {
        label: 'Signal',
        value: asText(headline) || chapter,
        meta: asText(subhead) || 'The problem is visible once it is measured.'
      },
      {
        label: 'Proof',
        value: asText(fine) || asText(chart) || 'Numbers replace vague motivation.',
        meta: asText(chips) || asText(metrics) || 'Concrete feedback beats self-talk.'
      },
      {
        label: 'Action',
        value: asText(cta) || 'Run the system.',
        meta: status ? asText(status) : 'One command. One standard.'
      }
    ];
    rail.innerHTML = cards.map((card) => `
      <article class="formal-card">
        <div class="label">${card.label}</div>
        <div class="value">${card.value}</div>
        <div class="meta">${card.meta}</div>
      </article>
    `).join('');

    const visualNodes = new Set([phone, chart, feed, chips, metrics, ...coachBoxes].filter(Boolean));

    nodes.forEach((node) => {
      if (!node.isConnected) return;
      if (node === topbar) return;
      if (visualNodes.has(node)) {
        right.appendChild(node);
      } else {
        left.appendChild(node);
      }
    });

    if (!right.childElementCount) right.appendChild(rail);
    else right.insertBefore(rail, right.firstChild);

    const summary = document.createElement('div');
    summary.className = 'formal-summary';
    summary.innerHTML = [
      { label: 'Hook', value: (asText(headline) || chapter).slice(0, 40) },
      { label: 'Proof', value: (asText(subhead) || asText(fine) || 'Concrete evidence.') .slice(0, 40) },
      { label: 'CTA', value: (asText(cta) || 'Run the system.').slice(0, 40) },
    ].map((item) => `<div class="summary-tile"><div class="label">${item.label}</div><div class="value">${item.value}</div></div>`).join('');

    const note = document.createElement('div');
    note.className = 'formal-note';
    note.textContent = scene.getAttribute('data-composition-id') || `LIVEIMPROVED / ${String(index + 1).padStart(2, '0')}`;
    right.appendChild(summary);
    right.appendChild(note);

    grid.append(left, right);
    shell.append(meta, grid);
    inner.replaceChildren(shell);
  });
})();
