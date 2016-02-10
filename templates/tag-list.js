window.tagList = [{% for i in items %}"{{ i|escapejs }}"{% if not forloop.last %},{% endif %}{% endfor %}]
