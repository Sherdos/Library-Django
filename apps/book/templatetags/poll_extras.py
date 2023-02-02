from django import template 
from django.utils.safestring import mark_safe   
register = template.Library() 
 
@register.simple_tag
def include_anything(file_name):
    file = open (file_name).read() #stores contents of the file in a variable 
    return mark_safe(file) 
