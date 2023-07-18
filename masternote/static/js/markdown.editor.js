window.onload = () => {
    let option = {
        linkify: true,
        breaks: true,
        // html: true,
        typographer: true
    }
    let md = window.markdownit(option);

    let live_preview = document.getElementById('note-preview');
    let code_editor = document.getElementById('id_body');
    if (code_editor){

        code_editor.addEventListener('input', (e) => {
            live_preview.innerHTML = md.render(code_editor.value);
        });
    }

}

