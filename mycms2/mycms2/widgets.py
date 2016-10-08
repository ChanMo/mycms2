from django import forms

class HtmlEditor(forms.Textarea):
    def __init__(self, *args, **kwargs):
        super(HtmlEditor, self).__init__(*args, **kwargs)
        self.attrs['class'] = 'html-editor'

    class Media:
        css = {
            'all': (
                'http://cdn.bootcss.com/codemirror/5.19.0/codemirror.min.css',
            )
        }
        js = (
            'http://cdn.bootcss.com/codemirror/5.19.0/codemirror.min.js',
            '//cdn.bootcss.com/codemirror/5.19.0/mode/xml/xml.min.js',
            'http://cdn.bootcss.com/codemirror/5.19.0/mode/htmlmixed/htmlmixed.min.js',
            '/static/codemirror/init.js'
        )
