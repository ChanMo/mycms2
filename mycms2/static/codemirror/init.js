(function(){
    var $ = django.jQuery;
    $(document).ready(function(){
        $('textarea.html-editor').each(function(idx, el){
            var cm = CodeMirror.fromTextArea(el, {
                lineNumbers: true,
                mode: 'htmlmixed'
            });
            cm.setSize("80%", 500);
        });
    });
})();
