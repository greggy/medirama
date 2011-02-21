from django import forms
from django.utils.safestring import mark_safe


class NameWidget(forms.Widget):
    '''Widget to render 'fancy pants' field name.'''
    def render(self, name, value, attrs=None):
        output = []
        output.append('''
<span> 
<input id="Field128" name="first_%s" type="text" class="field text fn" value="%s" size="8" tabindex="1" onkeyup="handleInput(this);" onchange="handleInput(this);" /> 
<label for="Field128">First</label> 
</span> 
<span> 
<input id="Field129" name="last_%s" type="text" class="field text ln" value="%s" size="14" tabindex="2" onkeyup="handleInput(this);" onchange="handleInput(this);" /> 
<label for="Field129">Last</label> 
</span>
        ''' % (name, value[0] if value else u'', name, value[1] if value else u''))
        return mark_safe(u' '.join(output))
    
    def value_from_datadict(self, data, files, name):
        return (data.get(u'first_name'), data.get(u'last_name'))