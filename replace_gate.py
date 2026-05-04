import re

path = r'c:\Users\Rettung\.gemini\antigravity\scratch\pixellight-preview\index.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

old_logic = r'/\* ============== GATE — KINOREIFER GRAVITATIONS-VORTEX ==============\ \*/\n\(function gateScene\(\) \{.*?\n\}\)\(\);\n'

new_logic = """/* ============== GATE — KINOREIFER GRAVITATIONS-VORTEX ============== */
(function gateScene() {
  const canvas = document.getElementById('gate-canvas');
  const portal = document.getElementById('gatePortal');
  const gateSection = document.getElementById('gate');
  
  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
  renderer.setClearColor(0x000000, 0); // Transparent background
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 100);
  camera.position.z = 10;

  // Particle System
  const N = 5000;
  const positions = new Float32Array(N * 3);
  const colors = new Float32Array(N * 3);
  const params = [];

  const color1 = new THREE.Color(0xff3d1f); // brand red
  const color2 = new THREE.Color(0x111111); // dark core
  const color3 = new THREE.Color(0xffffff); // white sparks

  for(let i=0; i<N; i++) {
    const angle = Math.random() * Math.PI * 2;
    // Exponential distribution to cluster near center
    const r = Math.pow(Math.random(), 2.5) * 6 + 1.3; 
    positions[i*3] = Math.cos(angle) * r;
    positions[i*3+1] = Math.sin(angle) * r;
    positions[i*3+2] = (Math.random()-0.5) * 1.5;

    params.push({
      angle: angle,
      radius: r,
      speed: (0.002 + Math.random() * 0.01) * (10 / r), // inner orbits faster
      zSpeed: (Math.random()-0.5) * 0.015
    });

    let c = color1;
    if(r < 1.8) c = color3;
    else if(Math.random() > 0.8) c = color2;
    
    colors[i*3] = c.r;
    colors[i*3+1] = c.g;
    colors[i*3+2] = c.b;
  }

  const geometry = new THREE.BufferGeometry();
  geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

  const material = new THREE.PointsMaterial({
    size: 0.04,
    vertexColors: true,
    transparent: true,
    opacity: 0.8,
    blending: THREE.AdditiveBlending
  });

  const points = new THREE.Points(geometry, material);
  scene.add(points);

  // Black hole center
  const bhGeo = new THREE.SphereGeometry(1.2, 32, 32);
  const bhMat = new THREE.MeshBasicMaterial({ color: 0x030203 }); // slightly above black
  const blackHole = new THREE.Mesh(bhGeo, bhMat);
  scene.add(blackHole);

  // Shockwave ring
  const swGeo = new THREE.RingGeometry(1.2, 1.3, 64);
  const swMat = new THREE.MeshBasicMaterial({ color: 0xff3d1f, transparent: true, opacity: 0, side: THREE.DoubleSide });
  const shockwave = new THREE.Mesh(swGeo, swMat);
  scene.add(shockwave);

  function resize() {
    const r = canvas.getBoundingClientRect();
    renderer.setSize(r.width, r.height, false);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    camera.aspect = r.width / r.height;
    camera.updateProjectionMatrix();
  }
  resize(); onResize(resize);

  let isImploding = false;
  let t = 0;

  function triggerVortex() {
    if(isImploding) return;
    if (typeof SoundManager !== 'undefined') SoundManager.playVortex();
    isImploding = true;
    gateSection?.classList.add('vortex-active');
    const plus = document.querySelector('.gate-plus');
    if (plus) plus.style.opacity = '0';
    
    // Shockwave animation
    gsap.to(shockwave.scale, { x: 25, y: 25, duration: 1.8, ease: "power2.out" });
    gsap.to(swMat, { opacity: 0.7, duration: 0.2, yoyo: true, repeat: 1 });
    
    // Singularity collapse & expand
    gsap.to(blackHole.scale, { x: 0.01, y: 0.01, z: 0.01, duration: 0.5, ease: "power3.in", onComplete: () => {
        gsap.to(blackHole.scale, { x: 1, y: 1, z: 1, duration: 1.2, ease: "elastic.out(1, 0.5)" });
    }});

    setTimeout(() => {
      isImploding = false;
      gateSection?.classList.remove('vortex-active');
      if (plus) plus.style.opacity = '';
      shockwave.scale.set(1,1,1);
      swMat.opacity = 0;
    }, 2400);
  }
  
  let targetRotX = 0;
  let targetRotY = 0;
  canvas.addEventListener('mousemove', e => {
    const r = canvas.getBoundingClientRect();
    const nx = ((e.clientX - r.left) / r.width) * 2 - 1;
    const ny = -((e.clientY - r.top) / r.height) * 2 + 1;
    targetRotY = nx * 0.4; // Lensing rotation effect
    targetRotX = -ny * 0.4;
  });
  canvas.addEventListener('mouseleave', () => { targetRotX = 0; targetRotY = 0; });
  
  portal.addEventListener('click', triggerVortex);
  portal.addEventListener('keydown', e => {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); triggerVortex(); }
  });

  function draw() {
    const rec = animRegistry.get(canvas);
    if (rec && !rec.active) { requestAnimationFrame(draw); return; }
    
    t += 0.01;
    
    // Smooth camera/object tilt
    points.rotation.x += (targetRotX - points.rotation.x) * 0.05;
    points.rotation.y += (targetRotY - points.rotation.y) * 0.05;
    
    const pos = points.geometry.attributes.position.array;
    for(let i=0; i<N; i++) {
      let p = params[i];
      let spd = isImploding ? p.speed * 8 : p.speed;
      p.angle -= spd;
      
      let currentR = p.radius;
      if (isImploding) {
         // Pull particles inward during implosion
         currentR = Math.max(1.2, currentR - 0.2); 
      }
      
      pos[i*3] = Math.cos(p.angle) * currentR;
      pos[i*3+1] = Math.sin(p.angle) * currentR;
      
      // Undulate Z slightly
      pos[i*3+2] += p.zSpeed;
      if(Math.abs(pos[i*3+2]) > 1.5) p.zSpeed *= -1;
    }
    points.geometry.attributes.position.needsUpdate = true;
    
    renderer.render(scene, camera);
    requestAnimationFrame(draw);
  }

  registerAnim(canvas, draw);
  animObserver.observe(canvas);
  draw();

  // Step indicator
  const steps = document.querySelectorAll('.gate-step');
  let cur = 0;
  setInterval(() => {
    steps.forEach(s => s.classList.remove('active'));
    cur = (cur + 1) % steps.length;
    steps[cur].classList.add('active');
  }, 2800);
})();
"""

text = re.sub(old_logic, new_logic, text, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Done!")
