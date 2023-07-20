function publish_button() {
    const is_private = document.getElementById('id_is_private');
    const publish_button = document.getElementById('publish');
    if (is_private) {
        if (is_private.checked) {
            publish_button.innerHTML = "Save";
        } else {
            publish_button.innerHTML = "Publish";
        }
        is_private.addEventListener('change', (e) => {
            if (e.target.checked) {
                publish_button.innerHTML = "Save";
            } else {
                publish_button.innerHTML = "Publish";
            }
        })
    }

}

function markdown_preview() {
    let option = {
        linkify: true,
        // breaks: true,
        typographer: true,
    }

    let md = new markdownit(option);
    // md.use(markdownitEmoji);

    let live_preview = document.getElementById('note-preview');
    let code_editor = document.getElementById('id_body');

    if (code_editor) {
        code_editor.addEventListener('input', (e) => {
            live_preview.innerHTML = md.render(code_editor.value);
        });
    }
    console.log('live preview added succesfully')
}

function preview_buttons_switch() {
    const change_view = Array.from(document.querySelectorAll('input[name="changeview"]'));

    let _editor_panel = document.getElementById('note-editor');
    let _preview_panel = document.getElementById('note-preview-container');

    change_view.forEach(element => {
        element.addEventListener('change', () => {
            if (element.value == '0') {
                _preview_panel.style.display = 'none';
                _editor_panel.style.display = 'block'

            } else if (element.value == '1') {
                _preview_panel.style.display = 'block';
                _editor_panel.style.display = 'block'

            } else if (element.value == '2') {
                _preview_panel.style.display = 'block';
                _editor_panel.style.display = 'none'
            }
        });
    });


}