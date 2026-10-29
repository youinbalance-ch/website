const toggle=document.querySelector('.menu');
const nav=document.querySelector('#navigation');
toggle?.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open)});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav?.classList.contains('open')){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.focus()}});
const form=document.querySelector('#contact-form');
form?.addEventListener('submit',e=>{e.preventDefault();if(!form.reportValidity())return;const d=new FormData(form);const body=`Hallo Tatjana,\n\n${d.get('message')}\n\nInteresse: ${d.get('topic')}\nName: ${d.get('name')}\nE-Mail: ${d.get('email')}`;document.querySelector('#draft').value=body;document.querySelector('#fallback').hidden=false;document.querySelector('#form-status').textContent='Dein E-Mail-Entwurf ist vorbereitet. Bitte prüfe und versende ihn in deiner E-Mail-App. Es wurde noch keine Anfrage verschickt.';window.location.href='mailto:tatjana.geiter1994@gmail.com?subject='+encodeURIComponent('Beratungsanfrage: '+d.get('topic'))+'&body='+encodeURIComponent(body)});
