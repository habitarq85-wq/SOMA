const UI = (() => {
    let toastTimer = null;

    function notify(message, type = 'success') {
        const container = document.getElementById('toast-container');
        if (!container) return;
        const el = document.createElement('div');
        el.className = `toast ${type}`;
        el.textContent = message;
        container.appendChild(el);
        setTimeout(() => { if (el.parentNode) el.remove(); }, 3000);
    }

    function confirmDialog(msg) {
        return new Promise(resolve => {
            const existing = document.querySelector('.modal-confirm');
            if (existing) existing.remove();

            const overlay = document.createElement('div');
            overlay.className = 'modal-overlay modal-confirm active';
            overlay.innerHTML = `
                <div class="modal-content" style="max-width:380px;text-align:center;">
                    <p style="font-family:'JetBrains Mono',monospace;font-size:.75rem;margin:10px 0 20px;">${API.esc(msg)}</p>
                    <div style="display:flex;gap:10px;justify-content:center;">
                        <button class="cand-btn btn-green" style="padding:8px 20px;font-size:.7rem;" id="cfm-yes">✓ Sí</button>
                        <button class="cand-btn" style="padding:8px 20px;font-size:.7rem;background:#888;color:#fff;" id="cfm-no">Cancelar</button>
                    </div>
                </div>`;
            document.body.appendChild(overlay);

            const closeOverlay = (result) => { overlay.remove(); if (!document.querySelector('.modal-overlay.active')) document.body.style.overflow = ''; resolve(result); };
            overlay.querySelector('#cfm-yes').onclick = () => closeOverlay(true);
            overlay.querySelector('#cfm-no').onclick = () => closeOverlay(false);
            overlay.onclick = e => { if (e.target === overlay) closeOverlay(false); };
        });
    }

    function openModal(id) {
        const el = document.getElementById(id);
        if (el) el.classList.add('active');
    }
    function restoreScroll() {
        document.body.style.overflow = '';
    }
    function closeModal(id) {
        const el = document.getElementById(id);
        if (el) el.classList.remove('active');
        if (!document.querySelector('.modal-overlay.active')) restoreScroll();
    }

    function loading(containerId, msg = 'Cargando...') {
        const el = document.getElementById(containerId);
        if (el) el.innerHTML = `<p class="loading-text">${msg}</p>`;
    }

    return { notify, confirmDialog, openModal, closeModal, loading };
})();

document.addEventListener('click', e => {
    if (e.target.classList.contains('modal-overlay')) {
        e.target.classList.remove('active');
        if (!document.querySelector('.modal-overlay.active')) document.body.style.overflow = '';
    }
});
document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
        document.querySelectorAll('.modal-overlay.active').forEach(m => m.classList.remove('active'));
        document.body.style.overflow = '';
    }
});
