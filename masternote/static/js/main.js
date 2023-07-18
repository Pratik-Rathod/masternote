//show markdown live



window.onload = function () {

    let option = {
        linkify: true,
        breaks: true,
        // html: true,
        typographer: true
    }
    let md = window.markdownit(option);

    let live_preview = document.getElementById('note-preview');
    let code_editor = document.getElementById('id_body');
    if (code_editor) {
        code_editor.addEventListener('input', (e) => {
            live_preview.innerHTML = md.render(code_editor.value);
        });
    }

    setInterval(
        () => {
            const mess = document.getElementById("messages")
            if (mess) {
                mess.remove()
            }

            // let errorlistcollection = document.getElementsByClassName("errorlist")
            // let arrerrorlist = Array.from(errorlistcollection)
            // arrerrorlist.forEach(error => {
            //     error.remove()
            // });
        }
        , 2500);


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

    form_input = document.querySelectorAll('.form input');
    // console.log(form_input)

    form_input.forEach(element => {
        let a = element.parentElement.querySelector(".helptext")

        if (document.activeElement === element) {
            if (!element.value) {
                if (a) {
                    a.style.cssText = "display:block"
                }
            }
        }
        element.addEventListener("input", (e) => {
            if (element.value) {
                if (a) {
                    a.style.cssText = "display:none"
                }

            } else {
                if (a) {
                    a.style.cssText = "display:block"
                }
            }
        })

        element.addEventListener("focus", (e) => {
            if (a) {
                a.style.cssText = "display:block"
            }
        })

        element.addEventListener("blur", () => {
            if (a) {
                a.style.cssText = "display:none"
            }
        })
    });


}
