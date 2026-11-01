// Usage : node jeu/test-clavier.js "$PWD/jeu/index.html" <dossier des captures> [1280,390]
// Joue chaque niveau au clavier (déplacements et sauts réels). L'état n'est que lu, jamais modifié.
const {chromium}=require('playwright');
const FICHIER=process.argv[2], DOSSIER=process.argv[3], LARGEURS=(process.argv[4]||'1280,390').split(',').map(Number);
const dormir=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{
 const b=await chromium.launch(); const errs=[]; const bilan=[];
 for (const w of LARGEURS) {
  const ctx=await b.newContext({viewport:{width:w,height:w>600?900:844}});
  const p=await ctx.newPage();
  p.on('pageerror',e=>errs.push(w+': '+e.message)); p.on('console',m=>{if(m.type()==='error')errs.push(w+': '+m.text())});
  await p.goto('file://'+FICHIER); await p.waitForTimeout(500);
  const pos=()=>p.evaluate(()=>{const j=__jeu.etat.joueur; return {x:j.x,y:j.y,sol:j.sol,vy:j.vy};});
  const etat=()=>p.evaluate(()=>({pages:__jeu.etat.pages,resolus:__jeu.etat.resolus.size,fin:__jeu.etat.fin,t:__jeu.etat.t}));
  async function go(x){
    for(let k=0;k<400;k++){
      const s=await pos(); const d=x-s.x;
      if(Math.abs(d)<9){ break; }
      const key=d>0?'ArrowRight':'ArrowLeft', autre=d>0?'ArrowLeft':'ArrowRight';
      await p.keyboard.up(autre); await p.keyboard.down(key);
      await dormir(Math.min(60,Math.abs(d)/280*1000*0.5+8));
      await p.keyboard.up(key);
    }
    await p.keyboard.up('ArrowRight'); await p.keyboard.up('ArrowLeft');
    for(let k=0;k<40;k++){ const s=await pos(); if(s.sol) break; await dormir(25); }
  }
  async function hop(dir,stopX){
    const key=dir>0?'ArrowRight':'ArrowLeft';
    await p.keyboard.down(key); await p.keyboard.press('Space');
    let lache=false; await dormir(60);
    for(let k=0;k<120;k++){
      const s=await pos();
      if(!lache && (dir>0 ? s.x>=stopX : s.x<=stopX)){ await p.keyboard.up(key); lache=true; }
      if(s.sol && k>2) break;
      await dormir(15);
    }
    await p.keyboard.up(key);
  }
  async function E(){ await p.keyboard.press('KeyE'); await dormir(180); }
  async function attendreFin(){ for(let k=0;k<60;k++){ if(!(await p.isHidden('#ecran-verdict'))) break; await dormir(100);} return (await p.textContent('#verdict h2')); }
  async function entrer(n){ await p.click('.cas >> nth='+n); await p.click('#b-commencer'); await dormir(200); }
  async function verifier(nom, attendu){ const e=await etat(); if(e.resolus!==attendu) throw new Error(nom+' '+JSON.stringify(await pos())+': '+e.resolus+' verrous au lieu de '+attendu+' ('+await p.textContent('#b-texte')+')'); }

  await p.click('#b-ouvrir');
  // Niveau 1 : l'escalier, avec une erreur volontaire.
  await entrer(0);
  await go(500); await E(); await go(1600); await E(); await verifier('L1 art123',1);
  // escalier
  await go(655); for(const s of [730,810,890,970,1050,1130]) await hop(1,s);
  await go(1240); await E();
  await go(1745); await E(); await verifier('L1 dol',2);
  // erreur volontaire : l'art. 144 sur la marche 2 au rez-de-chaussée vide → on le porte à l'étage de l'illicéité
  await go(655); await hop(1,730); await hop(1,810); await go(870); await E();
  await go(1380); await hop(1,1450); await hop(1,1545); await go(1680); await E();
  const e1=await etat(); bilan.push(w+' erreur volontaire → pages '+e1.pages+' : '+(await p.textContent('#b-texte')).slice(0,70));
  await go(1560); await E(); // on pose l'objet par terre, sur l'étage
  await go(240); await E(); await go(1380); await hop(1,1450); await hop(1,1545); await go(1680); await E(); await verifier('L1 ill',3);
  await go(1100); await E(); await go(1380); await hop(1,1450); await hop(1,1545); await hop(-1,1460); await hop(1,1545); await go(1680); await E(); await verifier('L1 cul',4);
  await go(2100); bilan.push(w+' niveau 1 : '+await attendreFin());
  if(w===1280) await p.screenshot({path:DOSSIER+'/v-l1.png'});
  await p.click('#b-sommaire');

  // Niveau 2
  await entrer(1);
  await go(440); await E(); await go(1545); await E();
  await go(480); await hop(1,560); await hop(1,680); await go(690); await E(); await go(1185); await E();
  await go(720); await hop(1,790); await go(800); await E(); await go(1365); await E();
  await go(980); await E(); await go(1725); await E(); await verifier('L2',4);
  await go(1955); bilan.push(w+' niveau 2 : '+await attendreFin()); await p.click('#b-sommaire');

  // Niveau 3
  await entrer(2);
  await go(330); await E(); await go(1390); await E();
  await go(640); await E(); await go(1600); await E();
  await go(920); await E(); await go(1810); await E();
  await go(1170); await E(); await go(1390); await E(); await verifier('L3',4);
  await go(2065); bilan.push(w+' niveau 3 : '+await attendreFin());
  if(w===390) await p.screenshot({path:DOSSIER+'/t-l3.png'});
  await p.click('#b-sommaire');

  // Niveau 4
  await entrer(3);
  await go(330); await E(); await go(1540); await E();
  await go(480); await hop(1,560); await go(570); await E(); await go(1680); await E();
  await go(480); await hop(1,560); await hop(1,700); await go(720); await E(); await go(1820); await E();
  await go(1000); await hop(1,1080); await go(1090); await E(); await go(1960); await E();
  await go(1000); await hop(1,1080); await hop(1,1230); await go(1250); await E(); await go(2100); await E(); await verifier('L4',5);
  await go(2265); bilan.push(w+' niveau 4 : '+await attendreFin()); await p.click('#b-sommaire');

  // Niveau 5
  await entrer(4);
  await go(1600); await hop(1,1680); await go(1690); await E(); await go(350); await E();
  await go(760); await E(); await go(350); await E();
  await go(2100); await E(); await go(690); await E();
  await go(560); await E(); await go(690); await E(); await verifier('L5',4);
  await go(2205); bilan.push(w+' niveau 5 : '+await attendreFin()); await p.click('#b-sommaire');

  // Niveau 6
  await entrer(5);
  await go(160); await E(); await go(480);
  for(let k=0;k<80;k++){ const l=await p.evaluate(()=>{const t=__jeu.etat.t%3.6; return t>2.35&&t<3.2;}); if(l) break; await dormir(50); }
  await E(); await verifier('L6 yasmine',1);
  await go(860); await E(); await go(1210); await E();
  await go(1420); await E(); await go(1570); await E();
  await go(1700); await E(); await go(1760); await hop(1,1830); await hop(1,1900); await hop(-1,1840); await hop(1,1900); await go(2020); await E(); await verifier('L6',4);
  await go(2355); bilan.push(w+' niveau 6 : '+await attendreFin());
  if(w===1280) await p.screenshot({path:DOSSIER+'/v-l6.png'});
  await p.click('#b-sommaire');

  // Dernière page
  await entrer(6);
  for(let q=0;q<6;q++){
    const cible=await p.evaluate(()=>__jeu.etat.chutes.find(c=>c.ok).x);
    await go(cible);
    for(let k=0;k<200;k++){ const qq=await p.evaluate(()=>__jeu.etat.q); if(qq>q||await p.evaluate(()=>__jeu.etat.fin)) break; await dormir(60); }
    await dormir(1000);
  }
  bilan.push(w+' dernière page : '+await attendreFin()+' · XP '+await p.textContent('#xp')+' · '+await p.textContent('#grade'));
  bilan.push(w+' défilement horizontal : '+await p.evaluate(()=>document.documentElement.scrollWidth));
  await ctx.close();
 }
 // Temps écoulé : horloge accélérée.
 const ctx=await b.newContext({viewport:{width:1280,height:900}}); const p=await ctx.newPage();
 p.on('pageerror',e=>errs.push('horloge: '+e.message));
 await p.clock.install(); await p.goto('file://'+FICHIER);
 await p.clock.runFor(500);
 await p.click('#b-ouvrir'); await p.click('.cas >> nth=0'); await p.click('#b-commencer');
 for(let k=0;k<45;k++) await p.clock.runFor(5000);
 await p.clock.runFor(1000);
 bilan.push('temps écoulé : '+(await p.isVisible('#ecran-verdict'))+' · '+await p.textContent('#verdict h2'));
 await p.click('#b-rejouer'); await p.clock.runFor(200);
 bilan.push('recommencer : '+await p.evaluate(()=>({pages:__jeu.etat.pages,t:__jeu.etat.t,resolus:__jeu.etat.resolus.size})).then(JSON.stringify));
 await ctx.close();
 console.log(bilan.join('\n')); console.log('erreurs', errs); await b.close();
})().catch(e=>{console.error('ÉCHEC', e.message); process.exit(1);});
