const { makeWASocket, useMultiFileAuthState, DisconnectReason } = require('@whiskeysockets/baileys');
const http = require('http');
const url = require('url');
const fs = require('fs');
const qrcode = require('qrcode-terminal');

const PORT = process.env.WA_SERVICE_PORT || 3001;
const TARGET_NUMBER = process.env.WA_NOTIFICACION || '5219993619433';
const SESSION_DIR = './session-data';
const WA_NUMBER = process.env.VINCULAR_NUMERO || '';

let sock = null;
let clientReady = false;
let lastError = null;
let pairingCodeGenerated = null;

async function startBot() {
    const { state, saveCreds } = await useMultiFileAuthState(SESSION_DIR);

    sock = makeWASocket({
        auth: state,
        syncFullHistory: false,
        markOnlineOnConnect: false,
        browser: ['SOMA Bot', 'Chrome', '22.04.4'],
    });

    if (!state.creds?.registered && WA_NUMBER) {
        setTimeout(async () => {
            try {
                const code = await sock.requestPairingCode(WA_NUMBER);
                pairingCodeGenerated = code;
                console.log('\n═══════════════════════════════════════════');
                console.log('   📱 CÓDIGO DE VINCULACIÓN WHATSAPP');
                console.log('   Abre WhatsApp > 3 puntos > Dispositivos');
                console.log('   vinculados > Vincular con número de teléfono');
                console.log('');
                console.log(`   Código: ${code.match(/.{1,3}/g).join('-')}`);
                console.log('');
                console.log('═══════════════════════════════════════════\n');
            } catch (e) {
                console.log('Error generando código de vinculación:', e.message);
            }
        }, 2000);
    }

    sock.ev.on('connection.update', (update) => {
        const { connection, qr, lastDisconnect } = update;

        if (qr && !WA_NUMBER) {
            console.log('\n=== ESCANEA ESTE QR CON WHATSAPP ===');
            console.log('Abre WhatsApp > 3 puntos > Dispositivos vinculados > Vincular dispositivo');
            const qrcode = require('qrcode-terminal');
            qrcode.generate(qr, { small: true });
            lastError = 'QR generado — escanea con WhatsApp';
        }

        if (connection === 'open') {
            console.log('✓ WhatsApp conectado!');
            console.log(` Notificaciones para: ${TARGET_NUMBER}`);
            clientReady = true;
            lastError = null;
            pairingCodeGenerated = null;
        }

        if (connection === 'close') {
            const reason = lastDisconnect?.error?.output?.statusCode;
            clientReady = false;

            if (reason === DisconnectReason.loggedOut) {
                console.log('✗ Sesión cerrada remotamente. Elimina session-data/ y reconecta.');
                lastError = 'Sesión cerrada. Re-autenticación requerida.';
            } else {
                console.log(`✗ Desconectado (razón: ${reason}). Reconectando en 5s...`);
                lastError = `Desconectado (${reason})`;
                setTimeout(startBot, 5000);
            }
        }
    });

    sock.ev.on('creds.update', saveCreds);
}

async function sendMessage(text) {
    if (!clientReady || !sock) {
        throw new Error('WhatsApp no conectado. Escanea el QR primero.');
    }
    const jid = TARGET_NUMBER + '@s.whatsapp.net';
    await sock.sendMessage(jid, { text });
}

const server = http.createServer(async (req, res) => {
    res.setHeader('Content-Type', 'application/json');
    res.setHeader('Access-Control-Allow-Origin', '*');

    const parsed = url.parse(req.url, true);
    const path = parsed.pathname;

    if (req.method === 'OPTIONS') {
        res.writeHead(204);
        res.end();
        return;
    }

    if (path === '/status' && req.method === 'GET') {
        res.writeHead(200);
        res.end(JSON.stringify({
            ready: clientReady,
            error: lastError,
            target: TARGET_NUMBER,
            pairingCode: pairingCodeGenerated
        }));
        return;
    }

    if (path === '/send' && req.method === 'POST') {
        let body = '';
        req.on('data', chunk => body += chunk);
        req.on('end', async () => {
            try {
                const data = JSON.parse(body);
                if (!data.message) {
                    res.writeHead(400);
                    res.end(JSON.stringify({ error: 'Falta el campo "message"' }));
                    return;
                }
                await sendMessage(data.message);
                res.writeHead(200);
                res.end(JSON.stringify({ status: 'sent' }));
            } catch (e) {
                res.writeHead(500);
                res.end(JSON.stringify({ error: e.message }));
            }
        });
        return;
    }

    res.writeHead(404);
    res.end(JSON.stringify({ error: 'Not found' }));
});

server.listen(PORT, () => {
    console.log(`\n📱 Servicio WhatsApp SOMA corriendo en puerto ${PORT}`);
    console.log(`   Endpoints: GET /status, POST /send`);
    console.log(`   Número destino: ${TARGET_NUMBER}`);
    console.log('   Inicializando WhatsApp...\n');
});

startBot();
