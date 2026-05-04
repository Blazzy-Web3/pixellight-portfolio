import re

path = r'c:\Users\Rettung\.gemini\antigravity\scratch\pixellight-preview\index.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update skillData
new_skill_data = """    const skillData = {
      web: {
        num: '01 / SKILL', title: 'Web Development',
        tag: 'Modernste Tech-Stacks und cinema-grade Frontends. React, Three.js, Next.js — performant gebaut, eigensinnig gestaltet.',
        tools: ['React', 'Next.js', 'Three.js', 'GSAP', 'Lenis', 'TypeScript', 'Vite', 'Tailwind', 'HTML5 / CSS'],
        projects: [
          { name: 'Elbe-Hypnose', year: '2026' },
          { name: 'Aura Clean Service', year: '2026' },
          { name: 'Kolonaki Barbershop', year: '2026' },
        ],
      },
      webdesign: {
        num: '02 / SKILL', title: 'Web Design',
        tag: 'Design das funktioniert und konvertiert. Ästhetik vereint mit psychologischer Nutzerführung für digitale Exzellenz.',
        tools: ['Canva', 'UI/UX Design', 'Wireframing', 'Prototyping', 'Design Systems'],
        projects: [
          { name: 'Pixel Light UI', year: '2026' },
          { name: 'Therapiezentrum Frieda', year: '2026' },
        ],
      },
      seo: {
        num: '03 / SKILL', title: 'Google SEO',
        tag: 'Sichtbarkeit ist kein Zufall. Technische Perfektion und datengetriebene Content-Strategien für echte Rankings.',
        tools: ['Technical SEO', 'Keyword Research', 'On-Page', 'Off-Page', 'Analytics'],
        projects: [
          { name: 'Therapiezentrum Frieda', year: '2026' },
          { name: 'Pixellight.studio', year: '2026' },
          { name: 'Local SEO Strategy', year: '2026' },
          { name: 'SEO Ranking', year: '2026' },
        ],
      },
      content: {
        num: '04 / SKILL', title: 'Content Production',
        tag: 'Visuelles Storytelling. Hochwertige Fotografie und Content-Produktion, die die Essenz der Marke einfängt.',
        tools: ['Photography', 'Lightroom', 'Remotion', 'CapCut', 'Art Direction', 'Storyboarding'],
        projects: [
          { name: 'Ehemalig Mit den Jungz', year: '2026' },
          { name: 'Tiktok Teamjntsch', year: '2026' },
          { name: 'Black Cobra Fight Club', year: '2026' },
        ],
      },
      email: {
        num: '05 / SKILL', title: 'Email Marketing',
        tag: 'Automatisierte Sales-Funnel und Newsletter, die gelesen werden. Direkt, personalisiert und conversion-optimiert.',
        tools: ['Klaviyo', 'ActiveCampaign', 'Copywriting', 'A/B Testing', 'Automation'],
        projects: [
          { name: 'Launch Sequence', year: '2026' },
          { name: 'Nurture Funnel', year: '2026' },
        ],
      },
      branding: {
        num: '06 / SKILL', title: 'Logo / Branding',
        tag: 'Identität als System. Voice, Direction, Visual Language — von der ersten Skizze bis zum konsistenten Brand-Kosmos.',
        tools: ['Figma', 'Illustrator', 'Brand Strategy', 'Voice Design', 'Typography'],
        projects: [
          { name: 'Pixel Light Identity', year: '2026' },
          { name: 'NoWi Car Pool', year: '2026' },
        ],
      },
      ki: {
        num: '07 / SKILL', title: 'KI - Kurse - Integration',
        tag: 'Die Zukunft der Automatisierung. Implementierung von KI-Workflows und maßgeschneiderte Trainings für Teams.',
        tools: ['ChatGPT', 'Midjourney', 'Custom GPTs', 'Workflow Automation', 'Prompt Engineering', 'Claude', 'Gemini', 'Kimi', 'Higgsfield'],
        projects: [
          { name: 'AI Workflow Integration', year: '2026' },
          { name: 'Prompt Masterclass', year: '2026' },
          { name: 'How to use AI', year: '2026' },
        ],
      },
    };"""

text = re.sub(r'const skillData = \{.*?\n    \};\n', new_skill_data + '\n', text, flags=re.DOTALL)

# 2. Update data-kind in HTML
# Content Production -> prism
text = text.replace(
    '<div class="acc-artifact" data-kind="torus"></div>\n    </article>\n\n    <article class="acc-panel" data-skill="email"',
    '<div class="acc-artifact" data-kind="prism"></div>\n    </article>\n\n    <article class="acc-panel" data-skill="email"'
)
text = text.replace(
    '<div class="arsenal-skill-card" data-kind="torus" data-accent="#ff3d1f">\n      <div class="skill-canvas"></div>\n      <div class="skill-meta">\n        <div class="skill-num">04 / SKILL</div>\n        <div class="skill-name">Content Production</div>',
    '<div class="arsenal-skill-card" data-kind="prism" data-accent="#ff3d1f">\n      <div class="skill-canvas"></div>\n      <div class="skill-meta">\n        <div class="skill-num">04 / SKILL</div>\n        <div class="skill-name">Content Production</div>'
)

# KI Integration -> network
text = text.replace(
    '<div class="acc-artifact" data-kind="codeCube"></div>\n    </article>\n  </div>\n\n  <!-- Mobile-only card stack -->',
    '<div class="acc-artifact" data-kind="network"></div>\n    </article>\n  </div>\n\n  <!-- Mobile-only card stack -->'
)
text = text.replace(
    '<div class="arsenal-skill-card" data-kind="codeCube" data-accent="#ff3d1f">\n      <div class="skill-canvas"></div>\n      <div class="skill-meta">\n        <div class="skill-num">07 / SKILL</div>\n        <div class="skill-name">KI - Kurse - Integration</div>',
    '<div class="arsenal-skill-card" data-kind="network" data-accent="#ff3d1f">\n      <div class="skill-canvas"></div>\n      <div class="skill-meta">\n        <div class="skill-num">07 / SKILL</div>\n        <div class="skill-name">KI - Kurse - Integration</div>'
)

# 3. Add THREE.js logic
logic_to_insert = """      } else if (kind === 'prism') {
        const g = new THREE.OctahedronGeometry(0.7, 0);
        group.add(new THREE.Mesh(g, new THREE.MeshBasicMaterial({ color: accent, transparent: true, opacity: 0.8, wireframe: true })));
        const innerG = new THREE.OctahedronGeometry(0.35, 0);
        group.add(new THREE.Mesh(innerG, new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.9 })));
        baseSpinY = 0.015;
        baseSpinX = 0.008;
      } else if (kind === 'network') {
        const g = new THREE.IcosahedronGeometry(0.7, 1);
        const m = new THREE.PointsMaterial({ color: accent, size: 0.05 });
        group.add(new THREE.Points(g, m));
        const l = new THREE.LineSegments(new THREE.EdgesGeometry(g), new THREE.LineBasicMaterial({ color: accent, transparent: true, opacity: 0.3 }));
        group.add(l);
        baseSpinY = 0.01;
        baseSpinX = 0.01;
"""

# Insert into mobile section
text = text.replace(
    "} else if (kind === 'helix') {\n        const turns = 3,",
    logic_to_insert + "} else if (kind === 'helix') {\n        const turns = 3,"
)

# Insert into desktop section (it might be the same string)
# The above replace will replace BOTH instances if they are identical!
# Let's check how many times it was replaced.

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Done applying deep dive updates!")
