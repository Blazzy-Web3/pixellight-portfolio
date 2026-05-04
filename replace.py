import re

path = r'c:\Users\Rettung\.gemini\antigravity\scratch\pixellight-preview\index.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Replace the Accordion HTML
old_acc = """  <div class="arsenal-accordion">
    <article class="acc-panel" data-skill="web" style="--accent:#ff3d1f">
      <div class="acc-panel-bg"></div>
      <div class="acc-panel-inner">
        <div class="acc-num">01 / SKILL</div>
        <div class="acc-title">Web Development</div>
        <div class="acc-content">
          <p>Modernste Tech-Stacks und cinema-grade Frontends. React, Three.js, Next.js — performant gebaut, eigensinnig gestaltet.</p>
          <div class="acc-tags"><span>React</span><span>Next.js</span><span>Three.js</span><span>GSAP</span></div>
          <button class="acc-btn magnetic" data-drawer="web">Explore Stack</button>
        </div>
      </div>
      <div class="acc-artifact" data-kind="codeCube"></div>
    </article>
 
    <article class="acc-panel" data-skill="branding" style="--accent:#ff5a2a">
      <div class="acc-panel-bg"></div>
      <div class="acc-panel-inner">
        <div class="acc-num">02 / SKILL</div>
        <div class="acc-title">Branding</div>
        <div class="acc-content">
          <p>Identität als System. Voice, Direction, Visual Language — von der ersten Skizze bis zum konsistenten Brand-Kosmos.</p>
          <div class="acc-tags"><span>Identity</span><span>Strategy</span><span>Voice</span></div>
          <button class="acc-btn magnetic" data-drawer="branding">Explore Stack</button>
        </div>
      </div>
      <div class="acc-artifact" data-kind="monolith"></div>
    </article>
 
    <article class="acc-panel" data-skill="interaction" style="--accent:#ff3d1f">
      <div class="acc-panel-bg"></div>
      <div class="acc-panel-inner">
        <div class="acc-num">03 / SKILL</div>
        <div class="acc-title">Interaction</div>
        <div class="acc-content">
          <p>Mikrobewegungen mit Bedeutung. Feedback-Loops, Hover-Mechanik, Choreografie — das Detail das Premium von Standard trennt.</p>
          <div class="acc-tags"><span>Micro-motion</span><span>Feedback</span><span>UX</span></div>
          <button class="acc-btn magnetic" data-drawer="interaction">Explore Stack</button>
        </div>
      </div>
      <div class="acc-artifact" data-kind="wireSphere"></div>
    </article>
 
    <article class="acc-panel" data-skill="3d" style="--accent:#ff7a3a">
      <div class="acc-panel-bg"></div>
      <div class="acc-panel-inner">
        <div class="acc-num">04 / SKILL</div>
        <div class="acc-title">3D Experience</div>
        <div class="acc-content">
          <p>WebGL als Erzählmedium. Custom Shader, Spatial Design, Physics — Räume die man durchschreitet statt durchklickt.</p>
          <div class="acc-tags"><span>WebGL</span><span>GLSL</span><span>R3F</span><span>Blender</span></div>
          <button class="acc-btn magnetic" data-drawer="3d">Explore Stack</button>
        </div>
      </div>
      <div class="acc-artifact" data-kind="torus"></div>
    </article>
 
    <article class="acc-panel" data-skill="motion" style="--accent:#ff3d1f">
      <div class="acc-panel-bg"></div>
      <div class="acc-panel-inner">
        <div class="acc-num">05 / SKILL</div>
        <div class="acc-title">Motion Design</div>
        <div class="acc-content">
          <p>Timing als Sprache. GSAP, Lenis, FLIP — jede Bewegung mit Anlauf, Mitte, Ausklang. Choreografie statt Animation.</p>
          <div class="acc-tags"><span>GSAP</span><span>Lenis</span><span>FLIP</span></div>
          <button class="acc-btn magnetic" data-drawer="motion">Explore Stack</button>
        </div>
      </div>
      <div class="acc-artifact" data-kind="wave"></div>
    </article>
 
    <article class="acc-panel" data-skill="creative" style="--accent:#ff5a2a">
      <div class="acc-panel-bg"></div>
      <div class="acc-panel-inner">
        <div class="acc-num">06 / SKILL</div>
        <div class="acc-title">Creative Code</div>
        <div class="acc-content">
          <p>Generative Systeme, custom Tools, handgeschriebene Shader. Kein Template-Vibe — jedes Projekt bekommt sein eigenes Vokabular.</p>
          <div class="acc-tags"><span>Generative</span><span>Custom</span><span>Shaders</span></div>
          <button class="acc-btn magnetic" data-drawer="creative">Explore Stack</button>
        </div>
      </div>
      <div class="acc-artifact" data-kind="helix"></div>
    </article>
  </div>"""

new_acc = """  <div class="arsenal-accordion">
    <article class="acc-panel" data-skill="web" style="--accent:#ff3d1f">
      <div class="acc-panel-bg"></div>
      <div class="acc-panel-inner">
        <div class="acc-num">01 / SKILL</div>
        <div class="acc-title">Web Development</div>
        <div class="acc-content">
          <p>Modernste Tech-Stacks und cinema-grade Frontends. React, Three.js, Next.js — performant gebaut, eigensinnig gestaltet.</p>
          <div class="acc-tags"><span>React</span><span>Next.js</span><span>Three.js</span><span>GSAP</span></div>
          <button class="acc-btn magnetic" data-drawer="web">Explore Stack</button>
        </div>
      </div>
      <div class="acc-artifact" data-kind="codeCube"></div>
    </article>

    <article class="acc-panel" data-skill="webdesign" style="--accent:#ff5a2a">
      <div class="acc-panel-bg"></div>
      <div class="acc-panel-inner">
        <div class="acc-num">02 / SKILL</div>
        <div class="acc-title">Web Design</div>
        <div class="acc-content">
          <p>Design das funktioniert und konvertiert. Ästhetik vereint mit psychologischer Nutzerführung für digitale Exzellenz.</p>
          <div class="acc-tags"><span>Figma</span><span>UI/UX</span><span>Prototyping</span></div>
          <button class="acc-btn magnetic" data-drawer="webdesign">Explore Stack</button>
        </div>
      </div>
      <div class="acc-artifact" data-kind="monolith"></div>
    </article>

    <article class="acc-panel" data-skill="seo" style="--accent:#ff7a3a">
      <div class="acc-panel-bg"></div>
      <div class="acc-panel-inner">
        <div class="acc-num">03 / SKILL</div>
        <div class="acc-title">Google SEO</div>
        <div class="acc-content">
          <p>Sichtbarkeit ist kein Zufall. Technische Perfektion und datengetriebene Content-Strategien für echte Rankings.</p>
          <div class="acc-tags"><span>Technical</span><span>Content</span><span>Analytics</span></div>
          <button class="acc-btn magnetic" data-drawer="seo">Explore Stack</button>
        </div>
      </div>
      <div class="acc-artifact" data-kind="wireSphere"></div>
    </article>

    <article class="acc-panel" data-skill="content" style="--accent:#ff3d1f">
      <div class="acc-panel-bg"></div>
      <div class="acc-panel-inner">
        <div class="acc-num">04 / SKILL</div>
        <div class="acc-title">Content Production</div>
        <div class="acc-content">
          <p>Visuelles Storytelling. Hochwertige Fotografie und Content-Produktion, die die Essenz der Marke einfängt.</p>
          <div class="acc-tags"><span>Photography</span><span>Direction</span><span>Lightroom</span></div>
          <button class="acc-btn magnetic" data-drawer="content">Explore Stack</button>
        </div>
      </div>
      <div class="acc-artifact" data-kind="torus"></div>
    </article>

    <article class="acc-panel" data-skill="email" style="--accent:#ff5a2a">
      <div class="acc-panel-bg"></div>
      <div class="acc-panel-inner">
        <div class="acc-num">05 / SKILL</div>
        <div class="acc-title">Email Marketing</div>
        <div class="acc-content">
          <p>Automatisierte Sales-Funnel und Newsletter, die gelesen werden. Direkt, personalisiert und conversion-optimiert.</p>
          <div class="acc-tags"><span>Automation</span><span>Copywriting</span><span>Funnels</span></div>
          <button class="acc-btn magnetic" data-drawer="email">Explore Stack</button>
        </div>
      </div>
      <div class="acc-artifact" data-kind="wave"></div>
    </article>

    <article class="acc-panel" data-skill="branding" style="--accent:#ff7a3a">
      <div class="acc-panel-bg"></div>
      <div class="acc-panel-inner">
        <div class="acc-num">06 / SKILL</div>
        <div class="acc-title">Logo / Branding</div>
        <div class="acc-content">
          <p>Identität als System. Voice, Direction, Visual Language — von der ersten Skizze bis zum konsistenten Brand-Kosmos.</p>
          <div class="acc-tags"><span>Identity</span><span>Strategy</span><span>Voice</span></div>
          <button class="acc-btn magnetic" data-drawer="branding">Explore Stack</button>
        </div>
      </div>
      <div class="acc-artifact" data-kind="helix"></div>
    </article>

    <article class="acc-panel" data-skill="ki" style="--accent:#ff3d1f">
      <div class="acc-panel-bg"></div>
      <div class="acc-panel-inner">
        <div class="acc-num">07 / SKILL</div>
        <div class="acc-title">KI - Kurse - Integration</div>
        <div class="acc-content">
          <p>Die Zukunft der Automatisierung. Implementierung von KI-Workflows und maßgeschneiderte Trainings für Teams.</p>
          <div class="acc-tags"><span>Automation</span><span>Prompting</span><span>Workflows</span></div>
          <button class="acc-btn magnetic" data-drawer="ki">Explore Stack</button>
        </div>
      </div>
      <div class="acc-artifact" data-kind="codeCube"></div>
    </article>
  </div>"""

# 2. Replace Mobile Stack
old_mob = """  <div class="arsenal-mobile-stack" id="arsenalMobileStack">
    <div class="arsenal-skill-card" data-kind="codeCube" data-accent="#ff3d1f">
      <div class="skill-canvas"></div>
      <div class="skill-meta">
        <div class="skill-num">01 / SKILL</div>
        <div class="skill-name">Web Development</div>
      </div>
      <div class="skill-arrow"></div>
    </div>
    <div class="arsenal-skill-card" data-kind="monolith" data-accent="#ff5a2a">
      <div class="skill-canvas"></div>
      <div class="skill-meta">
        <div class="skill-num">02 / SKILL</div>
        <div class="skill-name">Branding</div>
      </div>
      <div class="skill-arrow"></div>
    </div>
    <div class="arsenal-skill-card" data-kind="wireSphere" data-accent="#ff3d1f">
      <div class="skill-canvas"></div>
      <div class="skill-meta">
        <div class="skill-num">03 / SKILL</div>
        <div class="skill-name">Interaction</div>
      </div>
      <div class="skill-arrow"></div>
    </div>
    <div class="arsenal-skill-card" data-kind="torus" data-accent="#ff7a3a">
      <div class="skill-canvas"></div>
      <div class="skill-meta">
        <div class="skill-num">04 / SKILL</div>
        <div class="skill-name">3D Experience</div>
      </div>
      <div class="skill-arrow"></div>
    </div>
    <div class="arsenal-skill-card" data-kind="wave" data-accent="#ff3d1f">
      <div class="skill-canvas"></div>
      <div class="skill-meta">
        <div class="skill-num">05 / SKILL</div>
        <div class="skill-name">Motion Design</div>
      </div>
      <div class="skill-arrow"></div>
    </div>
    <div class="arsenal-skill-card" data-kind="helix" data-accent="#ff5a2a">
      <div class="skill-canvas"></div>
      <div class="skill-meta">
        <div class="skill-num">06 / SKILL</div>
        <div class="skill-name">Creative Code</div>
      </div>
      <div class="skill-arrow"></div>
    </div>
  </div>"""

new_mob = """  <div class="arsenal-mobile-stack" id="arsenalMobileStack">
    <div class="arsenal-skill-card" data-kind="codeCube" data-accent="#ff3d1f">
      <div class="skill-canvas"></div>
      <div class="skill-meta">
        <div class="skill-num">01 / SKILL</div>
        <div class="skill-name">Web Development</div>
      </div>
      <div class="skill-arrow"></div>
    </div>
    <div class="arsenal-skill-card" data-kind="monolith" data-accent="#ff5a2a">
      <div class="skill-canvas"></div>
      <div class="skill-meta">
        <div class="skill-num">02 / SKILL</div>
        <div class="skill-name">Web Design</div>
      </div>
      <div class="skill-arrow"></div>
    </div>
    <div class="arsenal-skill-card" data-kind="wireSphere" data-accent="#ff7a3a">
      <div class="skill-canvas"></div>
      <div class="skill-meta">
        <div class="skill-num">03 / SKILL</div>
        <div class="skill-name">Google SEO</div>
      </div>
      <div class="skill-arrow"></div>
    </div>
    <div class="arsenal-skill-card" data-kind="torus" data-accent="#ff3d1f">
      <div class="skill-canvas"></div>
      <div class="skill-meta">
        <div class="skill-num">04 / SKILL</div>
        <div class="skill-name">Content Production</div>
      </div>
      <div class="skill-arrow"></div>
    </div>
    <div class="arsenal-skill-card" data-kind="wave" data-accent="#ff5a2a">
      <div class="skill-canvas"></div>
      <div class="skill-meta">
        <div class="skill-num">05 / SKILL</div>
        <div class="skill-name">Email Marketing</div>
      </div>
      <div class="skill-arrow"></div>
    </div>
    <div class="arsenal-skill-card" data-kind="helix" data-accent="#ff7a3a">
      <div class="skill-canvas"></div>
      <div class="skill-meta">
        <div class="skill-num">06 / SKILL</div>
        <div class="skill-name">Logo / Branding</div>
      </div>
      <div class="skill-arrow"></div>
    </div>
    <div class="arsenal-skill-card" data-kind="codeCube" data-accent="#ff3d1f">
      <div class="skill-canvas"></div>
      <div class="skill-meta">
        <div class="skill-num">07 / SKILL</div>
        <div class="skill-name">KI - Kurse - Integration</div>
      </div>
      <div class="skill-arrow"></div>
    </div>
  </div>"""

# 3. Replace JS Data
new_data = """    const skillData = {
      web: {
        num: '01 / SKILL', title: 'Web Development',
        tag: 'Modernste Tech-Stacks und cinema-grade Frontends. React, Three.js, Next.js — performant gebaut, eigensinnig gestaltet.',
        tools: ['React', 'Next.js', 'Three.js', 'GSAP', 'Lenis', 'TypeScript', 'Vite', 'Tailwind'],
        projects: [
          { name: 'Elbe-Hypnose', year: '2026' },
          { name: 'Passive Income Dashboard', year: '2026' },
          { name: 'Pixel Light Studio', year: '2026' },
        ],
      },
      webdesign: {
        num: '02 / SKILL', title: 'Web Design',
        tag: 'Design das funktioniert und konvertiert. Ästhetik vereint mit psychologischer Nutzerführung für digitale Exzellenz.',
        tools: ['Figma', 'UI/UX Design', 'Wireframing', 'Prototyping', 'Design Systems'],
        projects: [
          { name: 'Aetherium Interface', year: '2026' },
          { name: 'Pixel Light UI', year: '2026' },
        ],
      },
      seo: {
        num: '03 / SKILL', title: 'Google SEO',
        tag: 'Sichtbarkeit ist kein Zufall. Technische Perfektion und datengetriebene Content-Strategien für echte Rankings.',
        tools: ['Technical SEO', 'Keyword Research', 'On-Page', 'Off-Page', 'Analytics'],
        projects: [
          { name: 'Elbe-Hypnose Ranking', year: '2026' },
          { name: 'Local SEO Strategy', year: '2026' },
        ],
      },
      content: {
        num: '04 / SKILL', title: 'Fotoshooting / Content Production',
        tag: 'Visuelles Storytelling. Hochwertige Fotografie und Content-Produktion, die die Essenz der Marke einfängt.',
        tools: ['Photography', 'Lightroom', 'Premiere', 'Art Direction', 'Storyboarding'],
        projects: [
          { name: 'Brand Story Shoot', year: '2026' },
          { name: 'Studio Session', year: '2026' },
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
          { name: 'Shining Stars: Arena', year: '2026' },
        ],
      },
      ki: {
        num: '07 / SKILL', title: 'KI - Kurse - Integration',
        tag: 'Die Zukunft der Automatisierung. Implementierung von KI-Workflows und maßgeschneiderte Trainings für Teams.',
        tools: ['ChatGPT', 'Midjourney', 'Custom GPTs', 'Workflow Automation', 'Prompt Engineering'],
        projects: [
          { name: 'AI Workflow Integration', year: '2026' },
          { name: 'Prompt Masterclass', year: '2026' },
        ],
      },
    };"""

def flexible_replace(source, old_str, new_str):
    pattern = re.escape(old_str)
    pattern = re.sub(r'\\\s+', r'\\s+', pattern)
    return re.sub(pattern, new_str.replace('\\', '\\\\'), source)

text1 = flexible_replace(text, old_acc, new_acc)
if text1 == text: print('Acc not replaced')

text2 = flexible_replace(text1, old_mob, new_mob)
if text2 == text1: print('Mob not replaced')

pattern3 = r'const skillData = \{.*?\n    \};\n'
text3 = re.sub(pattern3, new_data + '\n', text2, flags=re.DOTALL)
if text3 == text2: print('Data not replaced')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text3)
print('Done!')
