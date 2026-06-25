// ─── STATE ───
let PROYECTO_ACTUAL = localStorage.getItem('soma_proyecto_id') || null;
let DATOS_PROYECTO = null;
const KANBAN_CYCLE = ['PENDIENTE','EN_PROGRESO','LISTO','APROBADO','NO_APLICA'];
const KANBAN_CLASS = ['s-pendiente','s-progreso','s-listo','s-aprobado','s-noaplica'];
const KANBAN_SYMBOL = ['●','●','●','●','○'];
let DB_PROGRESO = {};

function esc(s){return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;')}

function lsKey(s){ return 'soma_kanban_'+(PROYECTO_ACTUAL||'0')+'_'+s; }

// ─── SECTION NAV ───
function showSection(n){
  document.querySelectorAll('.detail-section').forEach(s=>s.classList.remove('active'));
  document.querySelectorAll('.station').forEach(s=>s.classList.remove('active'));
  const sec=document.getElementById('sec-'+n);
  if(sec){sec.classList.add('active')}
  const st=document.querySelectorAll('.station')[n-1];
  if(st){st.classList.add('active')}
  const tl=document.getElementById('timeline');
  if(tl)tl.querySelectorAll('.station')[n-1].scrollIntoView({behavior:'smooth',inline:'center',block:'nearest'});
  window.location.hash='sec-'+n;
  if(n===1) renderContactoReal();
  if(n===2) renderImmersionReal();
  if(n===3) { renderProgramaReal(); }
  if(n===10) renderKanbanDashboard();
}

function toggle(el){
  const expanded=el.classList.toggle('expanded');
  const d=el.querySelector('.step-detail');
  if(d){ d.classList.toggle('open'); d.setAttribute('aria-hidden',!expanded); }
  el.setAttribute('aria-expanded',expanded);
}

function toggleInv(el){
  el.classList.toggle('open');
  const a=el.querySelector('.arrow');
  if(a)a.textContent=el.classList.contains('open')?'▼':'▶';
}

function toggleSubgroup(el){
  el.classList.toggle('open');
  const a=el.querySelector('.arrow');
  if(a)a.textContent=el.classList.contains('open')?'▼':'▶';
}

document.addEventListener('keydown',function(e){
  if(e.key==='Enter'||e.key===' '){
    const t=e.target.closest('.step-card,.station,.node');
    if(t&&typeof t.click==='function'){e.preventDefault();t.click()}
  }
});

// ─── API HELPERS ───
async function apiGet(url){
  try{ const r=await fetch(url); return await r.json(); }catch(e){ return null; }
}
async function apiPut(url, data){
  try{ await fetch(url,{method:'PUT',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)}); }catch(e){}
}

// ─── CARGAR DATOS DEL PROYECTO ───
async function cargarDatosProyecto(proyectoId){
  PROYECTO_ACTUAL = proyectoId;
  localStorage.setItem('soma_proyecto_id', proyectoId);
  DATOS_PROYECTO = await apiGet(`/api/algoritmo/datos/${proyectoId}`);
  if(DATOS_PROYECTO){
    await cargarProgreso();
    const active = document.querySelector('.detail-section.active');
    if(active){
      const id = active.id;
      if(id==='sec-1') renderContactoReal();
      else if(id==='sec-2') renderImmersionReal();
      else if(id==='sec-3') { renderProgramaReal(); if(document.getElementById('diagrama-section')?.classList.contains('visible')){ renderProgramaRelaciones(); renderDiagramaRelaciones(proyectoId); } }
      else if(id==='sec-10') renderKanbanDashboard();
    }
  }
}

// ─── KANBAN — DB + LOCALSTORAGE POR PROYECTO ───
async function cargarProgreso(){
  if(!PROYECTO_ACTUAL) return;
  const res = await apiGet(`/api/algoritmo/progreso/${PROYECTO_ACTUAL}`);
  DB_PROGRESO = (res && res.progreso) || {};
  actualizarTodosBullets();
  actualizarProgresoTarjeta();
}

async function guardarProgreso(seccion, paso, estado){
  if(!PROYECTO_ACTUAL) return;
  await apiPut(`/api/algoritmo/progreso/${PROYECTO_ACTUAL}`, { seccion, paso, estado });
  DB_PROGRESO[seccion+'_'+paso] = estado;
  actualizarProgresoTarjeta();
  if(document.getElementById('sec-10')?.classList.contains('active')) renderKanbanDashboard();
}

function totalStepsInSection(s){
  const sec = document.getElementById('sec-'+s);
  if(!sec) return 0;
  if(s===2) return sec.querySelectorAll('.inv-card.var .inv-item').length;
  return sec.querySelectorAll('.step-card').length;
}

function varItemsInSection(s){
  const sec = document.getElementById('sec-'+s);
  if(!sec) return [];
  if(s===2) return [...sec.querySelectorAll('.inv-card.var .inv-item')];
  return [...sec.querySelectorAll('.step-card')];
}

function calcularProgresoGlobal(){
  if(!PROYECTO_ACTUAL) return 0;
  let total = 0, completados = 0;
  for(let s=1;s<=9;s++){
    const items = varItemsInSection(s);
    items.forEach(item => {
      const step = (s===2)
        ? (item.querySelector('h4')||{}).textContent?.match(/([\d.]+)/)?.[1]||s+'.1'
        : item.dataset.step||s+'.1';
      const st = DB_PROGRESO[s+'_'+step] || 'PENDIENTE';
      if(st==='NO_APLICA') return;
      total++;
      if(st==='APROBADO'||st==='LISTO') completados++;
    });
  }
  return total ? Math.round((completados/total)*100) : 0;
}

function actualizarProgresoTarjeta(){
  const pct = calcularProgresoGlobal();
  const fill = document.getElementById('prog-fill-'+PROYECTO_ACTUAL);
  const label = document.getElementById('prog-pct-'+PROYECTO_ACTUAL);
  if(fill) fill.style.width = pct+'%';
  if(label) label.textContent = pct+'%';
}

function actualizarTodosBullets(){
  for(let s=1;s<=9;s++){
    const section = document.getElementById('sec-'+s);
    if(!section) continue;
    const selector = (s===2) ? '.inv-card.var .inv-item' : '.step-card';
    section.querySelectorAll(selector).forEach(item => {
      const step = (s===2)
        ? (item.querySelector('h4')||{}).textContent?.match(/([\d.]+)/)?.[1]||s+'.1'
        : item.dataset.step||s+'.1';
      if(s!==2) item.dataset.step = step;
      const st = DB_PROGRESO[s+'_'+step] || 'PENDIENTE';
      const dot = item.querySelector('.step-status');
      if(dot) setBullet(dot, st);
    });
  }
}

// ─── PROGRESIÓN IRREVERSIBLE ───
function nextStatus(cur){
  const idx = KANBAN_CYCLE.indexOf(cur);
  if(idx < 0 || idx >= 3) return cur;
  return KANBAN_CYCLE[idx+1];
}
function setBullet(dot, status){
  const idx = KANBAN_CYCLE.indexOf(status);
  dot.dataset.status = status;
  dot.className = 'step-status '+KANBAN_CLASS[idx>=0?idx:0];
  dot.textContent = KANBAN_SYMBOL[idx>=0?idx:0];
}

// ─── INYECTAR BULLETS ───
(function(){
for(let s=1;s<=9;s++){
  const section = document.getElementById('sec-'+s);
  if(!section) continue;
  if(s===2){
    section.querySelectorAll('.inv-card.var .inv-item').forEach(item => {
      const h4 = item.querySelector('h4');
      if(!h4) return;
      const m = h4.textContent.match(/([\d.]+)/);
      if(!m) return;
      const step = m[1];
      item.dataset.step = step;
      const dot = document.createElement('span');
      dot.className = 'step-status s-pendiente';
      dot.textContent = '●';
      dot.dataset.status = 'PENDIENTE';
      dot.dataset.seccion = s;
      dot.dataset.paso = step;
      dot.style.cssText = 'margin-left:6px;font-size:1.2rem;vertical-align:middle;cursor:pointer';
      dot.addEventListener('click', function(e){
        e.stopPropagation();
        const next = nextStatus(this.dataset.status);
        if(next===this.dataset.status) return;
        setBullet(this, next);
        guardarProgreso(parseInt(this.dataset.seccion), this.dataset.paso, next);
      });
      dot.addEventListener('contextmenu', function(e){
        e.preventDefault();
        e.stopPropagation();
        if(this.dataset.status==='NO_APLICA'){
          setBullet(this, 'PENDIENTE');
          guardarProgreso(parseInt(this.dataset.seccion), this.dataset.paso, 'PENDIENTE');
        } else {
          setBullet(this, 'NO_APLICA');
          guardarProgreso(parseInt(this.dataset.seccion), this.dataset.paso, 'NO_APLICA');
        }
      });
      h4.parentNode.insertBefore(dot, h4.nextSibling);
    });
  } else {
    section.querySelectorAll('.step-card').forEach((card, idx) => {
      const nameEl = card.querySelector('.step-name');
      if(!nameEl) return;
      let step;
      const match = nameEl.textContent.match(/(\d{2}|\d+\.\d+)/);
      if(match) step = match[1];
      else step = s+'.'+(idx+1);
      card.dataset.step = step;
      const dot = document.createElement('span');
      dot.className = 'step-status s-pendiente';
      dot.textContent = '●';
      dot.dataset.status = 'PENDIENTE';
      dot.dataset.seccion = s;
      dot.dataset.paso = step;
      dot.addEventListener('click', function(e){
        e.stopPropagation();
        const next = nextStatus(this.dataset.status);
        if(next===this.dataset.status) return;
        setBullet(this, next);
        guardarProgreso(parseInt(this.dataset.seccion), this.dataset.paso, next);
      });
      dot.addEventListener('contextmenu', function(e){
        e.preventDefault();
        e.stopPropagation();
        if(this.dataset.status==='NO_APLICA'){
          setBullet(this, 'PENDIENTE');
          guardarProgreso(parseInt(this.dataset.seccion), this.dataset.paso, 'PENDIENTE');
        } else {
          setBullet(this, 'NO_APLICA');
          guardarProgreso(parseInt(this.dataset.seccion), this.dataset.paso, 'NO_APLICA');
        }
      });
      const head = card.querySelector('.step-head');
      if(head) head.appendChild(dot);
    });
  }
}})();

// ─── PROJECT SELECTOR ───
(function(){
  const container = document.getElementById('proj-cards');
  if(!container) return;
  const saved = localStorage.getItem('soma_proyecto_id');
  const MOMENTOS = ['lead','entrevistado','programado','cotizado','contratado','primera_entrega','entrega_final','terminado'];

  function renderCards(proyectos){
    const filtrados = (proyectos||[]).filter(p => MOMENTOS.includes(p.pipeline_estado));
    if(!filtrados.length){
      container.innerHTML = '<p style="font-family:\'Courier New\',monospace;font-size:.65rem;color:var(--text3);padding:10px;">Sin proyectos registrados.</p>';
      return;
    }
    container.innerHTML = filtrados.map(p => {
      const sel = String(p.id) === String(saved) ? ' selected' : '';
      return `<div class="proj-card${sel}" data-id="${p.id}">
        <div class="proj-name"><span>${esc(p.nombre_proyecto || p.temp_id || '—')}</span><span class="arrow${sel?' open':''}">▶</span></div>
        <div class="proj-details${sel?' open':''}"><div class="proj-details-inner">
          <dt>ID SOMA</dt><dd>${esc(p.temp_id||'—')}</dd>
          <dt>Cliente</dt><dd>${esc(p.nombre_cliente || p.contacto || '—')}</dd>
          <dt>Tipo</dt><dd>${esc(p.tipo_proyecto || '—')}</dd>
          <dt>Nivel</dt><dd>${esc(p.nivel_proyecto || '—')} · ${p.m2||'?'} m²</dd>
          <button class="btn-prog" data-id="${p.id}">📐 PROGRAMA</button>
          <div class="proj-progress-wrap"><div class="proj-progress-bar" id="prog-bar-${p.id}"><div class="proj-progress-fill" id="prog-fill-${p.id}" style="width:0%"></div></div><div class="proj-progress-label"><span>Avance</span><span id="prog-pct-${p.id}">0%</span></div></div>
        </div></div>
      </div>`;
    }).join('');

    container.querySelectorAll('.proj-card').forEach(card => {
      card.addEventListener('click', async function(e){
        if(e.target.closest('.btn-prog')) return;
        const id = this.dataset.id;
        const isSelected = this.classList.contains('selected');
        if(isSelected){
          this.classList.remove('selected');
          this.querySelector('.proj-details').classList.remove('open');
          this.querySelector('.arrow').classList.remove('open');
          localStorage.removeItem('soma_proyecto_id');
          PROYECTO_ACTUAL = null;
          DATOS_PROYECTO = null;
          return;
        }
        container.querySelectorAll('.proj-card').forEach(c => {
          c.classList.remove('selected');
          c.querySelector('.proj-details').classList.remove('open');
          c.querySelector('.arrow').classList.remove('open');
        });
        this.classList.add('selected');
        this.querySelector('.proj-details').classList.add('open');
        this.querySelector('.arrow').classList.add('open');
        await cargarDatosProyecto(id);
      });
    });

    container.querySelectorAll('.btn-prog').forEach(btn => {
      btn.addEventListener('click', function(e){
        e.stopPropagation();
        window.open('/dashboard', '_blank');
      });
    });

    if(saved){
      const matched = container.querySelector(`.proj-card[data-id="${saved}"]`);
      if(matched) matched.click();
    }
  }

  fetch('/get_leads').then(r=>r.json()).then(p=>{
    if(Array.isArray(p)) renderCards(p);
  }).catch(()=>{});
})();

// ─── EXPEDIENTE ───
function abrirExpediente(){
  if(!PROYECTO_ACTUAL){ alert('Selecciona un proyecto primero.'); return; }
  window.open('/lead/'+PROYECTO_ACTUAL+'/expediente-pdf', '_blank');
}

// ─── ESTACIÓN 1 ───
function renderContactoReal(){
  const lead = DATOS_PROYECTO?.lead;
  if(!lead) return;
  const h = document.querySelector('#sec-1 .detail-header p');
  if(h) h.textContent = `Proyecto: ${esc(lead.nombre_proyecto||lead.temp_id||'—')} · Cliente: ${esc(lead.nombre_cliente||lead.contacto||'—')} · Estado: ${lead.pipeline_estado||'—'}`;
}

// ─── ESTACIÓN 2 ───
function renderImmersionReal(){
  // ya no inyecta tarjeta — reemplazada por 2.2.1.1 Datos de Inmersión (expediente)
}

// ─── ESTACIÓN 3: PROGRAMA EN 3.3 ───
function renderProgramaReal(){
  const proyId = PROYECTO_ACTUAL;
  if(!proyId) return;
  const programa = DATOS_PROYECTO?.programa;
  if(!programa || !programa.length) return;
  const detail3 = document.querySelector('#sec-3 .step-card:nth-child(3) .step-detail');
  if(!detail3) return;
  const existing = detail3.querySelector('.real-programa-card');
  if(existing) existing.remove();
  const totalM2 = programa.reduce((s,e) => s+Number(e.area||0), 0);
  const zonas = {1:'Social',2:'Operativa',3:'Descanso',4:'Soporte',5:'Transición'};
  const porZona = {};
  programa.forEach(e => {
    const z = e.zona||1; if(!porZona[z]) porZona[z]={count:0,area:0};
    porZona[z].count++; porZona[z].area+=Number(e.area||0);
  });
  const zonasHtml = Object.entries(porZona).map(([z,d]) =>
    `<span style="color:#999;">Z${z} ${zonas[z]||'?'}: ${d.count} esp · ${d.area.toFixed(1)} m²</span>`
  ).join(' · ');
  const html = `<div class="real-programa-card" style="margin-top:8px;border:1px solid rgba(212,94,44,.4);border-radius:4px;padding:6px;">
    <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:4px;">
      <span style="font-size:.65rem;color:#d45e2c;font-weight:700;">📋 PROGRAMA · ${programa.length} espacios · ${totalM2.toFixed(1)} m²</span>
      <span style="font-size:.55rem;color:#999;">${zonasHtml}</span>
      <button class="btn-guia" style="font-size:.55rem;padding:2px 8px;" onclick="event.stopPropagation();window.open('/programa/${proyId}/html','_blank')">📋 GENERAR PROGRAMA ARQUITECTÓNICO</button>
    </div>
  </div>`;
  detail3.insertAdjacentHTML('beforeend', html);
}

// ─── KANBAN DASHBOARD ───
function renderKanbanDashboard(){
  const container = document.getElementById('ctrl-sections');
  if(!container) return;
  const SECTIONS = {1:'Contacto',2:'Investigación',3:'Análisis',4:'Conceptualización',5:'Modelado+Vis.',6:'Antep. Básico',7:'Representación',8:'Antep. Integral',9:'Coord.+Planos'};
  const ALL_STATUS = {PENDIENTE:0,EN_PROGRESO:0,LISTO:0,APROBADO:0};
  let html = '';
  for(let s=1;s<=9;s++){
    const sec = document.getElementById('sec-'+s);
    if(!sec) continue;
    const counts = {PENDIENTE:0,EN_PROGRESO:0,LISTO:0,APROBADO:0,NO_APLICA:0};
    let validos = 0;
    const items = varItemsInSection(s);
    items.forEach(item => {
      const step = (s===2)
        ? (item.querySelector('h4')?.textContent?.match(/([\d.]+)/)?.[1]||s+'.1')
        : item.dataset.step||s+'.1';
      const st = DB_PROGRESO[s+'_'+step] || 'PENDIENTE';
      if(st==='NO_APLICA'){ counts.NO_APLICA++; return; }
      validos++;
      if(KANBAN_CYCLE.indexOf(st)>=0) counts[st]++;
      else counts['PENDIENTE']++;
    });
    if(!validos && !counts.NO_APLICA){ html+=sectionBarHtml(s,SECTIONS[s],counts,1); continue; }
    KANBAN_CYCLE.slice(0,4).forEach(c=>ALL_STATUS[c]+=(counts[c]||0));
    html += sectionBarHtml(s,SECTIONS[s],counts,validos||1);
  }
  container.innerHTML = html;
  document.getElementById('ctrl-total-pen').textContent = ALL_STATUS['PENDIENTE'];
  document.getElementById('ctrl-total-pro').textContent = ALL_STATUS['EN_PROGRESO'];
  document.getElementById('ctrl-total-lis').textContent = ALL_STATUS['LISTO'];
  document.getElementById('ctrl-total-apr').textContent = ALL_STATUS['APROBADO'];
}

function sectionBarHtml(s,name,counts,total){
  const MAP = [
    {cls:'bar-pendiente',c:'#555',status:'PENDIENTE'},
    {cls:'bar-progreso', c:'#ff9800',status:'EN_PROGRESO'},
    {cls:'bar-listo',    c:'#4caf50',status:'LISTO'},
    {cls:'bar-aprobado', c:'#2196f3',status:'APROBADO'}
  ];
  const t = total||1;
  const cN = counts.NO_APLICA||0;
  return `<div class="ctrl-section"><div class="ctrl-section-header"><h3>${s}. ${name}</h3><span>${total} pasos ${cN?'('+cN+' NA)':''}</span></div><div class="ctrl-bar">
    ${MAP.map(o=>'<div class="ctrl-bar-seg '+o.cls+'" style="width:'+((counts[o.status]||0)/t*100)+'%"></div>').join('')}
    ${cN?'<div class="ctrl-bar-seg bar-noaplica" style="width:'+(cN/t*100)+'%"></div>':''}
    </div><div style="display:flex;gap:12px;margin-top:6px;font-family:Courier New,monospace;font-size:.5rem">
    ${MAP.map(o=>'<span style="color:'+o.c+'">● '+(counts[o.status]||0)+' '+o.status+'</span>').join('')}
    ${cN?'<span style="color:#333;opacity:.5">○ '+cN+' NO_APLICA</span>':''}</div></div>`;
}

document.addEventListener('click', function(e){
  if(e.target.closest('.step-status') && document.getElementById('sec-10')?.classList.contains('active')){
    setTimeout(renderKanbanDashboard, 50);
  }
});

// ─── DOMContentLoaded ───
// ─── DIAGRAMA DE RELACIONES (vis-network) ───
let diagramaNetwork = null;
let connectNode = null;
const ZONA_COLOR = {1:'#4d7ae6',2:'#e6cc33',3:'#e64d4d',4:'#e68033',5:'#9933cc'};
const ZONA_NOMBRE = {1:'Social',2:'Operativa',3:'Descanso',4:'Soporte',5:'Transición'};

function abrirDiagramaRelaciones(){
  const section = document.getElementById('diagrama-section');
  if(!section) return;
  section.classList.toggle('visible');
  if(section.classList.contains('visible') && PROYECTO_ACTUAL){
    renderProgramaRelaciones();
    renderDiagramaRelaciones(PROYECTO_ACTUAL);
    section.scrollIntoView({behavior:'smooth',block:'start'});
  }
}

function renderProgramaRelaciones(){
  const container = document.getElementById('diagrama-programa');
  if(!container) return;
  const programa = DATOS_PROYECTO?.programa;
  if(!programa || !programa.length){ container.innerHTML='<div style="color:var(--text3);font-size:.55rem;">Sin programa arquitectónico</div>'; return; }
  const zonas = {1:'Social',2:'Operativa',3:'Descanso',4:'Soporte',5:'Transición'};
  let html = '<div class="prog-header"><span>Programa Arquitectónico · '+programa.length+' espacios</span></div>';
  [...programa].sort((a,b)=>(a.zona||1)-(b.zona||1)).forEach(e => {
    const clave = e.clave||'?';
    const rels = (()=>{try{return JSON.parse(e.relacion_directa||'[]');}catch{return [];}})();
    const relTags = rels.map(r => {
      const otro = programa.find(p => p.clave===r);
      return `<span class="rel-tag" onclick="eliminarRelacion('${esc(clave)}','${esc(r)}')" title="Quitar ${esc(otro?otro.espacio:r)}">${esc(otro?otro.espacio:r)} ✕</span>`;
    }).join('');
    html += '<div class="prog-card">';
    html += '<div class="prog-row">';
    html += '<span class="prog-nombre">'+esc(e.espacio)+'</span>';
    html += '<span class="prog-m2">'+Number(e.area||0).toFixed(1)+' m²</span>';
    html += '<span class="prog-zona" style="color:'+(ZONA_COLOR[e.zona]||'#666')+'">'+(zonas[e.zona]||'Z'+e.zona)+'</span>';
    html += '<span class="prog-rels" id="prog-rels-'+esc(clave)+'">'+relTags+'</span>';
    html += '<span class="rel-add" onclick="togglePicker(\''+esc(clave)+'\')">+</span>';
    html += '</div>';
    html += '<div class="prog-picker" id="prog-picker-'+esc(clave)+'" style="display:none"></div>';
    html += '</div>';
  });
  container.innerHTML = html;
}

let PICKER_OPEN = null;

function togglePicker(clave){
  const picker = document.getElementById('prog-picker-'+clave);
  if(!picker) return;
  if(PICKER_OPEN && PICKER_OPEN!==clave){
    const prev = document.getElementById('prog-picker-'+PICKER_OPEN);
    if(prev) prev.style.display = 'none';
  }
  if(picker.style.display==='block'){
    picker.style.display = 'none';
    PICKER_OPEN = (PICKER_OPEN===clave) ? null : PICKER_OPEN;
    return;
  }
  PICKER_OPEN = clave;
  picker.style.display = 'block';
  if(picker.children.length===0) renderPickerContent(clave, picker);
}

function renderPickerContent(clave, picker){
  const programa = DATOS_PROYECTO?.programa;
  if(!programa) return;
  const actual = programa.find(e => e.clave===clave);
  if(!actual) return;
  const rels = (()=>{try{return JSON.parse(actual.relacion_directa||'[]');}catch{return [];}})();
  const otros = programa.filter(e => e.clave && e.clave!==clave);
  let checks = '';
  otros.forEach(o => {
    const checked = rels.includes(o.clave) ? 'checked' : '';
    checks += '<label><input type="checkbox" value="'+esc(o.clave)+'" '+checked+'> '+esc(o.espacio)+'</label>';
  });
  picker.innerHTML = '<div class="picker-grid">'+checks+'</div>'
    + '<div class="picker-actions">'
    + '<button class="btn-save" onclick="guardarPicker(\''+esc(clave)+'\')">✓ GUARDAR</button>'
    + '<button onclick="togglePicker(\''+esc(clave)+'\')">✕ CANCELAR</button>'
    + '</div>';
}

async function guardarPicker(clave){
  const picker = document.getElementById('prog-picker-'+clave);
  if(!picker) return;
  const checks = picker.querySelectorAll('input[type=checkbox]:checked');
  const nuevas = Array.from(checks).map(c => c.value);
  const programa = DATOS_PROYECTO?.programa;
  const actual = programa?.find(e => e.clave===clave);
  if(!actual) return;
  const viejas = (()=>{try{return JSON.parse(actual.relacion_directa||'[]');}catch{return [];}})();
  const agregar = nuevas.filter(r => !viejas.includes(r));
  const quitar = viejas.filter(r => !nuevas.includes(r));
  try {
    await fetch('/programa/espacio/'+actual.id+'/relaciones', {
      method: 'PUT', headers: {'Content-Type':'application/json'},
      body: JSON.stringify({ relaciones: nuevas })
    });
    actual.relacion_directa = JSON.stringify(nuevas);
    for(const t of agregar){
      const otro = programa.find(e => e.clave===t);
      if(!otro) continue;
      const relsOtro = (()=>{try{return JSON.parse(otro.relacion_directa||'[]');}catch{return [];}})();
      if(!relsOtro.includes(clave)){
        relsOtro.push(clave);
        await fetch('/programa/espacio/'+otro.id+'/relaciones', {
          method: 'PUT', headers: {'Content-Type':'application/json'},
          body: JSON.stringify({ relaciones: relsOtro })
        });
        otro.relacion_directa = JSON.stringify(relsOtro);
      }
    }
    for(const t of quitar){
      const otro = programa.find(e => e.clave===t);
      if(!otro) continue;
      const relsOtro = (()=>{try{return JSON.parse(otro.relacion_directa||'[]');}catch{return [];}})();
      const idx = relsOtro.indexOf(clave);
      if(idx!==-1){
        relsOtro.splice(idx,1);
        await fetch('/programa/espacio/'+otro.id+'/relaciones', {
          method: 'PUT', headers: {'Content-Type':'application/json'},
          body: JSON.stringify({ relaciones: relsOtro })
        });
        otro.relacion_directa = JSON.stringify(relsOtro);
      }
    }
    picker.style.display = 'none';
    PICKER_OPEN = null;
    renderProgramaRelaciones();
    if(PROYECTO_ACTUAL) renderDiagramaRelaciones(PROYECTO_ACTUAL);
  } catch(e){ console.error(e); }
}

async function eliminarRelacion(clave, target){
  const programa = DATOS_PROYECTO?.programa;
  const actual = programa?.find(e => e.clave===clave);
  if(!actual) return;
  const otro = programa?.find(e => e.clave===target);
  try {
    const rels = (()=>{try{return JSON.parse(actual.relacion_directa||'[]');}catch{return [];}})();
    const idx = rels.indexOf(target);
    if(idx!==-1){
      rels.splice(idx, 1);
      await fetch('/programa/espacio/'+actual.id+'/relaciones', {
        method: 'PUT', headers: {'Content-Type':'application/json'},
        body: JSON.stringify({ relaciones: rels })
      });
      actual.relacion_directa = JSON.stringify(rels);
    }
    if(otro){
      const relsOtro = (()=>{try{return JSON.parse(otro.relacion_directa||'[]');}catch{return [];}})();
      const jdx = relsOtro.indexOf(clave);
      if(jdx!==-1){
        relsOtro.splice(jdx, 1);
        await fetch('/programa/espacio/'+otro.id+'/relaciones', {
          method: 'PUT', headers: {'Content-Type':'application/json'},
          body: JSON.stringify({ relaciones: relsOtro })
        });
        otro.relacion_directa = JSON.stringify(relsOtro);
      }
    }
    renderProgramaRelaciones();
    if(PROYECTO_ACTUAL) renderDiagramaRelaciones(PROYECTO_ACTUAL);
  } catch(e){ console.error(e); }
}

function toggleConnectMode(){
  const btn = document.getElementById('btn-connect-mode');
  if(!btn) return;
  btn.classList.toggle('active');
  btn.textContent = btn.classList.contains('active') ? '🔗 CONECTANDO...' : '🔗 CONECTAR';
  if(!btn.classList.contains('active')) connectNode = null;
}

function handleDiagramClick(params){
  if(params.nodes.length===1){
    const clicked = params.nodes[0];
    if(connectNode===null){
      connectNode = clicked;
      diagramaNetwork.selectNodes([clicked]);
    } else if(connectNode!==clicked){
      diagramaNetwork.selectNodes([]);
      const from = connectNode, to = clicked;
      connectNode = null;
      agregarRelacionDiagrama(from, to);
    } else {
      connectNode = null;
      diagramaNetwork.selectNodes([]);
    }
  } else if(params.edges.length===1 && params.nodes.length===0){
    const edgeId = params.edges[0];
    connectNode = null;
    diagramaNetwork.selectNodes([]);
    eliminarRelacionDiagrama(edgeId);
  } else {
    connectNode = null;
    diagramaNetwork.selectNodes([]);
  }
}

async function agregarRelacionDiagrama(from, to){
  const programa = DATOS_PROYECTO?.programa;
  const a = programa?.find(e => e.clave===from);
  const b = programa?.find(e => e.clave===to);
  if(!a || !b) return;
  try {
    const relsA = (()=>{try{return JSON.parse(a.relacion_directa||'[]');}catch{return [];}})();
    if(!relsA.includes(to)){
      relsA.push(to);
      await fetch('/programa/espacio/'+a.id+'/relaciones', {
        method: 'PUT', headers: {'Content-Type':'application/json'},
        body: JSON.stringify({ relaciones: relsA })
      });
      a.relacion_directa = JSON.stringify(relsA);
    }
    const relsB = (()=>{try{return JSON.parse(b.relacion_directa||'[]');}catch{return [];}})();
    if(!relsB.includes(from)){
      relsB.push(from);
      await fetch('/programa/espacio/'+b.id+'/relaciones', {
        method: 'PUT', headers: {'Content-Type':'application/json'},
        body: JSON.stringify({ relaciones: relsB })
      });
      b.relacion_directa = JSON.stringify(relsB);
    }
    renderProgramaRelaciones();
    if(PROYECTO_ACTUAL) renderDiagramaRelaciones(PROYECTO_ACTUAL);
  } catch(e){ console.error(e); }
}

async function eliminarRelacionDiagrama(edgeId){
  const parts = edgeId.split('→');
  if(parts.length!==2) return;
  const from = parts[0], to = parts[1];
  const programa = DATOS_PROYECTO?.programa;
  const a = programa?.find(e => e.clave===from);
  const b = programa?.find(e => e.clave===to);
  try {
    if(a){
      const ra = (()=>{try{return JSON.parse(a.relacion_directa||'[]');}catch{return [];}})();
      const ia = ra.indexOf(to);
      if(ia!==-1){
        ra.splice(ia,1);
        await fetch('/programa/espacio/'+a.id+'/relaciones', {
          method: 'PUT', headers: {'Content-Type':'application/json'},
          body: JSON.stringify({ relaciones: ra })
        });
        a.relacion_directa = JSON.stringify(ra);
      }
    }
    if(b){
      const rb = (()=>{try{return JSON.parse(b.relacion_directa||'[]');}catch{return [];}})();
      const ib = rb.indexOf(from);
      if(ib!==-1){
        rb.splice(ib,1);
        await fetch('/programa/espacio/'+b.id+'/relaciones', {
          method: 'PUT', headers: {'Content-Type':'application/json'},
          body: JSON.stringify({ relaciones: rb })
        });
        b.relacion_directa = JSON.stringify(rb);
      }
    }
    renderProgramaRelaciones();
    if(PROYECTO_ACTUAL) renderDiagramaRelaciones(PROYECTO_ACTUAL);
  } catch(e){ console.error(e); }
}

async function renderDiagramaRelaciones(proyectoId, zona){
  const canvas = document.getElementById('diagrama-canvas');
  const info = document.getElementById('diagrama-info');
  if(!canvas) return;
  if(!window.vis || !window.vis.Network){
    if(info) info.textContent = 'Error: vis-network no cargó. Recarga la página.';
    return;
  }
  const z = zona || parseInt(document.getElementById('diagrama-zona-filter')?.value||'0');
  const url = `/api/diagrama/grafo/${proyectoId}${z>0?'?zona='+z:''}`;
  const res = await apiGet(url);
  if(!res || !res.nodes || !res.nodes.length){
    if(info) info.textContent = 'Sin espacios en el programa arquitectónico para este proyecto.';
    if(diagramaNetwork){ diagramaNetwork.destroy(); diagramaNetwork=null; }
    return;
  }
  if(diagramaNetwork){ diagramaNetwork.destroy(); diagramaNetwork=null; }
  canvas.innerHTML = '';
  const savedKey = 'soma_diagrama_' + proyectoId + '_zona_' + z;
  let savedPos = {};
  try{ savedPos = JSON.parse(localStorage.getItem(savedKey)||'{}'); }catch(e){}

  const nodeData = res.nodes.map(n => {
    const pos = savedPos[n.id];
    return {
      id: n.id, label: n.label,
      size: Math.max(12, Math.min(n.size, 60)),
      color: { background: n.color, border: '#ffffff' },
      font: { color: '#f4f1ee', size: Math.max(6, Math.min(n.size*0.45, 16)), face: 'Courier New', strokeWidth: 0 },
      shape: 'dot',
      title: '<b>'+esc(n.espacio)+'</b><br>Clave: '+esc(n.id)+'<br>Área: '+n.area+' m²<br>Zona: '+(ZONA_NOMBRE[n.zona]||n.zona)+'<br>Tipo: '+esc(n.tipo),
      x: pos ? pos.x : undefined, y: pos ? pos.y : undefined
    };
  });
  const edgeData = res.edges.map(e => ({
    id: e.from+'→'+e.to, from: e.from, to: e.to,
    color: { color: '#f4f1ee', opacity: 0.35 },
    width: 1.5, smooth: { type: 'continuous' }
  }));

  try {
    diagramaNetwork = new vis.Network(canvas, { nodes: nodeData, edges: edgeData }, {
      physics: {
        enabled: true, solver: 'barnesHut',
        barnesHut: { gravitationalConstant: -800, centralGravity: 0.2, springLength: 150, springConstant: 0.03, damping: 0.6 },
        stabilization: { iterations: 30 }
      },
      layout: { improvedLayout: true, randomSeed: 42 },
      interaction: { hover: true, tooltipDelay: 200, navigationButtons: true, keyboard: true },
      configure: { enabled: false }
    });
    diagramaNetwork.once('stabilizationIterationsDone', function(){
      diagramaNetwork.setOptions({ physics: { enabled: false } });
      diagramaNetwork.fit();
      guardarPosicionesDiagrama();
    });
    diagramaNetwork.on('dragEnd', function(){ guardarPosicionesDiagrama(); });
    diagramaNetwork.on('zoom', function(){ guardarPosicionesDiagrama(); });
    if(info) info.textContent = res.nodes.length + ' espacios · ' + res.edges.length + ' relaciones';
    diagramaNetwork.on('click', function(params){
      const btn = document.getElementById('btn-connect-mode');
      if(!btn || !btn.classList.contains('active')){ connectNode=null; return; }
      handleDiagramClick(params);
    });
  } catch(e) {
    if(info) info.textContent = 'Error al renderizar: ' + e.message;
    console.error('Diagrama error:', e);
  }
}

function guardarPosicionesDiagrama(){
  if(!diagramaNetwork || !PROYECTO_ACTUAL) return;
  const z = parseInt(document.getElementById('diagrama-zona-filter')?.value||'0');
  const key = 'soma_diagrama_' + PROYECTO_ACTUAL + '_zona_' + z;
  const pos = diagramaNetwork.getPositions();
  try{ localStorage.setItem(key, JSON.stringify(pos)); }catch(e){}
}

function resetDiagrama(){
  const z = parseInt(document.getElementById('diagrama-zona-filter')?.value||'0');
  const key = 'soma_diagrama_' + PROYECTO_ACTUAL + '_zona_' + z;
  localStorage.removeItem(key);
  if(PROYECTO_ACTUAL) renderDiagramaRelaciones(PROYECTO_ACTUAL, z);
}

function exportDiagramaPDF(){
  if(!diagramaNetwork) return;
  const container = document.getElementById('diagrama-canvas');
  const c = container.querySelector('canvas');
  if(!c) return;
  if(!window.jspdf){
    const info = document.getElementById('diagrama-info');
    if(info) info.textContent = 'Error: jsPDF no cargó. Recarga.';
    return;
  }
  const { jsPDF } = window.jspdf;
  const doc = new jsPDF({ orientation: 'landscape', unit: 'mm', format: 'a4' });
  const pw = doc.internal.pageSize.getWidth();
  const ph = doc.internal.pageSize.getHeight();

  const tmpCanvas = document.createElement('canvas');
  tmpCanvas.width = c.width; tmpCanvas.height = c.height;
  const ctx = tmpCanvas.getContext('2d');
  ctx.fillStyle = '#1a1a1a';
  ctx.fillRect(0, 0, tmpCanvas.width, tmpCanvas.height);
  ctx.drawImage(c, 0, 0);
  const imgData = tmpCanvas.toDataURL('image/png');
  const cw = c.width, ch = c.height;
  const aspect = cw / ch;
  let iw = pw - 20, ih = iw / aspect;
  if(ih > ph - 50){ ih = ph - 50; iw = ih * aspect; }
  doc.addImage(imgData, 'PNG', 10, 25, iw, ih);

  const proyecto = DATOS_PROYECTO?.lead;
  const nombre = proyecto?.nombre_proyecto || proyecto?.contacto || 'Proyecto';
  doc.setFontSize(10);
  doc.text('Diagrama de Relaciones Espaciales — ' + nombre, 10, 10);
  doc.setFontSize(7);
  doc.text('SOMA Algoritmo 3.4', 10, 15);

  const zonas = [
    {color:'#4d7ae6', nombre:'Social'},
    {color:'#e6cc33', nombre:'Operativa'},
    {color:'#e64d4d', nombre:'Descanso'},
    {color:'#e68033', nombre:'Soporte'},
    {color:'#9933cc', nombre:'Transición'}
  ];
  const ly = Math.max(ih + 30, 30);
  doc.setFontSize(8);
  doc.text('Simbología de Zonas:', 10, ly);
  let lx = 10;
  zonas.forEach(z => {
    doc.setFillColor(parseInt(z.color.slice(1,3),16), parseInt(z.color.slice(3,5),16), parseInt(z.color.slice(5,7),16));
    doc.rect(lx, ly+3, 5, 5, 'F');
    doc.setTextColor(100);
    doc.text(z.nombre, lx+7, ly+7);
    lx += 35;
  });

  const infoEl = document.getElementById('diagrama-info');
  const edgeCount = infoEl ? infoEl.textContent : '';
  doc.setTextColor(150); doc.setFontSize(6);
  doc.text(edgeCount, 10, ph - 5);
  doc.text(new Date().toLocaleDateString(), pw - 30, ph - 5);

  doc.save('diagrama_soma_' + PROYECTO_ACTUAL + '.pdf');
}

document.addEventListener('DOMContentLoaded',()=>{
  document.querySelectorAll('.step-card').forEach(c=>{
    c.setAttribute('role','button');
    c.setAttribute('aria-expanded','false');
    const d=c.querySelector('.step-detail');
    if(d)d.setAttribute('aria-hidden','true');
  });
  document.querySelectorAll('.station').forEach(s=>s.setAttribute('role','button'));
  const hash=window.location.hash.replace('#','');
  if(hash&&hash.startsWith('sec-')){
    const n=parseInt(hash.replace('sec-',''));
    if(n>=1&&n<=10) showSection(n);
  }else{
    const t=document.getElementById('timeline');
    if(t) t.querySelectorAll('.station')[3].scrollIntoView({inline:'center',block:'nearest'});
  }
  if(PROYECTO_ACTUAL) cargarDatosProyecto(PROYECTO_ACTUAL);
});
